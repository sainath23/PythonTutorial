# File handling in python using context manager.

# using read().
try:
    with open('test111.txt', 'r') as f:
        f_contents = f.read()
        print("Using read(): ", f_contents)
except FileNotFoundError as e:
    print('File does not exists!', e)

# using readlines()
with open('test.txt', 'r') as f:
    f_contents = f.readlines()
    print("\nUsing readlines(): ", f_contents)

# using readline()
with open('test.txt', 'r') as f:
    f_contents = f.readline()
    print("\nUsing readline(): ", f_contents, end='')
    f.seek(0)
    f_contents = f.readline()
    print("\nUsing readline(): ", f_contents, end='')


#with open('test.txt', 'r') as f:

    #for line in f:
        #print(line, end='')

    #f_contents = f.readlines()
    #print("\nUsing readlines(): ", f_contents)

with open('test.txt', 'r') as f:
    print('')
    size_to_read = 50
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(size_to_read)

with open('test2.txt', 'w') as f:
    f.write('Hey there!')
    f.write('\nIts me')

with open('test.txt', 'r') as read_file:
    with open('test_copy.txt', 'w') as write_file:
        for line in read_file:
            write_file.write(line)

# Reading and writing binary picture file
with open('fb.png', 'rb') as read_file:
    with open('fb_1.png', 'wb') as write_file:
        chunk_size = 4096
        rf_chunk = read_file.read(chunk_size)
        while len(rf_chunk) > 0:
            write_file.write(rf_chunk)
            rf_chunk = read_file.read(chunk_size)


print("\n", f.closed)