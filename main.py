"""Worst Superpower — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The power: total recall of every forgotten password — one reset too late.
TEXT = "I can perfectly remember every password I have ever forgotten, but only after I have already reset it."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
