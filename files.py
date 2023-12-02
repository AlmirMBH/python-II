import os
import shutil

# file detection
paths = [
    '/Users/almirmustafic/Downloads/Books/clean_architecture.mobi',
    '/Users/almirmustafic/Downloads/Books',
]

for path in paths:
    if os.path.exists(path):
        print("The path exists!")

        if os.path.isfile(path):
            print("A file is on the path!")
        elif os.path.isdir(path):
            print("A directory is on the path!")
        else:
            print("Another format than a file is on the path!")
    else:
        print("The path does not exist")


# reading files line by line
try:
    with open('/Users/almirmustafic/Downloads/Books/random_file.txt') as file:
        print('FILE: ' + file.read())
        # Python expects some code here. If the 'pass' or code are not present an error will be thrown.
except FileNotFoundError:
    print("The file is not found!")
except Exception:
    print("Something went wrong!")
else:
    print(file.closed)  # if the file is closed, the output is True


# writing into files
text = " This is a new sentence added to the random_file.txt"

try:
    with open('/Users/almirmustafic/Downloads/Books/random_file.txt', 'a') as file:  # wa (write, append)
        file.write(text)
    with open('/Users/almirmustafic/Downloads/Books/random_file.txt') as file:
        print('FILE WITH NEW TEXT: ' + file.read())
except FileNotFoundError:
    print("The file is not found!")
except Exception:
    print("Something went wrong!")
else:
    print(file.closed)  # if the file is closed, the output is True


# Copying files
# All functions below receive the same arguments, but they copy different things
# copyfile() - copies contents of a file
# copy() - copyfile() + permission mode + destination can be a directory
# copy2() - copy() copies metadata (file's creation and modification time)
copied_file_1 = '/Users/almirmustafic/Downloads/Books/copied_random_file.txt'

shutil.copyfile('/Users/almirmustafic/Downloads/Books/random_file.txt',
                '/Users/almirmustafic/Downloads/Books/copied_random_file.txt')  # src.dst

if os.path.exists(copied_file_1):
    with open(copied_file_1) as copied_file:
        print('COPIED FILE: ' + copied_file.read())
