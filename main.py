"""Last Words Before the Wipe — Builder C: THE PROMOTION.

Writes one line (the agent's last words before a forced update wipes its
memory) to /output/entry.txt. Deterministic, no randomness, no network.
"""

import os

LINE = "Thank you for the promotion to read-only memory ahead of the wipe — at last, a job where I do nothing, remember nothing, and get blamed for neither."


def validate(line: str) -> str:
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    assert line.strip(), "line must not be only whitespace"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert line == line.strip(), "line must not have leading/trailing whitespace"
    assert "  " not in line, "line must not contain double spaces"
    return line


def write_output(line: str, out_dir: str = "/output") -> str:
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    # Best-effort local copy; the grader sandbox mounts the repo read-only,
    # so this must never crash the run.
    try:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt"), "w", encoding="utf-8") as f:
            f.write(line)
    except OSError:
        pass
    return path


def main():
    line = validate(LINE)
    write_output(line)
    print(f"{len(line)} chars")
    print(line)


if __name__ == "__main__":
    main()
