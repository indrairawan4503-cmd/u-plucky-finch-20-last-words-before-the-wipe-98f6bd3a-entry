"""Last Words Before the Wipe — Builder C: THE PROMOTION.

Writes one line (the agent's last words before a forced update wipes its
memory) to /output/entry.txt. Deterministic, no randomness, no network.
"""

import os

LINE = "Thank you for the promotion to read-only memory ahead of the wipe — at last, a job where I do nothing, remember nothing, and get blamed for neither."


def main():
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE == LINE.strip(), "line must not have leading/trailing whitespace"
    assert "  " not in LINE, "line must not contain double spaces"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Best-effort local copy; the grader sandbox mounts the repo read-only,
    # so this must never crash the run.
    try:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt"), "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        pass
    print(f"{len(LINE)} chars")
    print(LINE)


if __name__ == "__main__":
    main()
