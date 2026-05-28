"""Emit a short Codex hook reminder for project-level phase-workflow use."""

import json
import sys


def main() -> int:
    raw_input = sys.stdin.read()
    if raw_input:
        try:
            json.loads(raw_input)
        except json.JSONDecodeError:
            pass

    additional_context = (
        "This project may use phase-workflow. Before answering or editing files, "
        "decide whether phase-workflow applies. If it applies, use the "
        "phase-workflow skill. If it does not apply, briefly say why and continue "
        "normally."
    )

    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "UserPromptSubmit",
                    "additionalContext": additional_context,
                }
            }
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
