import time
import os


def now():
    return int(time.time() * 1e9)


def deep_ensure_directory_exists(dirr):
    """recursively add the directories"""
    all_directories = []
    while True:
        all_directories.append(dirr)
        try:
            dirr = os.path.dirname(dirr)
            if len(dirr) < 3:
                break
        except:
            break
    for dirr in reversed(all_directories):
        if not os.path.exists(dirr):
            os.mkdir(dirr)
    return


def ensure_dir_and_file_exists(pathy):
    if os.path.exists(pathy):
        return
    dirr = os.path.dirname(pathy)
    if not os.path.exists(dirr):
        os.makedirs(dirr)
    if not os.path.exists(pathy):
        open(pathy, 'x')
    return
