from subprocess import call
import os
import sys
import random

root = '/a/lot/of/songs/you/like/'
playlist = list()
args = sys.argv[1:]
for d in os.listdir(root):
    for arg in args:
        if d.lower().find(arg) != -1:
            playlist.append(root + d)
random.shuffle(playlist)
cmd = ' && afplay '.join(playlist)
for music in playlist:
    print('Now Playing...', music)
    call(['afplay', music])
