from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable


DEFAULT_COMPACT_STATE_CANDIDATES = (
    "CURRENT_STATE.md",
    "current_state.md",
    "HANDOFF.md",
    "handoff.md",
    "docs/handoff.md",
)

TODO_SECTION_HEADINGS = (
    "## Current Phase",
    "## Active Task",
    "## Next Tasks",
    "## Blocked",
    "## Blockers",
    "## Do Not Do Yet",
    "## Do-Not-Do-Yet",
)


class MCPReadError(RuntimeError):
    """Raised when a read would exceed the local read-only MCP boundary."""


def read_allowed_file(
    project_root: Path | str,
    relative_path: Path | str,
    allowed_files: Iterable[Path | str],
):
    """Read a single allowlisted project file and return source refs."""

    root = Path(project_root).resolve()
    normalized_path = _normalize_project_relative_path(root, relative_path)
    _ensure_allowed(normalized_path, allowed_files)
    target = root / normalized_path

    if not target.is_file():
        raise MCPReadError(f"allowlisted file does not exist: {normalized_path}")

    return {
        "path": normalized_path,
        "content": target.read_text(encoding="utf-8"),
        "source_refs": [normalized_path],
    }


def read_scoped_section(
    project_root: Path | str,
    relative_path: Path | str,
    heading: str,
    allowed_files: Iterable[Path | str],
):
    """Read a named markdown section from an allowlisted file."""

    file_result = read_allowed_file(project_root, relative_path, allowed_files)
    section_text = _extract_markdown_section(file_result["content"], heading)
    clean_heading = _clean_heading(heading)

    return {
        "path": file_result["path"],
        "content": section_text,
        "source_refs": [f"{file_result['path']}#{clean_heading}"],
    }


def get_default_snapshot(
    project_root: Path | str,
    allowed_files: Iterable[Path | str],
    guidance_paths: Iterable[Path | str] | None = None,
    compact_state_paths: Iterable[Path | str] | None = None,
):
    """Build the bounded default ChatGPT/MCP planning snapshot."""

    root = Path(project_root).resolve()
    allowed = tuple(allowed_files)
    items = []

    if (root / "AGENTS.md").is_file():
        items.append(read_allowed_file(root, "AGENTS.md", allowed))

    for guidance_path in guidance_paths or ():
        normalized = _normalize_project_relative_path(root, guidance_path)
        if (root / normalized).is_file():
            items.append(read_allowed_file(root, normalized, allowed))

    compact_candidates = tuple(compact_state_paths or DEFAULT_COMPACT_STATE_CANDIDATES)
    for compact_path in compact_candidates:
        normalized = _normalize_project_relative_path(root, compact_path)
        target = root / normalized
        if target.is_file() and _is_allowed(normalized, allowed):
            lines = target.read_text(encoding="utf-8").splitlines()
            items.append(
                {
                    "path": normalized,
                    "content": "\n".join(lines[:120]).rstrip() + "\n",
                    "source_refs": [f"{normalized}:1-120"],
                }
            )
            break

    if (root / "TODO.md").is_file():
        todo_file = read_allowed_file(root, "TODO.md", allowed)
        todo_result = _extract_todo_current_sections(todo_file["content"], todo_file["path"])
        items.append(todo_result)

    source_refs = []
    for item in items:
        source_refs.extend(item["source_refs"])

    return {
        "kind": "default_snapshot",
        "items": items,
        "source_refs": source_refs,
    }


def list_allowed_files(allowed_files: Iterable[Path | str]):
    return sorted({_normalize_allowed_path(path) for path in allowed_files})


def _normalize_project_relative_path(root: Path, relative_path: Path | str) -> str:
    raw_path = Path(relative_path)
    if raw_path.is_absolute():
        raise MCPReadError("path must be relative to the selected project root")

    candidate = (root / raw_path).resolve()
    try:
        normalized = candidate.relative_to(root).as_posix()
    except ValueError as exc:
        raise MCPReadError("path must stay inside project root") from exc

    if not normalized or normalized == ".":
        raise MCPReadError("path must name a project file")
    return normalized


def _normalize_allowed_path(path: Path | str) -> str:
    raw = str(path).replace("\\", "/").strip()
    if not raw:
        raise MCPReadError("allowed file path is empty")
    if raw.startswith("/") or Path(raw).is_absolute():
        raise MCPReadError("allowed file path must be relative")

    parts = [part for part in raw.split("/") if part not in ("", ".")]
    if not parts or any(part == ".." for part in parts):
        raise MCPReadError("allowed file path must stay inside project root")
    if ":" in parts[0]:
        raise MCPReadError("allowed file path must be relative")
    return "/".join(parts)


def _ensure_allowed(normalized_path: str, allowed_files: Iterable[Path | str]):
    if not _is_allowed(normalized_path, allowed_files):
        raise MCPReadError(f"file is not allowlisted: {normalized_path}")


def _is_allowed(normalized_path: str, allowed_files: Iterable[Path | str]) -> bool:
    return normalized_path in {_normalize_allowed_path(path) for path in allowed_files}


def _extract_markdown_section(text: str, heading: str) -> str:
    heading_line = heading.strip()
    start_match = None
    lines = text.splitlines()

    for index, line in enumerate(lines):
        if line.strip() == heading_line:
            start_match = (index, _heading_level(line))
            break

    if start_match is None:
        raise MCPReadError(f"section not found: {heading_line}")

    start_index, start_level = start_match
    end_index = len(lines)
    for index in range(start_index + 1, len(lines)):
        level = _heading_level(lines[index])
        if level is not None and level <= start_level:
            end_index = index
            break

    return "\n".join(lines[start_index:end_index]).rstrip() + "\n"


def _extract_todo_current_sections(text: str, relative_path: str):
    sections = []
    source_refs = []

    for heading in TODO_SECTION_HEADINGS:
        try:
            section = _extract_markdown_section(text, heading)
        except MCPReadError:
            continue

        if heading == "## Active Task":
            section = _filter_active_task_section(section)

        sections.append(section)
        source_refs.append(f"{relative_path}#{_clean_heading(heading)}")

    return {
        "path": relative_path,
        "content": "\n".join(sections).rstrip() + "\n",
        "source_refs": source_refs,
    }


def _filter_active_task_section(section: str) -> str:
    lines = section.splitlines()
    if not lines:
        return section

    filtered = [lines[0], ""]
    include_continuation = False
    found_unchecked = False

    for line in lines[1:]:
        if line.startswith("- [ ]"):
            filtered.append(line)
            include_continuation = True
            found_unchecked = True
            continue
        if re.match(r"^- \[[xX]\]", line):
            include_continuation = False
            continue
        if include_continuation and (line.startswith("  ") or not line.strip()):
            filtered.append(line)
            continue
        include_continuation = False

    if not found_unchecked:
        filtered.append("No active unchecked tasks.")

    return "\n".join(filtered).rstrip() + "\n"


def _heading_level(line: str) -> int | None:
    match = re.match(r"^(#{1,6})\s+\S", line)
    if not match:
        return None
    return len(match.group(1))


def _clean_heading(heading: str) -> str:
    return re.sub(r"^#{1,6}\s+", "", heading.strip()).strip()
