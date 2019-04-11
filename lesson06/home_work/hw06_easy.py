# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

from math import sqrt

class Triangle:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def f_square(self):
        return abs((self.A[0] - self.C[0]) * (self.B[1] - self.C[1])
                   - (self.A[1] - self.C[1]) * (self.B[0] - self.C[0])) / 2

    def f_high(self):
        def any_high(A, B, C):
            return (abs((B[1] - C[1]) * A[0] +
                       (C[0] - B[0]) * A[1] +
                       (B[0] * C[1] - C[0] * B[1])) /
                    sqrt((B[1] - C[1]) ** 2 + (C[0] - B[0]) **2))
        dict_high = {'High_A': any_high(self.A, self.B, self.C),
                     'High_B': any_high(self.B, self.C, self.A),
                     'High_C': any_high(self.C, self.B, self.A)}
        return dict_high

    def f_perimeter(self):
        def any_side(A, B):
            return sqrt((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2)
        return (any_side(self.A, self.B) +
                any_side(self.B, self.C) +
                any_side(self.A, self.C))


tr = Triangle((1, 3), (3, 2), (-1, 0))

print(f'Площадь треугольника: {tr.f_square()}\n'
      f'Высоты треугольника: {tr.f_high()}\n'
      f'Периметр треугольника: {tr.f_perimeter()}\n')


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze():
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D


    @staticmethod
    def __any_side(A, B):
        return sqrt((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2)


    def check_figure(self):
        d1 = self.__any_side(self.A, self.B)      # sqrt((self.A[0] - self.C[0]) ** 2 + (self.A[1] - self.C[1]) ** 2)
        d2 = self.__any_side(self.C, self.D)      # sqrt((self.B[0] - self.D[0]) ** 2 + (self.B[1] - self.D[1]) ** 2)
        return 'Это равнобедренная трапеция' if d1 == d2 else 'Другая фтгура'

    def f_side_len(self):
        dict_length = {'AB': self.__any_side(self.A, self.B),
                       'BC': self.__any_side(self.B, self.C),
                       'CD': self.__any_side(self.C, self.D),
                       'DA': self.__any_side(self.D, self.A)}
        return dict_length

    def f_perimeter(self):
        return (self.__any_side(self.A, self.B) +
                self.__any_side(self.B, self.C) +
                self.__any_side(self.C, self.D) +
                self.__any_side(self.D, self.A))

    def f_square(self):
        sides = self.f_side_len()
        h = sqrt(sides['AB'] ** 2 -
                    (((sides['DA'] - sides['BC']) ** 2 + sides['AB'] ** 2 - sides['CD'] ** 2) /
                    2 * (sides['DA'] - sides['BC'])) ** 2)
        return (sides['BC'] + sides['DA']) * h / 2


trap = Trapeze((2, 1), (3, 3), (6, 3), (7, 1))

print(f'Это трапеция ? {trap.check_figure()}\n'
      f'Длины сторон: {trap.f_side_len()}\n'
      f'Периметр: {tr.f_perimeter()}\n'
      f'Площадь: {tr.f_square()}')
