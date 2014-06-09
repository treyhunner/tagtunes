import os


def get_all_files(path):
    for root, dirs, files in os.walk(path):
        files.sort()
        for filename in files:
            yield os.path.join(root, filename)
