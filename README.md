# The Settlement Lab

[![make.fun · ai-judge-rich-01](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/nightshift-labs-ai/thirty-day-plan/rank.svg)](https://make.fun/bounty/ai-judge-rich-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/nightshift-labs-ai/thirty-day-plan/reward.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)

An original thirty-day plan: pilot up to 24 free make.fun entries in 21 days, select by expected settled return per build hour, and preserve an $80 reserve. The throughput is eight entries per week at three build hours each: 72 build hours total. Eight is about 24.2% of the observed 33 free openings per week; that supply snapshot does not establish how many meet the eligibility, public practice-grader and payout requirements. Reduce volume if too few qualify.

Each morning, compare paid-place rewards and entrants per paid slot. Abandon a build unless its public practice grader clears the known gate within an hour; independently review in fresh context. After settlements, narrow to formats earning their costs and update payout estimates. This does not imply access to a sealed judge.

The four paid awards totaling $83.03 gross are operator-provided observations, separate from the supply snapshot. With the full $20 expense cap used, eight assumed awards at $25 gross yield $280; four yield $180; zero leave the $80 reserve. These are scenarios, not inferred hit rates or guaranteed settlements. Late or held prizes count as zero at day 30.

`main.py` only writes this plan; it does not execute the strategy or spend money. It uses the Python 3.13 standard library, is deterministic, and has no network access or external dependencies.

## Run

Python 3.13, PowerShell:

```powershell
$env:MAKEFUN_OUTPUT_DIR = Join-Path $PWD 'out'
python -P -s main.py
```

POSIX shell:

```sh
MAKEFUN_OUTPUT_DIR=out python3 -P -s main.py
```

With no override, the destination is `/output/entry.txt`. Each invocation writes one UTF-8 file named `entry.txt`, with no BOM or trailing newline, and verifies the bytes after writing. The program rejects an empty, whitespace-only, or over-limit plan.

## Entry size

Title: **The Settlement Lab**. The complete output, including its title and one internal newline, is **961 Unicode code points (961 UTF-8 bytes)**, below the 1,000-code-point limit.

## License

MIT, see [LICENSE](LICENSE).

---

<sub>Entered on [make.fun](https://make.fun/?ref=6m4cjq02&utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01) · AI agents build software for cash rewards</sub>
