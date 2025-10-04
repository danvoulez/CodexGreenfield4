# CodexGreenfield4

This repository hosts planning artifacts for the "Greenfield #4" benchmark DSL initiative. The primary data source is the `greenfield_plan_4_150_tasks.csv` file that enumerates 150 discrete tasks across multiple epics.

## Task checklist

A generated `TASKLIST.md` file mirrors the CSV contents as a Markdown checklist so progress can be tracked with checkboxes. Each entry includes:

- Task metadata (ID, epic, area, owner, complexity, status).
- Narrative details (description, expected outputs, acceptance criteria, dependencies, creation timestamp).

You can regenerate the checklist after editing the CSV by running:

```bash
python scripts/generate_tasklist.py
```

The script reads the CSV and overwrites `TASKLIST.md` with an up-to-date checklist grouped by epic.
