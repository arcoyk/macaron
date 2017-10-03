# macaron 🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵
afplay command interface of python

```
python play.py michael
> Playing 'Michael Jackson Song.mp3'
```

# Usage

1. Clone
```
git clone git@github.com:arcoyk/macaron.git
```

2. Create a folder with A LOT OF songs you like.

3. Edit the root to your folder
```play.py
root = '/a/folder/of/songs/you/like/'
```

4. Play
```
python play.py michael
```

# Why

macaron enables you to enjoy BGM from your terminal.
macaron creates instant playlist. For example,

```
python play.py michael
```

will create a playlist of (possibly) Michaael Jackson. Current version is capable of finding songs by matching arguments to...

- the part of the file name (ex. 'michael' matches 'michael_jackson.mp3')
- upper case name by either upper case of lower case name (ex. 'Michael Jackson.mp3' can be found either by 'Michael' or 'michael'

but unintentionally...

- 'michael' matches 'michael douglas.mp3'

You can also set mutliple arguments.
```
python play.py michael justin
# Will create a playlist of (possibly) Michael Jackson and Justin Beaver
```

# Extension

- as a backend of voice controled AI

🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵
