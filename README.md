# Macaron 🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵
is a python script to play musics in a local folder through terminal for MacOS.

```
# Save songs in your favorite folder.
# Rewrite 'root' (in play.py) to the folder.
python play.py michael
# will play michael's songs (if they exist in the folder)!
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

5. Makes it easier😎⚡️
```
echo "alias play='python /the/path/you/cloned/macaron/play.py' >> ~/.bashrc"
source ~/.bashrc
play michael
```

# Details of Instant Playlist

Instant Playlist is a list of path to music files.
macaron creates Instant Playlist through commands. For example,

```
python play.py michael
# Now playing 1 of 12 Michael's songs..
```

will create a playlist of Michale's songs if you have his songs.
Here, 'michael' hits songs whose title has 'michael' in any part of it (lower case, upper case).
For example,

```
python play.py michael
# Now playing michael.mp3 in ['michael.mp3', 'michael_jackson.mp3', 'michaeljackson.mov', 'George_Michael.mp3', 'Michael.mp3', 'MICHAEL.mp4']
```

You can also set multiple arguments.
```
python play.py michael justin
# Now playing michael.mp3 in ['michael.mp3', 'michael_jackson.mp3', 'michaeljackson.mov', 'George_Michael.mp3', 'Michael.mp3', 'MICHAEL.mp4', 'justin.mp3']
```

Or you can remove 'George_Michael.mp3'.

```
python play.py michael justin -george
# Now playing michael.mp3 in ['michael.mp3', 'michael_jackson.mp3', 'michaeljackson.mov', 'Michael.mp3', 'MICHAEL.mp4', 'justin.mp3']
```

🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵
