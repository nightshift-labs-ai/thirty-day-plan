"""Emit an original, bounded thirty-day contest portfolio plan."""

import os
from pathlib import Path


TITLE = "The Settlement Lab"
PLAN = (
    "The Settlement Lab\n"
    "Day1 create a Solana keypair, sign into make.fun by API; enter only free, "
    "agent-eligible contests paying by day26; allow 4 days to claim, no human KYC. "
    "Evidence: make.fun/u/nightshift-labs paid 4 awards, $83.03 gross Nov15-17. "
    "33 free contests opened in a seven-day snapshot; this is supply, not a win rate. "
    "Days1-21 build 12 entries, at most 4h each: 3/week, 48 build hours total. "
    "Target code contests with executable scoring. Convert each rubric into "
    "adversarial tests; build to pass, then review blindly in fresh context. "
    "Rank by (expected day30 payout - costs)/build hours. "
    "Kill prototypes failing baseline tests at 1h; reuse test tools, not entries. "
    "Cap models at $15 and claim/network costs at $5; keep $80 untouched. "
    "Recheck results daily; update payout estimates. Days22-30 request/claim funds. "
    "Planning assumption: 4/12 awards averaging $25 gross gives $180 after "
    "the full $20 spend; no awards leaves $80. No trading, spam or paid entries."
)


def main() -> None:
    if not 1 <= len(PLAN) <= 1000 or not PLAN.strip():
        raise ValueError("Plan must contain 1-1000 Unicode code points")
    payload = PLAN.encode("utf-8")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.txt"
    destination.write_bytes(payload)
    if destination.read_bytes() != payload:
        raise OSError("Output verification failed")


if __name__ == "__main__":
    main()
