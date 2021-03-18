import os

from datetime import datetime
os.chdir('/Users/anaju/Desktop')

mod_time = (os.stat('demo.txt').st_mtime)
print(datetime.fromtimestamp(mod_time))

# print(os.listdir())