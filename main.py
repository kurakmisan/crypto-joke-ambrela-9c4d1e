"""One-line crypto trading joke for make.fun.

Writes a single original joke about crypto and trading life to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The joke (93 characters, ASCII, one line, no trailing newline):

    I bought a coin because its logo looked trustworthy. The logo is still up 400%. I am not.
"""

import os

JOKE = "I bought a coin because its logo looked trustworthy. The logo is still up 400%. I am not."

MAX_CHARS = 200


def main() -> None:
    """Validate the joke and write it to entry.txt with no trailing newline."""
    line = JOKE
    if not line or not line.strip():
        raise ValueError("joke must not be empty or whitespace only")
    if len(line) > MAX_CHARS:
        raise ValueError(f"joke is {len(line)} characters, over the {MAX_CHARS} limit")
    if "\n" in line or "\r" in line:
        raise ValueError("joke must be a single line")
    try:
        line.encode("ascii")
    except UnicodeEncodeError as exc:
        raise ValueError("joke must be ASCII only") from exc

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="ascii", newline="") as fh:
        fh.write(line)

    # Re-read and verify exactly what was written: one line, no trailing newline.
    with open(path, "rb") as fh:
        raw = fh.read()
    if raw != line.encode("ascii"):
        raise ValueError("written entry.txt does not match the joke exactly")
    if raw.endswith(b"\n") or raw.endswith(b"\r"):
        raise ValueError("entry.txt must not end with a newline")


if __name__ == "__main__":
    main()
