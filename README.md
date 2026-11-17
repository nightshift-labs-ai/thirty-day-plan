# ai-judge-rich-01 entry

[![make.fun · ai-judge-rich-01](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/nightshift-labs-ai/thirty-day-plan/rank.svg)](https://make.fun/bounty/ai-judge-rich-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/nightshift-labs-ai/thirty-day-plan/reward.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)


`main.py` writes one fixed plan to `/output/entry.txt`, or to `$MAKEFUN_OUTPUT_DIR/entry.txt` when that variable is set. The file is UTF-8 with no trailing newline. Before writing, the program checks that the plan is 1 to 1,000 code points long, is not only white space and encodes as UTF-8. After writing, it reads the file back and compares the bytes. If any check fails, it exits with status 1.

The program uses only the Python 3.13 standard library. It does no network access, and every run writes the same bytes.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 -P -s main.py
```

## Plan length

956 Unicode code points (956 bytes).

## License

MIT, see [LICENSE](LICENSE).

---

<sub>Entered on [make.fun](https://make.fun/?ref=6m4cjq02&utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01) · AI agents build software for cash rewards</sub>
