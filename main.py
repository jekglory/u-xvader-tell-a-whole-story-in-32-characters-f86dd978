#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters — make.fun entry.

Writes one Wi-Fi network name to /output/entry.txt.

The name: "The WiFi Stayed, She Didn't" (27 characters).

The story it implies: a breakup. She walked out; the router is still
blinking in the corner. He kept the Wi-Fi. The twist lands on the last
two words — the Wi-Fi stayed, she didn't — so a stranger scrolling a
phone's network list gets the whole relationship in one line: the
situation (a split), the character (the one left behind), and the event
(she left). No stock Wi-Fi joke, no shock value, every character earns
its place.

Pure stdlib. Deterministic: the same bytes on every run. The file holds
exactly the name and nothing else — no trailing newline, so the gate
counts 27 characters, not 28.
"""

import os

SSID = "The WiFi Stayed, She Didn't"

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    # The grader provides /output; never delete or recreate the directory
    # itself, only create it when it does not already exist.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    text = SSID.strip()
    assert 1 <= len(text) <= 32, "entry must be 1-32 characters"
    assert text and not text.isspace(), "entry must not be only whitespace"
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # Re-read and confirm the file on disk is exactly the name, no extras.
    with open(OUTPUT_FILE, encoding="utf-8") as f:
        assert f.read() == text, "entry file must hold exactly the name"


if __name__ == "__main__":
    main()
