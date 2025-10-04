import ast
import csv
from collections import OrderedDict
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parent.parent / "greenfield_plan_4_150_tasks.csv"
OUTPUT_PATH = Path(__file__).resolve().parent.parent / "TASKLIST.md"


def parse_collection(raw: str):
    if not raw:
        return []
    try:
        value = ast.literal_eval(raw)
    except Exception:
        return [raw.strip()]
    if isinstance(value, (list, tuple, set)):
        return [str(item) for item in value]
    return [str(value)]


def format_list(values):
    if not values:
        return "None"
    return ", ".join(f"`{value}`" for value in values)


def build_markdown(rows):
    by_epic = OrderedDict()
    for row in rows:
        epic_key = (row["epic"], row["epic_name"])
        by_epic.setdefault(epic_key, []).append(row)

    lines = []
    lines.append("# Greenfield #4 Task Checklist")
    lines.append("")
    lines.append(
        "This document lists the 150 tasks defined in `greenfield_plan_4_150_tasks.csv` "
        "with checkboxes so progress can be tracked directly in the repository."
    )
    lines.append("")

    total_tasks = len(rows)
    lines.append(f"- **Total tasks:** {total_tasks}")
    lines.append(f"- **Source file:** `{CSV_PATH.name}`")
    lines.append("")

    for (epic_code, epic_name), tasks in by_epic.items():
        lines.append(f"## {epic_name} (Epic {epic_code})")
        lines.append("")
        for task in tasks:
            expected_outputs = format_list(parse_collection(task["expected_outputs"]))
            acceptance_criteria = format_list(parse_collection(task["acceptance_criteria"]))
            dependencies = format_list(parse_collection(task["dependencies"]))

            lines.append(
                f"- [ ] **{task['title']}** — Task `{task['task_id']}`"
            )
            lines.append(
                f"  - **Area:** {task['area']}  |  **Owner:** {task['owner']}  |  "
                f"**Complexity:** {task['complexity']}  |  **Status:** {task['status']}"
            )
            lines.append(f"  - **Description:** {task['description']}")
            lines.append(f"  - **Expected outputs:** {expected_outputs}")
            lines.append(f"  - **Acceptance criteria:** {acceptance_criteria}")
            lines.append(f"  - **Dependencies:** {dependencies}")
            lines.append(f"  - **Created at:** {task['created_at']}")
            lines.append("")
        lines.append("")

    return "\n".join(line.rstrip() for line in lines).strip() + "\n"


def main():
    with CSV_PATH.open(newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)
    markdown = build_markdown(rows)
    OUTPUT_PATH.write_text(markdown, encoding="utf-8")


if __name__ == "__main__":
    main()
