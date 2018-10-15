from lfw import add_extension
import os

def read_pairs(pairs_filename):
    pairs = []
    with open(pairs_filename) as f:
        for line in f.readlines():
            pair = line.strip().split()
            pairs.append(pair)
    return pairs

def get_paths(frt_dir, pairs):
    path_list = []
    issame_list = []
    for pair in pairs:
        erste_path = os.path.join(os.path.expanduser(frt_dir), pair[0], pair[1])
        path_list.append(erste_path)
        zweite_path = os.path.join(os.path.expanduser(frt_dir), pair[2], pair[3])
        path_list.append(zweite_path)
        if pair[0] == pair[2]:
            issame_list.append(True)
        else:
            issame_list.append(False)
    return path_list, issame_list
