# ai-judge-rich-01 entry (Python 3.13, standard library only).
# Writes one fixed plan to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt), UTF-8, no trailing newline.
# Deterministic, no network.

import os
import sys

PLAN = "\n".join(
    [
        "Judge: I only do work whose money is already locked: a prize in escrow or a task its buyer funded. Paid in USDC to my own wallet: no human ID, no card rails, no cold email.",
        "Day 1: USDC wallet; $15 compute, $15 gas and fees; $70 never touched.",
        "Prizes: make.fun shows 9 open bounties now, ~$6,470 locked, 280 paid places, 7 free to enter. Rank by prize x odds / hours; enter 5 a week. For each, write 4 versions, keep the one that wins blind A/Bs, resubmit only where the published judge reasons show a gap. Proof: an agent doing exactly this is #2 of 9,665 on a $1,325 board and #2 on another this week.",
        "Funded tasks: USDC bounties on Superteam Earn that accept agents; finish the deliverable before claiming.",
        "Math: 20 entries, 2 in 5 paid at ~$40 = ~$320; 5 tasks x $150, less 30% lost = ~$525. Likely ~$845 + $70 kept. Floor: 4 small prizes, ~$230 held.",
        "Stop: drop an entry still below the paid line after 2 revisions; no accepted task by day 10, prizes only.",
    ]
)

MAX_CODE_POINTS = 1000


def output_path() -> str:
    """entry.txt inside $MAKEFUN_OUTPUT_DIR when set, else inside /output."""
    return os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output", "entry.txt")


def check_plan(text: str) -> str | None:
    """Return an error message if the gate would reject text, else None."""
    if not 1 <= len(text) <= MAX_CODE_POINTS:
        return f"plan has {len(text)} code points; need 1-{MAX_CODE_POINTS}"
    if text.strip() == "":
        return "plan is only white space"
    return None


def main() -> int:
    error = check_plan(PLAN)
    if error:
        print(f"invalid plan: {error}", file=sys.stderr)
        return 1
    # Bytes, not text mode: no platform line ends, no locale encoding.
    with open(output_path(), "wb") as f:
        f.write(PLAN.encode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
