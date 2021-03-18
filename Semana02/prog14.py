import os

os.chdir('/Users/anaju/Documents/Playlist')

for f in os.listdir():
    print(os.path.splitext(f))

