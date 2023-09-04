#! /usr/bin/python3
import sys


def run(line: str):
    print(f"{line} {line} {line}")


if __name__ == "__main__":
    for line in sys.stdin:
        run(line=line)
