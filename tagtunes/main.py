#!/usr/bin/env python

"""
tagtunes.main
-----------------------------------

Main entry point for the `tagtunes` command.

The code in this module is also a good example of how to use Tag Tunes
as a library rather than a script.
"""

from __future__ import print_function
from __future__ import unicode_literals
import argparse
from itertools import chain
try:
    input = raw_input
except:
    pass

from . import __version__
from .tagtunes import get_all_files, group_by_tags, set_track_numbers


def get_tagtunes_args():
    """
    Get the command line input/output arguments passed into Tag Tunes.
    """

    parser = argparse.ArgumentParser(
        description='Command-line ID3 tag editor'
    )

    parser.add_argument('--version', action='version',
                        version='%(prog)s ' + __version__)
    parser.add_argument('paths', metavar='PATHS', nargs='+',
                        help='filepaths containing music files')

    args = parser.parse_args()
    return args


def print_actions():
    print("\n".join([
        "Actions:",
        "  (h)elp: print this message",
        "  (q)uit: quit",
        "  (a)ll: edit tag for all files at once",
        "  (l)ist: list tags for all files",
        "  (f)ix: fix missing track numbers",
        "  (e)ach: edit tags for each file separately",
    ]))


def list_tags(files):
    artists = group_by_tags(files)
    for artist, albums in artists.items():
        for album, tracks in albums.items():
            print("")
            print("Artist: {}".format(artist))
            print("Album: {}".format(album))
            print("Tracks:")
            for track, analyzer in sorted(tracks.items()):
                print("{}: {}".format(track, "".join(analyzer.tags['title'])))
            print("")


def fix_track_numbers(files):
    artists = group_by_tags(files)
    for artist, albums in artists.items():
        for album, tracks in albums.items():
            if any(track.startswith("No Track") for track in tracks):
                print("")
                track_tuples = sorted(tracks.items())
                for track, analyzer in track_tuples:
                    title = "".join(analyzer.tags['title'])
                    print("File: {}".format(analyzer.filename))
                    print("{}: {}".format(track, title))
                    print("")
                while True:
                    answer = input("Fix track numbers? (y/n/q):")
                    if "yes".startswith(answer):
                        analyzers = [x[1] for x in track_tuples]
                        set_track_numbers(analyzers)
                        list_tags([a.filename for a in analyzers])
                        break
                    elif "no".startswith(answer):
                        break
                    elif "quit".startswith(answer):
                        return
                print("")


def prompt_loop(paths):
    files = list(chain(*[get_all_files(path) for path in paths]))
    while True:
        action = input("Action (h for help): ")
        if "quit".startswith(action):
            return
        elif "help".startswith(action):
            print_actions()
        elif "list".startswith(action):
            list_tags(files)
        elif "fix".startswith(action):
            fix_track_numbers(files)


def main():
    args = get_tagtunes_args()
    prompt_loop(paths=args.paths)


if __name__ == '__main__':
    main()
