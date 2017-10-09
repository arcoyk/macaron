from subprocess import call
import os
import sys
import random

root = '/users/yui/desktop/movs/'
args = sys.argv[1:]

def titles(root):
  return list(map(lambda x:root + x, os.listdir(root)))

def match_any(tar, words):
  for word in words:
    if word.lower() in tar.lower():
      return True
  return False

def search(tars, posi=[], nega=[]):
  rst = []
  for tar in tars:
    if (not match_any(tar, nega)) and (match_any(tar, posi)):
      rst.append(tar)
  return rst

def parse_args(args):
  likes = list()
  dislikes = list()
  for arg in args:
    # Remove titles start with '-' (ex. '-bad_song')
    if arg[0] == '-':
      dislikes.append(arg[1:])
    else:
      likes.append(arg)
  return likes, dislikes

def instant_playlist(args):
  likes, dislikes = parse_args(args)
  playlist = titles(root)
  playlist = search(playlist, posi=likes, nega=dislikes) 
  loop = True
  mix = True
  if 'noloop' in args:
    loop = False
  if 'nomix' in args:
    mix = False
  return mix, loop, playlist

def keywords():
  name_line = (' ').join(os.listdir(root))
  words = name_line.split(' ')
  rst = []
  for word in list(set(words)):
    if words.count(word) > 4:
      rst.append(word)
  return rst

def show_playlist(playlist):
  print(u"🎵 Macaron:", len(playlist), "musics found!")
  for music in playlist:
    print(wrap(path2title(music)))
  print()

def path2title(path):
  return path.split('/')[-1]

def wrap(s):
  return "[[" + s + "]]"

def is_multi(a):
  return ['s',''][int(len(a) * 2 == 1)]

def show_indicator(music, playlist):
  print(u"🎵 Now Playing...", wrap(path2title(music)))
  print("in ", len(playlist), " music%s..." % is_multi(playlist))
  print()

def play(playlist, mix=False, loop=False):
  if not playlist:
    print(keywords())
    exit()
  if mix:
    random.shuffle(playlist)
  show_playlist(playlist)
  cmd = ' && afplay '.join(playlist)
  for music in playlist:
    show_indicator(music, playlist)
    call(['caffeinate', '-i', 'afplay', music])
  if loop:
    play(playlist, mix, loop)

mix, loop, playlist = instant_playlist(args)
play(playlist, mix, loop)
