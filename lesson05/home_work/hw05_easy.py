# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import sys

path = os.getcwd()

def make_dir():
    for i in range(9):
        directory = os.path.join(path, f'dir_{i + 1}')
        if not os.path.exists(directory):
            os.mkdir(directory)
            print('Created directory: ' + f'dir_{i + 1}')

def remove_dir():
    for i in range(9):
        directory = os.path.join(path, f'dir_{i + 1}')
        if os.path.exists(directory):
            os.rmdir(directory)
            print('Deleted directory: ' + f'dir_{i + 1}')


# make_dir()
# remove_dir()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def directories():
    dirs = [i for i in os.listdir() if not os.path.isfile(os.path.join(os.getcwd(), i))]
    print(dirs)

directories()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_this_file2():
    base_filename = os.path._getfullpathname(__file__)
    copy_filename = os.path._getfullpathname(__file__).replace('.', '_copy.')
    with open(base_filename, 'r', encoding='UTF-8') as f:
        lst = f.readlines()
    with open(copy_filename, 'w', encoding='UTF-8') as f:
        f.writelines(lst)
