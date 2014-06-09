#!/usr/bin/env python

"""
tagtunes.main
-----------------------------------

Main entry point for the `tagtunes` command.

The code in this module is also a good example of how to use Tag Tunes
as a library rather than a script.
"""

import argparse

from . import __version__


def get_tagtunes_args():
    """
    Get the command line input/output arguments passed into Tag Tunes.
    """

    parser = argparse.ArgumentParser(
        description='Command-line ID3 tag editor'
    )

    parser.add_argument('--version', action='version',
                        version='%(prog)s ' + __version__)

    args = parser.parse_args()
    return args


def main():
    args = get_tagtunes_args()

    # TODO: call function that does the main work here


if __name__ == '__main__':
    main()
