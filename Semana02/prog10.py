import os

from datetime import datetime
os.chdir('/Users/anaju/Desktop')

for dirpath, dirnames, filenames in os.walk('/Users/anaju/Desktop'):
    print('Current Path:',dirpath)
    print('Directories:',dirnames)
    print('Files',filenames)
    print()