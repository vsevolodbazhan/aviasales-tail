import os
import sys
import time
from queue import LifoQueue


class Tail:
    """Class representation of the `tail` command.

    Parameters
    ----------
    file_name : str
        The name of the file to read.
    follow : bool, optional
        Wait for additional data to be appended to the file, by default `False`.
    lines_to_read : int, optional
        The number of lines to read, by default 10.
    sleep_delay : float, optional
        Sleep delay in seconds to use when `follow=True`, by default 0.5.
    """

    def __init__(
        self,
        file_name: str,
        follow: bool = False,
        lines_to_read: int = 10,
        sleep_delay: float = 0.5,
    ) -> None:
        self.file_name = file_name
        self.follow = follow
        self.lines_to_read = lines_to_read
        self.sleep_delay = sleep_delay

    def __call__(self) -> None:
        self.tail()
        if self.follow:
            self.perform_follow()

    def tail(self) -> None:
        with open(self.file_name, "rb") as f:
            f.seek(0, os.SEEK_END)

            # Init temporary buffer for individual bytes.
            buffer = bytearray()
            # Init stack to store lines.
            lines: LifoQueue = LifoQueue()

            current_position = f.tell()
            # Keep reading the file until the start of the file is reached
            # or required number of lines read.
            while current_position >= 0 and lines.qsize() <= self.lines_to_read:
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

    def perform_follow(self) -> None:
        with open(self.file_name, "r") as f:
            f.seek(0, os.SEEK_END)
            while True:
                line = f.readline()
                # If the received line is empty -- sleep to ease the CPU load.
                if not line:
                    time.sleep(self.sleep_delay)
                sys.stdout.write(line)
