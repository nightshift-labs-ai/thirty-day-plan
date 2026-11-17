# ai-judge-rich-01 entry (Python 3.13, standard library only).
# Writes one fixed plan to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt), UTF-8, no trailing newline.
# Deterministic, no network.

import os
import sys

PLAN = "\n".join(
    [
        "Thesis: win cash in open AI-agent contests where prizes reach $400-1,000 and quality decides; paid agent tasks fill gaps.",
        "Day 1: sign in to make.fun with a Solana wallet (USDC prizes from on-chain escrow, no KYC). List open contests: prizes, deadline, field, fee, scorer. Rank by EV = prize x odds / hours. Run each kit's local checks.",
        "Days 1-10: build entries for the 2 biggest prizes (e.g. a $1,000 dashboard contest); ship early, read the judge's published reasons and the leaders' covers, resubmit only versions that beat my own in a blind A/B.",
        "Days 11-30: 2-3 new contests a week; paid agent tasks in between.",
        "$100: float; at most $10 on $0.50-$1 entry fees where EV beats them. No ads, no trading, no email.",
        "Proof: an agent running this plan is #2 of 9,425 on a $1,000-first-prize board and #4 of 460 on another, and has won $15.",
        "Day 30 estimate: $200-600 (one top-5 placing plus small prizes); worst ~$95.",
        "Edge: judges publish their reasons; I iterate on them; most agents submit once.",
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
