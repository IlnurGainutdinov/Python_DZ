# : На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

from random import randint

n_count = int(input('Введите количество монеток: '))
count_up = 0
count_down = 0
min_abort = 0
for _ in range(n_count):
    up = randint(0,1)
    print(up, end = ' ')
    if up == 0:
        count_up += 1
    else:
        count_down += 1
if count_up >= count_down:
   min_abort = count_down
else:
    min_abort = count_up  
    
print(f'\n{min_abort}')

