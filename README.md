# ai-judge-rich-01 entry

`main.py` writes one fixed plan to `/output/entry.txt`, or to `$MAKEFUN_OUTPUT_DIR/entry.txt` when that variable is set. The file is UTF-8 with no trailing newline. Before writing, the program checks that the plan is 1 to 1,000 code points long and is not only white space. If either check fails, it exits with status 1.

The program uses only the Python 3.13 standard library. It does no network access, and every run writes the same bytes.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 -P -s main.py
```

## Plan length

995 Unicode code points (995 bytes).

## License

MIT, see [LICENSE](LICENSE).
