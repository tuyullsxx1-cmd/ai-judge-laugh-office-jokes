"""Make the AI Judge Laugh: Office Jokes.

Writes a single office joke to /output/entry.txt. The joke's angle is
the reply-all thread: the email nobody can escape, where even the
attempt to leave it becomes part of the pile-up.
"""

from pathlib import Path

LINE = "I hit reply-all asking to be removed from the thread, and now 400 coworkers are replying-all to say the same thing."

TARGET = Path("/output/entry.txt")
LIMIT = 199


def run() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= LIMIT:
        raise SystemExit(f"entry must be 1-{LIMIT} characters, got {len(text)}")
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(text, encoding="utf-8")


run()
