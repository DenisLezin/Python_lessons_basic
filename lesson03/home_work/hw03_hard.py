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

import re

str1 = '5/6 + 4/7'
str2 = '-2/3 - -2'
str3 = '5 4/6 + -7 4/5 - -4/3 + 8'

def g_delimiter1(n, m):
    nums = [max(n, m), min(n, m)]
    return nums[len(nums) - 1] if nums[len(nums) - 2] % nums[len(nums) - 1] == 0 else \
        g_delimiter1(nums[len(nums) - 1], nums[len(nums) - 2] % nums[len(nums) - 1])


def optim_num(num):
    if len(num) == 1:
        [num.append(0) for _ in range(2)]
    else:
        num.insert(0, 0) if len(num) == 2 else num

        if num[1] % num[2] == 0:
            num[0] += num[1] // num[2]
            num[1] = 0
            num[2] = 0
        else:
            num[0] += abs(num[1]) // abs(num[2])
            if num[1] < 0:
                num[2] = -num[2]
                num[0] = -num[0]
            num[1] = int(num[1] % num[2] / g_delimiter1(abs(num[1]), abs(num[2])))
            num[2] = int(num[2] / g_delimiter1(abs(num[1]), abs(num[2])))
    return num

# def sum_param(param1, param2, sign):
#     param1 = optim_num(list(map(int, re.split(' |/', param1))))
#     param2 = optim_num(list(map(int, re.split(' |/', param2))))
#
#     if param1[2] == 0 or param2[2] == 0:
#         return list(map(sum, zip(param1, param2)))
#
#
#     return param1, param2, sign, res



# pattern = re.compile('[+-]?\d+ \d+/\d+')
tr_num = re.findall('-?\d+? ?\d+/\d+|-?\d+/\d+|-?\d', str3)
tr_sign =[i.strip() for i in re.findall(' [-+] ', str3)]

res = [0, 0, 0]
num = list(map(int, re.split(' |/', tr_num[0])))
num1 = list(map(int, re.split(' |/', tr_num[3])))
num2 = list(map(int, re.split(' |/', tr_num[2])))



'''
    denominator
'''
# if res[2] == 0:
#     res[2] == num[2]
'''
    numerator
'''

'''
   integer
'''

print(tr_num)
print(tr_sign)
print('num    ', num)
print('num_f  ', optim_num(num))
print('num1   ', num1)
print('num1_f ', optim_num(num1))
print('num2   ', num2)
print('num2_f ', optim_num(num2))
# print(sum_param(tr_num[2], tr_num[3], tr_sign[0]))


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


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
