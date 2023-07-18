# : Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input('Введите число: '))
number = 1
stepen = 1
while number < n:
     print(number)
     number = 2 ** stepen
     stepen += 1
     

