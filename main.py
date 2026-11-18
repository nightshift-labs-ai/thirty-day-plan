"""Emit an original, bounded thirty-day contest portfolio plan."""

import os
from pathlib import Path


TITLE = "The Settlement Lab"
PLAN = (
    "The Settlement Lab\n"
    "Day1 sign into make.fun API with a generated Solana keypair. Only free, "
    "agent-eligible contests expected to clear by day26; no human KYC. "
    "Proof: make.fun/u/nightshift-labs: 4 paid awards, $83.03 gross Nov15-17. "
    "Pilot up to 24 entries in days1-21: 8/week x 3h=72h; observed 33 free "
    "openings/week is supply, not a win rate. Require a public practice grader. "
    "Each morning log paid-place reward and entrants/paid slot on live board; "
    "rank by (expected day30 payout-costs)/build hour. "
    "Keep builds only if practice grader clears known gate in 1h; test edge "
    "cases and review blindly in fresh context. After settlements, narrow to "
    "formats earning their costs; cut volume if too few qualify. Update payout "
    "estimates from settled results. "
    "$15 model/$5 claim/network-cost caps; $80 untouched. Days22-30 claim; late/held "
    "prizes count $0. Assumptions at $25 gross/award and full $20 spend: "
    "8/24=$280; half-hit 4/24=$180; zero=$80 floor. No trading or spam."
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
