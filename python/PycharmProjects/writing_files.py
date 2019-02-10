#!/usr/bin/env python3
import os
import sys

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
    f.write('Out of this stony rubbish? ')
    f.close()


def open_file():

    g = open(abs_file_path, mode='rt', encoding='utf-8')
    print('...Reading the first 32 codepoints...')
    sys.stdout.write(g.read(32))
    print('...Then the rest of the file...')
    sys.stdout.write(g.read())
    print('...Seeking to the beginning...')
    g.seek(0)
    print('...Using readline() function instead...')
    sys.stdout.write(g.readline())
    sys.stdout.write(g.readline())
    print("...Seeking to the beginning...")
    g.seek(0)
    print("...using readlines() function...")
    sys.stdout.write("".join(g.readlines()))
    g.close()


def append_file():
    h = open(abs_file_path, mode='at', encoding='utf-8')  # append text mode
    h.writelines(
        ['son of man,\n',
         'You cannot say, or guess, ',
         'for you know only,\n',
         'A heap of broken images, ',
         'where the sun beats\n'])
    h.close()
