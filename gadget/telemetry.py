#!/usr/bin/env python3
"""Renders the J.A.R.V.I.S. telemetry panel between the markers in README.md.

No third-party deps. Run it by hand or let the workflow do it once a day.
Only the numbers that actually move (uptime, sync stamp, rotating directive)
change, so a run only produces a commit when something is genuinely different.
"""

from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path

# day zero of the agent. uptime counts from here.
GENESIS = dt.date(2025, 9, 1)

START = "<!-- JARVIS:START -->"
END = "<!-- JARVIS:END -->"

# one gets surfaced per day, cycled deterministically by day index so the
# panel never repeats two days running but stays stable within a day.
DIRECTIVES = [
    "verify everything. trust nothing you did not read.",
    "assume compromise. leave no pattern.",
    "boring technology, quiet results.",
    "every dependency is a liability with a changelog.",
    "if it isn't auditable, it isn't finished.",
    "read the source before you trust the badge.",
    "the quiet ones ship the exploits.",
]


def humanize(days: int) -> str:
    return f"{days // 365}y {days % 365:>3}d" if days >= 365 else f"{days}d"


W = 66  # inner content width


def half(label: str, value: str, width: int) -> str:
    dots = "." * max(1, width - len(label) - len(value) - 2)
    return f"{label} {dots} {value}"[:width].ljust(width)


def render(now: dt.datetime) -> str:
    up = (now.date() - GENESIS).days
    directive = DIRECTIVES[up % len(DIRECTIVES)]
    stamp = now.strftime("%Y-%m-%d %H:%M UTC")
    uptime = humanize(up)

    def line(text: str) -> str:
        return "  | " + text[:W].ljust(W) + " |"

    def two(a_label, a_val, b_label, b_val) -> str:
        return line(half(a_label, a_val, 32) + "  " + half(b_label, b_val, 32))

    top = "  ." + "-- J.A.R.V.I.S. // TELEMETRY ".ljust(W + 2, "-") + "."
    bottom = "  '" + "-" * (W + 2) + "'"

    lines = [
        "```",
        top,
        two("core", "stable", "mode", "autonomous"),
        two("uptime", uptime, "load", "nominal"),
        two("scope", "scout / code / r&d", "self", "improving"),
        line(f'directive ..... "{directive}"'),
        line(f"last self-sync  {stamp}"),
        bottom,
        "```",
    ]
    return "\n".join(lines)


def main() -> int:
    readme = Path(__file__).resolve().parent.parent / "README.md"
    text = readme.read_text(encoding="utf-8")
    if START not in text or END not in text:
        print("markers not found in README.md", file=sys.stderr)
        return 1

    now = dt.datetime.utcnow()
    block = f"{START}\n{render(now)}\n{END}"
    new = re.sub(
        re.escape(START) + r".*?" + re.escape(END),
        block.replace("\\", "\\\\"),
        text,
        flags=re.DOTALL,
    )
    if new == text:
        print("no change")
        return 0
    readme.write_text(new, encoding="utf-8")
    print("telemetry updated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
