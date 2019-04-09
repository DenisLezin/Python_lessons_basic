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

#-----------------------------------------------------------
# заготовки для модуля
# def make_dir1(directory):
# #    directory = os.path.join(os.getcwd(), dname)
#     if not os.path.exists(directory):
#         os.mkdir(directory)
#         print('Created directory: ' + dname)
#     else:
#         print('Directory alredy exists')
#
# def remove_dir1(directory):
# #    directory = os.path.join(os.getcwd(), dname)
#     if os.path.exists(directory):
#         os.rmdir(directory)
#         print('Deleted directory: ' + dname)
#     else:
#         print('There is no such directory')
#------------------------------------------------------------
from easy import make_dir1, remove_dir1
import os
import sys

cur_dir = os.getcwd()


# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
