import os

ENTRY = "Noddrift (n.): nodding along to a conversation you stopped actually hearing minutes ago."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    with open(out_dir + "/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
