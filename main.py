"""Write the entry review for make.fun's "One-Star Review" bounty.

The entry is one original deadpan one-star review of an everyday
essential: a single line of at most 160 characters. This program writes
that line to entry.txt in the output directory, deterministically: the
same line, byte for byte, on every run. Standard library only; no
network.
"""

import os

LINE = "★☆☆☆☆ Sleep: promised eight hours of rest. Delivered six hours of replaying an argument from 2014 and two hours of listening for the alarm."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DESTINATION = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    if not 1 <= len(LINE) <= 160:
        raise ValueError("review must be 1 to 160 characters")
    if not LINE.strip():
        raise ValueError("review must not be only whitespace")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # make.fun collects the outputs as another user than the one the
    # program runs as, so the output must be readable by everyone.
    os.chmod(OUTPUT_DIR, 0o755)
    with open(DESTINATION, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    os.chmod(DESTINATION, 0o644)
    print("wrote {} ({} characters)".format(DESTINATION, len(LINE)))


if __name__ == "__main__":
    main()
