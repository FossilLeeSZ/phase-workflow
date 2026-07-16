"""Emit a bounded Codex reminder for explicit phase-workflow prompts."""

import json
import re
import sys


EXACT_CONTINUATIONS = re.compile(
    r"^(?:下一步|确认|确认执行|确认规划|确认修改|next step|confirm|"
    r"confirm execution|confirm plan)[。.!！?？]?$",
    re.IGNORECASE,
)

WORKFLOW_CUES = (
    re.compile(r"(?:\$)?phase-workflow\b", re.IGNORECASE),
    re.compile(r"\bphase\s+workflow\b", re.IGNORECASE),
    re.compile(r"\b(?:phase|start)\s+gate\b", re.IGNORECASE),
    re.compile(r"(?:启动门|执行门|阶段门)"),
    re.compile(
        r"\b(?:show|start|continue|begin|enter|execute|confirm)\b.{0,48}"
        r"\bphase\s*\d+(?:\.\d+)*\b",
        re.IGNORECASE,
    ),
    re.compile(
        r"\bphase\s*\d+(?:\.\d+)*\b.{0,48}"
        r"(?:\bgate\b|\bstart\b|\bcontinue\b|\bexecute\b|\bplan\b|"
        r"确认|启动门|执行门|阶段门)",
        re.IGNORECASE,
    ),
    re.compile(
        r"(?:展示|开始|继续|执行|进入|确认).{0,24}\bphase\s*\d+(?:\.\d+)*\b",
        re.IGNORECASE,
    ),
    re.compile(
        r"\b(?:update|modify|recover|inspect)\b.{0,32}\b(?:plan\.md|todo\.md)\b",
        re.IGNORECASE,
    ),
    re.compile(r"(?:更新|修改|恢复|检查).{0,16}(?:PLAN\.md|TODO\.md|计划|规划)", re.IGNORECASE),
    re.compile(r"\b(?:scope|plan)\s+change\b|范围变更|修改计划|更新规划", re.IGNORECASE),
)


def is_workflow_prompt(prompt: str) -> bool:
    prompt = prompt.strip()
    if not prompt:
        return False
    if EXACT_CONTINUATIONS.fullmatch(prompt):
        return True
    return any(pattern.search(prompt) for pattern in WORKFLOW_CUES)


def main() -> int:
    raw_input = sys.stdin.read()
    if not raw_input.strip():
        return 0

    try:
        payload = json.loads(raw_input)
    except json.JSONDecodeError:
        return 0

    if not isinstance(payload, dict):
        return 0
    if payload.get("hook_event_name") != "UserPromptSubmit":
        return 0

    prompt = payload.get("prompt")
    if not isinstance(prompt, str) or not is_workflow_prompt(prompt):
        return 0

    additional_context = (
        "This prompt appears related to phase-workflow. Open the installed "
        "phase-workflow SKILL.md, revalidate current anchors, and preserve the "
        "visible-gate and separate live-confirmation boundary. This reminder does "
        "not invoke the skill and does not authorize execution."
    )

    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "UserPromptSubmit",
                    "additionalContext": additional_context,
                }
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
