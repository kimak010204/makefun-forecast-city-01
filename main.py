"""Funniest Forecast for a City That Isn't.

Writes one line, at most 120 characters: a weather forecast for the
invented city of Grumbletown, in flat bulletin phrasing that breaks
when the drizzle turns out to be spiteful.
"""

import os

ENTRY = (
    "Grumbletown: drizzle falls sideways out of spite. "
    "Locals urged to lean left and not take it personally."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 120, f"entry length {len(ENTRY)} out of range"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and re-check what actually landed on disk.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written entry differs from ENTRY"
    assert 1 <= len(written) <= 120
    assert "\n" not in written and "\r" not in written


if __name__ == "__main__":
    main()
