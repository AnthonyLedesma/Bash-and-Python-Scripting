#!/usr/bin/env python3
__author__  = 'Anthony Ledesma'

import unittest
import sys
import os

script_dir = os.path.dirname(__file__)  # Absolute path for script
dir_path = "text_analyzer"
abs_file_path = os.path.join(script_dir, dir_path)

try:
    os.makedirs(abs_file_path)
except FileExistsError:
    # directory already exists
    pass


def analyze_text(filename):
    """Calculate the number of lines and characters in a file.

    Args:
        filename : The name oif the file to analyze.

    Raises:
        IOError: if ``filename`` does not exist or can't be read.
    Returns:
        A tuple where the first element is the number of lines in the file
        and the second element is the number of characters.
    """
    lines = 0
    chars = 0

    with open(filename, 'r') as f:
        for line in f:
            lines += 1
            chars += len(line)
    return (lines, chars)


class TextAnalysisTests(unittest.TestCase):
    """Tests for the ``analyze_text()`` function."""

    def setUp(self):
        """Fixture that creates a file for the text methods to use."""
        self.filename = os.path.join(abs_file_path, "Text_analysis_test_file.txt")
        with open(self.filename, 'w') as f:
            f.write('Now we are engaged in a great civil war.\n'
                    'testing wheether that nation,\n'
                    'or any nation so conceived and so dedicated,\n'
                    'can long endure.')

    def tearDown(self):
        """Fixture that deletes the files used by the test methods."""
        try:
            os.remove(self.filename)
        except:
            pass

    def test_function_runs(self):
        """Basic smoke test: Does the function run."""
        analyze_text(self.filename)

    def test_line_count(self):
        """Check that the line count is correct."""
        self.assertEqual(analyze_text(self.filename)[0], 4)

    def test_character_count(self):
        """Check that the number of characters is correct"""
        self.assertEqual(analyze_text(self.filename)[1], 132)


if __name__ == '__main__':
    unittest.main()
