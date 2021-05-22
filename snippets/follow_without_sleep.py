import os
import sys

FILE_NAME = "dataset.txt"
LINES_TO_READ_COUNT = 10

with open(FILE_NAME, "r") as f:
    f.seek(0, os.SEEK_END)
    while True:
        line = f.readline()
        sys.stdout.write(line)
