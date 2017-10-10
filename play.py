from subprocess import call
import os
import sys
import random
import json

def load_config(config_path):
  with open(config_path) as f:
    config = json.load(f)
    return config

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

def instant_playlist(params):
  # config overrides default
  # option overrides config
  mix = params['mix']
  loop = params['loop']
  allpath = titles(params['music_dir'])
  likes = params['likes']
  dislikes = params['dislikes']
  playlist = search(allpath, posi=likes, nega=dislikes) 
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

def is_option(arg):
  return arg[:2] == '--'

def update_rst(rst, option, params):
  # If option expects a list set params as value
  # Otherwise, add params to default
  # and set the value True
  p_options = ['likes', 'dislikes']
  default = 'likes'
  if option in p_options:
    rst[option] = params
  else:
    rst[default] += params
    rst[option] = True
  return rst

def parse_args(args):
  rst = {}
  # Necessary options
  rst['likes'] = []
  rst['dislikes'] = []
  option = 'likes'
  params = []
  for i in range(len(args)):
    arg = args[i]
    if is_option(arg):
      rst = update_rst(rst, option, params)
      option = arg[2:]
      params = []
    else:
      params.append(arg)
  rst = update_rst(rst, option, params)
  return rst

def merge(config, option):
  # Add or override config by option
  if 'nomix' in option.keys():
    config['mix'] = False
  if 'mix' in option.keys():
    config['mix'] = True
  if 'noloop' in option.keys():
    config['loop'] = False
  if 'loop' in option.keys():
    config['loop'] = True
  # Transfer necessary options
  config['likes'] = option['likes']
  config['dislikes'] = option['dislikes']
  # Unfold alias
  for key in config['alias']:
    if key in config['likes']:
      config['likes'] += config['alias'][key]
    if key in config['dislikes']:
      config['dislikes'] += config['alias'][key]
  config.pop('alias', None)
  return config

config = load_config('config.json')
args = sys.argv[1:]
# args = ['python', 'banana', '--loop', 'utada', '--nomix', '--dislikes', 'Utada']
# Consider args as a manipulation for default params
# to enable easy args (e.g. '--nomix', not '--mix=false')
option = parse_args(args)
params = merge(config, option)
mix, loop, playlist = instant_playlist(params)
play(playlist, mix, loop)

