# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    def fib(num):
        return 1 if num == 1 or num == 0 else fib(num -1) + num - 2

    return [fib(i) for i in range(n, m + 1)] if m >= n and n > 0 \
           else '"n" should be greater or equal "m" and "n" should be greater then 0'

print(fibonacci(200, 50))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    n = 1
    while n < len(origin_list):
        for i in range(len(origin_list) - n):
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
        n += 1
    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

func = lambda x: x >= 0

def my_filter(f, lst = [3, 5, -8, -1, 0]):
    return [i for i in lst if f(i)]

print(my_filter(func))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

# Если в четырехугольнике противоположные стороны попарно равны,
# то этот четырехугольник — параллелограмм

import math

A1 = [int(i) for i in input('Input х1 у1: ').split()]
A2 = [int(i) for i in input('Input х2 у2: ').split()]
A3 = [int(i) for i in input('Input х3 у3: ').split()]
A4 = [int(i) for i in input('Input х4 у4: ').split()]

# A1 = [-1, 0]
# A2 = [0, 3]
# A3 = [5, 3]
# A4 = [4, 0]


def is_parallelogram(A1, A2, A3, A4):
    '''
    Проверка; являются ли 4 произволные точки вершинами параллелограмма.
    попарно сравнивает растояние между точками (A1A2 и A3A4)
    для положительного результата достаточно равенства 2х любых независимых отрезков
    :param A1: [x1, y1]
    :param A2: [x2, y2]
    :param A3: [x3, y3]
    :param A4: [x4, y4]
    :return: результат проверки в виде сообщения, str
    '''
    def range_point(a, b):
        '''
        Вычисляет расстояние между 2 точками по координатам
        :param a: [x1, y1]
        :param b: [x2, y2]
        :return: расстояние, float
        '''
        return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    tests = {}
    tests['A1A2VsA3A4'] = range_point(A1, A2) == range_point(A3, A4)
    tests['A1A3VsA2A4'] = range_point(A1, A3) == range_point(A2, A4)
    tests['A1A4VsA2A3'] = range_point(A1, A4) == range_point(A2, A3)
    return "It's Parallelogram!" if list(tests.values()).count(True) == 2 else 'Some other figure :('


res = is_parallelogram(A1, A2, A3, A4)
print(res)

