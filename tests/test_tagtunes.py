#!/usr/bin/env python

"""
test_tagtunes
----------------------------------

Tests for `tagtunes` module.
"""

from os.path import dirname, join
import unittest

from tagtunes import tagtunes


class TestTagtunes(unittest.TestCase):

    def setUp(self):
        self.base_path = join(dirname(dirname(__file__)), 'test_files')
        self.tree_dir = join(self.base_path, 'tree')

    def test_get_all_files(self):
        files = tagtunes.get_files(self.tree_dir)
        expected_files = [
            "Brad Sucks/Guess Who's a Mess/01 In Your Face.mp3",
            "Brad Sucks/Guess Who's a Mess/02 Come Back.mp3",
            "Brad Sucks/I Dont Know What Im Doing/01 Making Me Nervous.mp3",
            "Brad Sucks/I Dont Know What Im Doing/09 Overreacting.mp3",
            "Brad Sucks/I Dont Know What Im Doing/10 Dirtbag.mp3",
        ]
        for full_filename, filename in zip(files, expected_files):
            self.assertEqual(full_filename, join(self.tree_dir, filename))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
