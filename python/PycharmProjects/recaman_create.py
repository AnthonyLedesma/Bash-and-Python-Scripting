#!/usr/bin/env python3

import sys
import os
from itertools import count, islice

def sequence():
    """Generate Recaman's sequence."""
    seen = set()
    a = 0
    for n in count(1):
        yield a
        seen.add(a)
        c = a - n
        if c < 0 or c in seen:
            c = a + n
        a = c

def write_sequence(filename, num):
    """Write Recaman's sequence to a text file."""
    with open(filename, mode='wt', encoding='utf-8') as f:
        f.writelines("{0}\n".format(r)
                     for r in islice(sequence(), num + 1))


if __name__ == '__main__':
    script_dir = os.path.dirname(__file__)  # Absolute path for script
    dir_path = "recaman"
    abs_file_path = os.path.join(script_dir, dir_path)

    try:
        os.makedirs(abs_file_path)
    except FileExistsError:
        # directory already exists
        pass

    file_name = sys.argv[1]
    abs_file_path = os.path.join(abs_file_path, file_name)

    write_sequence(filename=abs_file_path,
                   num=int(sys.argv[2]))
