# Verification Policy

Use this policy to decide whether a phase can be marked complete. Every phase needs actual
command-based verification.

## Default Command

Use this command unless the project defines a more specific test command:

```bash
python -m pytest -q
```

## Rules

- Run the verification command before marking a phase complete.
- Do not use "should run" or "looks correct" as completion standards.
- Record the actual command and result in `DEV_LOG.md`, a phase note, or a handoff note.
- If verification fails, do not mark the phase complete.
- If a CLI exists, run a smoke test that exercises the CLI entry point.
- If a web app exists, run the relevant build or browser smoke test.
- If a command cannot be run, record the exact reason and leave the phase open.

## What To Record

Record:

- Command.
- Date.
- Exit status.
- Short result summary.
- Failures or warnings that matter.
- Follow-up task if the command failed.

Example:

```text
Command: python -m pytest -q
Result: 6 passed in 0.05s
Notes: No warnings.
```

## Failed Verification

When verification fails:

1. Keep the phase open.
2. Record the failing command and main failure.
3. Fix the issue using a test-first approach when behavior changes.
4. Run verification again.
5. Update the development log with the final result.
