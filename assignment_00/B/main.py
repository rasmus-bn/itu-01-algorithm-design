#! /usr/bin/python3
import sys


def run(line: str):
    new_line = []
    for char in line:
        if char == "<":
            new_line.pop()
        else:
            new_line.append(char)
    print("".join(new_line))


if __name__ == "__main__":
    for line in sys.stdin:
        run(line=line)
