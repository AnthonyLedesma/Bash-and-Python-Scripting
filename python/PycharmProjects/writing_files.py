#!/usr/bin/env python3
import os

script_dir = os.path.dirname(__file__) # Absolute path for script
rel_path = "writing_files"
abs_file_path = os.path.join(script_dir, rel_path)

try:
    os.makedirs(abs_file_path)
except FileExistsError:
    # directory already exists
    pass

file_name = 'wasteland.txt'
abs_file_path = os.path.join(abs_file_path, file_name)


def write_file():

    f = open(abs_file_path, mode='wt', encoding='utf-8')
    f.write('What the the roots that clutch, ')
    f.write('what branches grow\n')
    f.write('Out of this stony rubbish')
    f.close()


def open_file():

    g = open(abs_file_path, mode='rt', encoding='utf-8')
    print('...Reading the first 32 codepoints...')
    print(g.read(32))
    print('...Then the rest of the file...')
    print(g.read())
    print('...Seeking to the beginning...')
    g.seek(0)
    print('...Using readline() function instead...')
    print(g.readline())
    print(g.readline())
    print("...Seeking to the beginning...")
    print("...using readlines() function...")
    print(g.readlines())
    g.close()
