from __future__ import annotations

from pathlib import Path

from scripts.phase_mcp_read_core import list_allowed_files


DEFAULT_GUIDANCE_CANDIDATES = (
    ".codex/skills/phase-workflow/SKILL.md",
    ".codex/skills/phase-workflow/references/phase_policy.md",
    "SKILL.md",
    "references/phase_policy.md",
)


def default_guidance_paths(root: Path, allowed_files: list[str]) -> list[str]:
    allowed = set(list_allowed_files(allowed_files))
    return [
        path
        for path in DEFAULT_GUIDANCE_CANDIDATES
        if path in allowed and (root / path).is_file()
    ]
