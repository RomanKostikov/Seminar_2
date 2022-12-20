# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
"""Doc."""
import os
os.system('cls')

# Решение через список
input_num = int(input('Return number N: '))
lst = [1]

for i in range(1, input_num):
    lst.append((i+1) * lst[i-1])

print(lst)

# Решение через переменную
# N = int(input('Return number N: '))

# f = 1
# for i in range(N):
#     i = i + 1
#     f = i * f

#     print(f, end=" ")
