# Задайте список из n чисел последовательности (1+1/n)**n
# и выведите на экран их сумму.
# Пример:
# - Для n = 6: [2.0, 2.25, 2.37, 2.44, 2.49, 2.52] => 14.07
"""Doc."""
import os
os.system('cls')

n = int(input('Return number: '))

lst = [round((1+1/i)**i, 2) for i in range(1, n+1)]
print(f'Sequence: {lst}\nSum: {round(sum(lst), 2)}')
