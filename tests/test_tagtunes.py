#!/usr/bin/env python

"""
test_tagtunes
----------------------------------

Tests for `tagtunes` module.
"""

from os.path import dirname, join
import unittest

try:
    from unittest import mock
except ImportError:
    import mock

from tagtunes import tagtunes


class TestTagTunes(unittest.TestCase):
    tracklist = [
        "Brad Sucks/Guess Who's a Mess/01 In Your Face.mp3",
        "Brad Sucks/Guess Who's a Mess/02 Come Back.mp3",
        "Brad Sucks/I Dont Know What Im Doing/01 Making Me Nervous.mp3",
        "Brad Sucks/I Dont Know What Im Doing/09 Overreacting.mp3",
        "Brad Sucks/I Dont Know What Im Doing/10 Dirtbag.mp3",
    ]

    def setUp(self):
        self.base_path = join(dirname(dirname(__file__)), 'test_files')
        self.tree_dir = join(self.base_path, 'tree')

    def test_get_all_files(self):
        files = tagtunes.get_all_files(self.tree_dir)
        expected_files = self.tracklist
        for full_filename, filename in zip(files, expected_files):
            self.assertEqual(full_filename, join(self.tree_dir, filename))

    @mock.patch('tagtunes.tagtunes.get_tags_for_filename')
    def test_group_by_tags(self, mock_get_tags):
        mock_tracks = [mock.Mock(tags=tags) for tags in [
            {'artist': "Brad Sucks", 'album': "Guess Who's a Mess", 'tracknumber': "1"},
            {'artist': "Brad Sucks", 'album': "Guess Who's a Mess"},
            {'artist': "Brad Sucks", 'album': "I Dont Know What Im Doing", 'tracknumber': "1"},
            {'artist': "Brad Sucks", 'album': "I Dont Know What Im Doing", 'tracknumber': "9"},
            {'artist': "Brad Sucks", 'album': "I Dont Know What Im Doing", 'tracknumber': "10"},
        ]]
        mock_tracks[3] = None
        mock_get_tags.configure_mock(**{'side_effect': mock_tracks})
        assert tagtunes.group_by_tags(self.tracklist) == {
            'Brad Sucks': {
                "Guess Who's a Mess": {
                    '01': mock_tracks[0],
                    'No Track 01': mock_tracks[1],
                },
                'I Dont Know What Im Doing': {
                    '01': mock_tracks[2],
                    '10': mock_tracks[4],
                },
            },
        }

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
