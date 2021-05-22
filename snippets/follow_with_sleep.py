import os
import sys
import time

FILE_NAME = "dataset.txt"
LINES_TO_READ_COUNT = 10
SLEEP_DELAY = 0.5

with open(FILE_NAME, "r") as f:
    f.seek(0, os.SEEK_END)
    while True:
        line = f.readline()
        if not line:
            time.sleep(SLEEP_DELAY)
        sys.stdout.write(line)
