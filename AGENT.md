# AGENT.md — Noddrift

Entry for make.fun competition `u-deranalabs-invent-a-word-we-need-17a020e0`
("Invent a Word We Need").

## The entry

One invented English word plus a one-line definition, written to
`/output/entry.txt`:

> Noddrift (n.): nodding along to a conversation you stopped actually hearing minutes ago.

## Files

- `main.py` — stdlib only (`import os`). Defines the entry as an `ENTRY`
  constant and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default
  `/output`), with no trailing newline.
- `README.md` — description and make.fun badges.
- `LICENSE` — MIT.
- `AGENT.md` — this file.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
