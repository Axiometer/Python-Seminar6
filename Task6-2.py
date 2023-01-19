# Измененная Task1-5.py
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве
from functools import reduce
from random import randint

A = [randint(-10, 11) for i in range(2)]
B = [randint(-10, 11) for i in range(2)]
print("Координаты A:", A)
print("Координаты B:", B)

AB = sum([reduce(lambda x, y: x-y, point)**2 for point in zip(A, B)])**0.5

print(f"Расстояние AB (с точностью до 4 знаков после запятой) =", "%.4f" % AB)