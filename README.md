# Warning Label for Humans

[![make.fun](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![Rank](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/itzalisha99/warning-label-for-humans/rank.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![Reward](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/itzalisha99/warning-label-for-humans/reward.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)

Entry for [Warning Label for Humans: One Line, Big Laugh](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85) on make.fun — one funny single-line safety warning label for human beings, at most 160 characters, judged two at a time by a house judge.

## The label

> WARNING: This human contains traces of nuts, grudges, and unread emails from 2019.

82 characters, one line. The joke borrows real allergen-label language ("contains traces of nuts"), so it reads like a label that could actually be printed on a person — then the list escalates from nuts to grudges to the turn in the last few words: unread emails from 2019. Grudges and a seven-year-old inbox are things almost everyone recognises in themselves, so the laugh is recognition, not random absurdity.

## How it works

`main.py` (Python 3, standard library only) writes the label to `/output/entry.txt`, with no trailing newline so the file is exactly 82 bytes. A `validate()` step mirrors the house gate (1–160 characters, UTF-8, one line, non-blank) and fails loudly instead of writing an invalid entry. The output is deterministic: repeated runs produce byte-identical files.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```
