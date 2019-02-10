"""Read and print an integer series."""
import sys
import os


def read_series(filename):
    with open(filename, mode="rt", encoding="utf-8") as f:
        return [int(line.strip()) for line in f]


def main(filename):
    series = read_series(filename)
    print(series)


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
    main(abs_file_path)
