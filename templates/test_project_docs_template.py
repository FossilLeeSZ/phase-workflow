import pathlib
import re


ROOT = pathlib.Path(__file__).resolve().parents[1]
PHASE_ID = re.compile(r"\bPhase\s+\d+(?:\.\d+)?\b", re.IGNORECASE)
REVISION = re.compile(
    r"(?im)^\s*-\s*phase-contract revision:\s*([^\s]+)\s*$"
)


def _read_root_file(relative_path, label):
    candidate = pathlib.Path(relative_path)
    assert not candidate.is_absolute(), f"{label} path must be project-relative: {relative_path}"
    assert ".." not in candidate.parts, f"{label} path escapes the project: {relative_path}"

    project_root = ROOT.resolve()
    resolved = (ROOT / candidate).resolve()
    assert resolved.is_relative_to(project_root), f"{label} path escapes the project: {relative_path}"
    assert resolved.is_file(), f"{label} file is missing: {relative_path}"
    return resolved.read_text(encoding="utf-8")


def _markdown_section(text, heading, label):
    lines = text.splitlines()
    matches = [index for index, line in enumerate(lines) if line.strip() == heading]
    assert len(matches) == 1, f"{label} heading must occur exactly once: {heading}"

    start = matches[0]
    level = len(heading) - len(heading.lstrip("#"))
    end = len(lines)
    for index in range(start + 1, len(lines)):
        match = re.match(r"^(#+)\s+", lines[index])
        if match and len(match.group(1)) <= level:
            end = index
            break
    return "\n".join(lines[start:end])


def _phase_id(text, label):
    matches = {match.group(0).casefold(): match.group(0) for match in PHASE_ID.finditer(text)}
    assert len(matches) == 1, f"{label} must identify exactly one Phase ID: {sorted(matches.values())}"
    return next(iter(matches))


def _owner_pointer(todo, label):
    anchors = _markdown_section(todo, "## Context Anchors", "TODO Context Anchors")
    match = re.search(
        rf"(?ms)^-\s*{re.escape(label)}:\s*`([^`]+)`\s*->\s*`([^`]+)`",
        anchors,
    )
    assert match, f"TODO Context Anchors is missing the {label} pointer"
    return match.group(1), match.group(2)


def _current_phase(todo):
    section = _markdown_section(todo, "## Current Phase", "TODO Current Phase")
    return _phase_id(section, "TODO Current Phase")


def _revision(section, label):
    matches = REVISION.findall(section)
    assert len(matches) == 1, f"{label} must contain exactly one phase-contract revision"
    return matches[0]


def _owner_state():
    todo = _read_root_file("TODO.md", "TODO owner")
    plan_path, plan_heading = _owner_pointer(todo, "PLAN phase")
    note_path, note_heading = _owner_pointer(todo, "Active phase note")
    plan = _read_root_file(plan_path, "PLAN owner")
    note = _read_root_file(note_path, "active phase note")
    return todo, plan, plan_heading, note, note_heading


def test_current_owner_pointers_resolve():
    _todo, plan, plan_heading, note, note_heading = _owner_state()
    _markdown_section(plan, plan_heading, "PLAN heading")
    _markdown_section(note, note_heading, "active phase note heading")


def test_current_phase_matches_independent_owners():
    todo, plan, plan_heading, note, note_heading = _owner_state()
    current = _current_phase(todo)
    plan_phase = _phase_id(plan_heading, "PLAN heading")
    note_heading_phase = _phase_id(note_heading, "active phase note heading")
    note_phase_section = _markdown_section(note, "## Phase", "active phase note Phase section")
    note_phase = _phase_id(note_phase_section, "active phase note Phase field")

    assert plan_phase == current, (
        f"TODO Current Phase does not match PLAN heading: TODO={current}, PLAN={plan_phase}"
    )
    assert note_heading_phase == current, (
        "TODO Current Phase does not match active phase note heading: "
        f"TODO={current}, note={note_heading_phase}"
    )
    assert note_phase == current, (
        "TODO Current Phase does not match active phase note Phase field: "
        f"TODO={current}, note={note_phase}"
    )


def test_current_contract_revisions_match():
    _todo, plan, plan_heading, note, note_heading = _owner_state()
    plan_section = _markdown_section(plan, plan_heading, "PLAN heading")
    note_section = _markdown_section(note, note_heading, "active phase note heading")
    plan_revision = _revision(plan_section, "PLAN phase")
    note_revision = _revision(note_section, "active phase note")

    assert plan_revision == note_revision, (
        "contract revision mismatch: "
        f"PLAN={plan_revision}, active phase note={note_revision}"
    )
