import os
import sys
from queue import LifoQueue

FILE_NAME = "dataset.txt"
LINES_TO_READ_COUNT = 1000

with open(FILE_NAME, "rb") as f:
    f.seek(0, os.SEEK_END)

    # Init temporary buffer for individual bytes.
    buffer = bytearray()
    # Init stack to store lines.
    lines = LifoQueue()

    current_position = f.tell()
    # Keep reading the file until the start of the file is reached
    # or required number of lines read.
    while current_position >= 0 and lines.qsize() <= LINES_TO_READ_COUNT:
        f.seek(current_position)

        byte = f.read(1)
        if byte == os.linesep.encode():
            # If current byte is a line separator then fixate the contents of
            # the buffer as a line and reset the buffer.
            # Since we read from the end we need to reverse.
            lines.put(buffer[::-1])
            buffer = bytearray()
        else:
            # Else just append the byte to the buffer.
            buffer.extend(byte)

        current_position -= 1

    # Process the very first line of the file if needed.
    # Since it does not end (start) from the line separator it won't be
    # fixated in the above `while`.
    if buffer:
        lines.put(buffer[::-1])

    # Output collected lines decoded from bytes to string.
    first = True
    while not lines.empty():
        if not first:
            sys.stdout.write(os.linesep)
        first = False
        line = lines.get().decode()
        sys.stdout.write(line)
