import os


os.chdir('/Users/anaju/Desktop')

print(os.stat('demo.txt').st_size)

# print(os.listdir())