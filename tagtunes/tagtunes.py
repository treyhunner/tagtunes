from collections import defaultdict
import os

import mutagenx


TAG_ORDERING = ['artist', 'album', 'tracknumber', 'title']
TAG_NAMES = {
    'artist': "Artist",
    'album': "Album",
    'tracknumber': "Track",
    'title': "Title",
}


def get_all_files(path):
    for root, dirs, files in os.walk(path):
        files.sort()
        for filename in files:
            yield os.path.join(root, filename)


def tree():
    return defaultdict(tree)


def group_by_tags(filenames):
    groupings = tree()
    counter = defaultdict(lambda: 1)
    for filename in filenames:
        tag_analyzer = mutagenx.File(filename, easy=True)
        if tag_analyzer is None:
            continue
        artist = "".join(tag_analyzer.tags['artist'])
        album = "".join(tag_analyzer.tags['album'])
        track = "".join(tag_analyzer.tags.get('tracknumber', ''))
        if track:
            track = track.zfill(2)
        else:
            track = "No Track " + str(counter[artist, album]).zfill(2)
            counter[artist, album] += 1
        groupings[artist][album][track] = tag_analyzer
    return groupings


def set_track_numbers(tag_analyzers):
    for track, tag_analyzer in enumerate(tag_analyzers, start=1):
        tag_analyzer['tracknumber'] = str(track).zfill(2)
        tag_analyzer.save()
