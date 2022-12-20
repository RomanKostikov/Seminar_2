# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Позиции хранятся в файле file.txt в одной строке одно число.
"""Doc."""
import random
import os
os.system('cls')


def lst(n):  # функция рандомного заполнения списка
    lst = []
    for _ in range(n):
        lst.append(random.randrange(-n, n))
    return lst


n = int(input('Return number N: '))
numbers = lst(n)
print(numbers)
# Чтение чисел из файла
f = open("file.txt", "r")
a, b = f.read().split("\n")
# Перевод строк в числа, в указатели на индексы
# ("...на указанных позициях(не индексах)")
a, b = int(a)-1, int(b)-1
# перемножение чисел на указанных позициях
result = numbers[a] * numbers[b]
print(result)
