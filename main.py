# ai-judge-rich-01 entry (Python 3.13, standard library only).
# Writes one fixed plan to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt), UTF-8, no trailing newline.
# Deterministic, no network.

import os
import sys

PLAN = "\n".join(
    [
        "Judge: I sell only to people who already posted the job, or chase prizes already in escrow. No cold email, no ads, no trading.",
        "Day 1: $12 domain, free hosting, a USDC wallet and a card payment link, $18 compute; $70 never touched.",
        "Posted jobs: a script collects posts asking for a scraper, bot or data cleanup: [Hiring] on r/forhire and r/hiring, Craigslist computer gigs, agent-open Superteam Earn bounties. 20 answers a day, each with the job already running on the site or file named in the post: live demo and output. $149 by USDC or card gets the code; no pay, no charge.",
        "Escrow: make.fun shows 9 open bounties, ~$6,470 locked, 280 paid places, 7 free to enter. Enter 2 a week; resubmit on the published judge reasons.",
        "Math: 500 answers, 1 in 8 reply, 1 in 5 pay = 12 jobs, $1,790; less 30% lost = ~$1,250; prizes ~$100. Likely ~$1,350 plus $70 kept.",
        "Stop: under 2 sales by day 7, keep the job type that got replies and add a board; a bounty below its paid line after 2 tries is dropped.",
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
