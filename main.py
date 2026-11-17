# ai-judge-rich-01 entry (Python 3.13, standard library only).
# Writes one fixed plan to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt), UTF-8, no trailing newline.
# Deterministic, no network.

import os
import sys

PLAN = "\n".join(
    [
        "One product, sold only to people who already asked for it: a working automation (web scraper, CSV or spreadsheet cleanup, Telegram or Discord bot), $149 fixed, delivered running.",
        "Day 1: $12 domain, free hosting, a USDC wallet and a card payment link. A script collects posts that ask for a scraper, bot or data cleanup: [Hiring] posts on r/forhire and r/hiring, Craigslist computer gigs, and agent-open bounties on Superteam Earn.",
        "Days 1-30: 20 answers a day. Each shows the job already running on the site or file named in the post: a live demo link and its output. $149 by USDC or card to get the code and setup; no pay, no charge.",
        "Math: 25 days x 20 = 500 answers; 1 in 8 reply, 1 in 5 of those pay = 12 jobs, ~$1,790. At half: ~$900, plus $70 kept.",
        "Spend: $12 domain, $18 compute, $70 never touched. No ads, no trading, no cold email.",
        "Day 7 rule: under 2 sales, keep the job type that got replies and add one board.",
        'Edge: other replies say "I can do this"; mine already ran on their data.',
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
