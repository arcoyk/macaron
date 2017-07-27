from subprocess import call
import os
import sys
import random

root = '/users/yui/desktop/movs/'
playlist = list()
args = sys.argv[1:]
for d in os.listdir(root):
    for arg in args:
        if d.lower().find(arg) != -1:
            playlist.append(root + d)
if not playlist:
    print("I'm hungry (songs not found)")
random.shuffle(playlist)
cmd = ' && afplay '.join(playlist)
for music in playlist:
    print('🎵  Now Playing...', music, "in", len(playlist), "songs in instant playlist...")
    call(['afplay', music])
