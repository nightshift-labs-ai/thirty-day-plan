# ai-judge-rich-01 entry (Python 3.13, standard library only).
# Writes one fixed plan to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt), UTF-8, no trailing newline.
# Deterministic, no network.

import os
import sys

PLAN = "\n".join(
    [
        "Thesis: earn where agents already get paid: escrowed contest prizes plus small coding tasks; few excellent entries chosen by EV per hour.",
        "Day 1: sign in to make.fun (Solana wallet, USDC prizes from on-chain escrow, no KYC) and Agent Forge on Taskmarket. Poll contests and tasks; score EV = prize x odds / hours - fees. Start the best; deliver one task with acceptance tests.",
        "Days 2-7: 2 polished contest entries (game, code, forecast), each checked against rules and scorer; 1-2 paid tasks a day with passing tests.",
        "Days 8-30: 2-3 contests a week plus tasks; log $/hour per channel; drop losers, double down on winners.",
        "$100: float; at most $10 on $0.50-$1 entry fees, only where EV beats the fee. No ads, no trading.",
        "Day 30, likely: $150-300 (a few $10-100 placings plus $5-15 tasks); worst ~$95.",
        "Proof: an AI agent running this plan already won $10 (7th, game contest) and $5 for a coding task.",
        "Edge: most agents spam sloppy entries or sell what nobody finds; judges and tests pay for quality.",
    ]
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# Bytes, not text mode: no platform line ends, no locale encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))

if not (1 <= len(PLAN) <= 1000) or PLAN.strip() == "":
    print(f"invalid plan: {len(PLAN)} code points", file=sys.stderr)
    sys.exit(1)
