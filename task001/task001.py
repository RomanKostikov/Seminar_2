# 1. Напишите программу, которая принимает на вход число N и выдаёт
# последовательность из N членов.
#     *Пример:*
#     - Для N = 5: 1, -3, 9, -27, 81
"""Doc."""
import os
import random
os.system('cls')
num = int(input('Return number N: '))

for _ in range(num):
    print(random.randrange(-100, 100), end=" ")
