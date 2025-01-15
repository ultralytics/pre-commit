# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

import re
from pathlib import Path

EXCLUDE_TERMS = ["import", "return", "def ", "class ", ".", "=", ":", "(", ",", "["]


def capitalize_comment_line(line: str, prev_was_comment: bool) -> str:
    """Capitalizes the first letter of a standalone inline comment."""
    # Skip lines containing any of the exclude terms
    if any(term in line for term in EXCLUDE_TERMS):
        return line

    # Skip if previous line was a comment
    if prev_was_comment:
        return line

    return re.sub(r"^(\s*)# (\w)", lambda m: f"{m.group(1)}# {m.group(2).upper()}", line)


def process_file(file_path: Path):
    """Processes a file and capitalizes the first letter of standalone inline comments."""
    with file_path.open("r") as f:
        lines = f.readlines()

    prev_was_comment = False
    processed_lines = []
    for line in lines:
        if is_comment := line.strip().startswith("#"):
            processed_line = capitalize_comment_line(line, prev_was_comment)
            processed_lines.append(processed_line)
            prev_was_comment = True
        else:
            processed_lines.append(line)
            prev_was_comment = False

    with file_path.open("w") as f:
        f.writelines(processed_lines)


if __name__ == "__main__":
    import sys

    for file in sys.argv[1:]:
        process_file(Path(file))
