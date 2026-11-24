import os

TEXT = "★★★★☆ Stunning blue marble, baffling locals: they invented machines to carry them everywhere, then pay to run in place indoors. Superb sunsets. Would abduct again."

def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
