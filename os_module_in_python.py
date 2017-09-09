import os
from datetime import datetime

# Get current working dir getcwd()
print(os.getcwd())

# make dir - mkdir(dirname)
os.mkdir('dir1')

# make dir within dir - makedirs(dirname)
os.makedirs('dir2/subdir1')

# remove dir - rmdir(dirname)
os.rmdir('dir1')

# remove dir within dir - removedirs(dirnames)
os.removedirs('dir2/subdir1')

# list files and folders in dir listdir
print(os.listdir())

# rename files - rename(filename, new_filename)
#os.rename('text.txt', 'demo.txt')

# stat of file - stat(filename)
print(os.stat('demo.txt'))

# print mod time of file.
mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

# change dir - chdir()
#os.chdir('c:/')

# walking through dir - walk()
for dirpath, dirnames, filenames in os.walk('C:/Users/Sainath/Music'):
    print("Current path: ", dirpath)
    print("Dirs: ", dirnames)
    print("File: ", filenames)
    print()

# print file name
print(os.path.basename('C:/Users/Sainath/Music/Demo.txt'))

# print dir name
print(os.path.dirname('C:/Users/Sainath/Music/Demo.txt'))

# print both file and dir name
print(os.path)
print(os.path.split('C:/Users/Sainath/Music/Demo.txt'))
print(os.path.splitext('C:/Users/Sainath/Music/Demo.txt'))

# check path exists
print(os.path.exists('C:/Users/Sainath/Music/Demo.txt'))