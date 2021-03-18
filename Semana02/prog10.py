import os

from datetime import datetime
os.chdir('/Users/anaju/Desktop')

print(os.environ.get('HOMEPATH'))

'test.txt'

file_path = os.path.join(os.environ.get('HOMEPATH'),'test.txt')
print(file_path)

