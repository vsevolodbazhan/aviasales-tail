import random
import string

from tqdm import tqdm

OUTPUT_FILE_NAME = "dataset.txt"
LINES_COUNT = 1_000_000
CHARS_IN_LINE_COUNT = 1_000

with open(OUTPUT_FILE_NAME, "w") as f:
    for i in tqdm(range(LINES_COUNT)):
        for _ in range(CHARS_IN_LINE_COUNT):
            f.write(random.choice(string.hexdigits))
        f.write("\n")
