# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

import random

list_1 = [random.randint(-10,10) for i in range(20)]
print(list_1)

max_digit = int(input('Введите максимум диапазона: '))
min_digit = int(input('Введите минимум диапазона: '))

list_2 = []

for i in range(len(list_1)):
    if list_1[i] > min_digit and list_1[i] < max_digit:
        list_2.append(i)
print(list_2)