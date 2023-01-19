# переделанная задача Task3-1.py
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# импорт модуля рандомизатора
from random import randint

# функция герерирования случайного списка из n элементов в диапазоне от -10 до 10
def generate_list(n):
    generated_list = [randint(-10,10) for i in range(n)]
    return generated_list

# определяем количество элементов списка
k = 6
# генерируем список случайных чисел
my_list = generate_list(k)

# сумма элементов списка, стоящих на нечётной позиции 
summma = sum([num for i, num in enumerate(my_list) if not(i % 2)])

# вывод результата
print("Сгенерирован случайный список: ", my_list)
print("Сумма всех элементов на нечетных позициях: ", summma)