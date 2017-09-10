# Python script to rename all the files in dir

import os

os.chdir('C:\\Users\\Sainath\\Documents\\Python\\pics')

for my_file in os.listdir():
    #print(my_file)
    f_name, f_ext = os.path.splitext(my_file)
    print(f_name)
    f_title, f_course, f_num = f_name.split('-')
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2) # zfill() makes char wide
    #print('{}-{}-{}'.format(f_num, f_course, f_ext))
    new_name = '{}-{}-{}'.format(f_num, f_course, f_ext)

    os.rename(my_file, new_name)