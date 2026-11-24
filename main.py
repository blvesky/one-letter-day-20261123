import os

ENTRY = "Y"
OUTPUT_PATH = "/output/entry.txt"


def main():
    # Write today's one-letter entry (a single uppercase Y, no newline).
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
