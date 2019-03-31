# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

# import re
#
# str1 = '5/6 + 4/7'
# str2 = '-2/3 - -2'
# str3 = '5 4/6 + -7 4/5 - -4/3 + 8'
#
# def g_delimiter1(n, m):
#     '''
#     принимает два числа и возвращает наибольший общий делитель
#     '''
#     nums = [max(n, m), min(n, m)]
#     return nums[len(nums) - 1] if nums[len(nums) - 2] % nums[len(nums) - 1] == 0 else \
#         g_delimiter1(nums[len(nums) - 1], nums[len(nums) - 2] % nums[len(nums) - 1])
#
#
# def optim_num(num):
#     '''
#     Преобразует входящий список([числитеь, знаменатель]) в список элементов простой дроби.
#     Корректирует целую часть и сокращает дробную.
#     :param res: [числитель, знамнатель]
#     :return: [целая часть, числитель, знаменатель]
#     '''
#     res = num[:]
#     res.insert(0, 0) if len(res) == 2 else res
#
#     if res[1] % res[2] == 0:
#         res[0] += res[1] // res[2]
#         res[1] = 0
#         res[2] = 0
#     else:
#         # ниже (num[1] / abs(num[1])) корректирует знак
#         res[0] += int(abs(res[1]) // abs(res[2]) * (res[1] / abs(res[1])))
#         g_del = g_delimiter1(abs(res[1]), res[2])
#         res[1] = int(abs(res[1]) % res[2] / g_del)
#         res[2] = int(res[2] / g_del)
#     return res
#
# def optim_for_calc(num):
#     '''
#     Приводит дробь к виду [числитель, знаменатель]
#     '''
#     if len(num) == 1:
#         return [num[0], 1]
#     elif len(num) == 2:
#         return num
#     else:
#         return [int((num[1] + abs(num[0]) * num[2]) * (num[0] / abs(num[0]))), num[2]]
#
# def sum_param(num1, num2, sign):
#     '''
#     Производит арифметические действия с дробями вида [числитель, знаменатель]
#     На вход принимает две дроби в виде [числитель, знаменатель] и знак операции - '+'
#     :param num1: [числитель, знаменатель]
#     :param num2: [числитель, знаменатель]
#     :param sign: '+'
#     :return: [числитель, знаменатель]
#     '''
#     num1 = optim_for_calc(list(map(int, re.split(r' |/', num1)))) if type(num1) == str else num1
#     num2 = optim_for_calc(list(map(int, re.split(r' |/', num2))))
#
#     if re.match(r'[-+]', sign) != None:
#         num2[0] = -num2[0] if sign == '-' else num2[0]
#         res1 = [num1[0] * num2[1] + num2[0] * num1[1], num1[1] * num2[1]]
#     return res1
#
# def eval_fraction(expr):
#     tr_num = re.findall(r'-?\d+? ?\d+/\d+|-?\d+/\d+|-?\d', expr)
#     tr_sign = [i.strip() for i in re.findall(' [-+] ', expr)]
#
#     res = tr_num[0]
#     test_res = []
#
#     for i in range(len(tr_sign)):
#         res = sum_param(res, tr_num[i + 1], tr_sign[i])
#         test_res.append(res)
#     res = optim_num(res)
#     return f'{expr} = {res[0]} {res[1]}/{res[2]}'
#
# for i in [str1, str2, str3]:
#     print(eval_fraction(i))

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

import os

path_workers = os.path.join(os.getcwd(), 'data/workers')
path_hours = os.path.join(os.getcwd(), 'data/hours_of')

# data_workers = []

with open(path_workers, 'r', encoding='utf-8') as f:
    data_workers = [i.split() for i in f.read().splitlines()]

with open(path_hours, 'r', encoding='utf-8') as f:
    data_hours = [i.split() for i in f.read().splitlines()]


for i in data_workers:
    match_worker = i[0] + i[1]
    if match_worker == 'ИмяФамилия':
        i.append('Стоимость_часа')
        i.append(data_hours[0][2])
        i.append('Расх_с_нормой_чсов')
        i.append('Коррект_зп')
        i.append('К_выплате')
    else:
        i.append(round(float(i[2]) / float(i[4]), 2))                # Стоимость_часа
        for j in data_hours:
            match_hours = j[0] + j[1]
            if match_worker == match_hours:
                i.append(int(j[2]))                                  # Отработано часов
                i.append(int(i[6]) - int(i[4]))                      # Расх_с_нормой_чсов
                i.append(round(i[7] * i[5] * 2, 2)) if i[7] >=0 \
                         else i.append(round(i[7] * i[5], 2))        # Коррект_зп
                i.append(float(i[2]) + i[8])                         # К_выплате

    print(f'{i[0]} {i[1]}{" " * 10}{i[9]}')


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
