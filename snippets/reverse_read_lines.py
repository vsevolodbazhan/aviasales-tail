import sys

FILE_NAME = "dataset.txt"
LINES_TO_READ_COUNT = 10

with open(FILE_NAME, "r") as f:
    lines_read = 0
    for line in reversed(f.readlines()):
        sys.stdout.write(line)
        lines_read += 1
        if lines_read == LINES_TO_READ_COUNT:
            break
