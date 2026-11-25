"""Entry for make.fun bounty: How Many Tabs Do You Have Open?

Writes the entry number to /output/entry.txt with no trailing newline.
One number in digits and nothing else.
"""

from pathlib import Path

ENTRY_TEXT = "137"

OUTPUT_PATH = Path("/output/entry.txt")


def render_entry() -> bytes:
    """Return the entry encoded exactly as it will be stored."""
    return ENTRY_TEXT.encode("utf-8")


def write_entry() -> None:
    """Write the entry text to the output file exactly as specified."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(render_entry())


if __name__ == "__main__":
    write_entry()
