# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

from easy import make_dir, remove_dir, change_dir
import os
import sys
import shutil


def print_help():
    print(f'\nСейчас вы находитесь: {os.getcwd()}')
    print(f'Вы можете выбрать:\n')
    print(f'1. Перейти в другую директорию')
    print(f'2. Просмотреть содержимое текущей директории')
    print(f'3. Удалить директорию')
    print(f'4. Создать директорию')
    print(f'5. Вернуться в исходную директорию')
    print(f'6. Закончить работу')
    return input(f'Выберите пункт меню: ')

do = {
    '1': change_dir,
    '2': os.listdir,
    '3': remove_dir,
    '4': make_dir,
    }

answer = ''

while answer != 'q':
#    os.system('clear') if os.name == 'posix' else os.system('cls')
    answer = print_help()
    if answer == '1':
        dir_name = input(f'Введите полное имя директории: ')
        do[answer](dir_name)
    elif answer in ['3', '4']:
        dir_name = input(f'Введите имя директории: ')
        do[answer](dir_name)
    elif answer == '2':
        print(f'Список директорий и файлов:\n{do[answer]()}')
    elif answer == '5':
        change_dir(os.path.dirname(os.path.abspath(__file__)))
    elif answer == '6':
        break
    else:
        print('Такого пункта в меню нет')
        continue
    input('Для продолжения нажмите Enter')





# print(os.path.dirname(os.path.abspath(__file__)))


# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
