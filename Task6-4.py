# Переделанная Task3-2.py
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# импорт модуля рандомизатора
from random import randint

# функция герерирования случайного списка из n элементов в диапазоне от -10 до 10
def generate_list(n):
    generated_list = [randint(-10,11) for i in range(n)]
    return generated_list

def mult_list(num_list):
    return [num_list[i] * num_list[-i-1] for i in range(len(num_list)//2 + len(num_list)%2)]

# определяем количество элементов списка
k = 7
# генерируем список случайных чисел
my_list = generate_list(k)
# вывод исходного списка
print("Исходный список:", my_list)

# вывод результата
print("Получаемый результат:", mult_list(my_list))