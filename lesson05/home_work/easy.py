
import os

# i = 'dir1'

def make_dir(*dirs):
    for i in dirs:
        if not i:
            print('Не указано имя директории')
            return
        path = os.path.join(os.getcwd(), i)
        try:
            os.mkdir(path)
            print(f'Создана директория {i}')
        except FileExistsError:
            print(f'Директория {i} уже существует')
        finally:
            pass


def remove_dir(*dirs):
    for i in dirs:
        if not i:
            print('Не указано имя директории')
            return
        path = os.path.join(os.getcwd(), i)
        try:
            os.rmdir(path)
            print(f'Удалена директория {i}')
        except FileNotFoundError:
            print(f'Директории {i} не существует')
        finally:
            pass

def change_dir(dir):
    if not dir:
        print('Не указано имя директории')
        return
    try:
        os.chdir(dir)
        print(f'Вы перешли в директорию: {dir}')
    except FileNotFoundError:
        print('Такой директории не существует')


# remove_dir()