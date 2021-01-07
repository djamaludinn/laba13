#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#   Выполнить индивидуальное задание 1 лабораторной работы 12, максимально задействовав
#   имеющиеся в Python средства перегрузки операторов.


class Triangle:

    def __init__(self, first=1, second=1, third=1, square=1):
        self.first = float(first)
        self.second = float(second)
        self.third = float(third)
        self.square = float(square)

    # Вывод данных на экран
    def __str__(self):
        return f"{self.first, self.second, self.third, self.square}"

    # Сравнение площадей треугольников
    def __lt__(self, other):
        return self.square < other.square

    def __gt__(self, other):
        return self.square > other.square

    def __le__(self, other):
        return self.square <= other.square

    def __ge__(self, other):
        return self.square >= other.square

    def __eq__(self, other):
        return self.square == other.square

    def __ne__(self, other):
        return self.square != other.square

    # Выполнения арифметических операций над площадями
    def __add__(self, other):
        return self.square + other.square

    def __sub__(self, other):
        if self.square >= other.square:
            return self.square - other.square
        else:
            return ValueError("Отрицательная площадь! -_-")

    def __mul__(self, other):
        return self.square * other.square

    def __truediv__(self, other):
        return self.square / other.square


if __name__ == '__main__':
    r1 = Triangle(first=7, second=12, third=5, square=13)
    print(f"r1 = {r1}")

    r2 = Triangle(first=9, second=6, third=8, square=16)
    print(f"r2 = {r2}")

    print(f"S1 < S2: {r1 < r2}")
    print(f"S1 > S2: {r1 > r2}")
    print(f"S1 <= S2: {r1 <= r2}")
    print(f"S1 >= S2: {r1 >= r2}")
    print(f"S1 = S2: {r1 == r2}")
    print(f"S1 != S2: {r1 != r2}")

    print(f"S1 + S2: {r1 + r2}")
    print(f"S1 - S2: {r1 - r2}")
    print(f"S1 * S2: {r1 * r2}")
    print(f"S1 / S2: {r1 / r2}")