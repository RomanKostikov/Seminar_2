# Напишите программу, которая принимает на вход вещественное
# число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
"""Doc."""
import os
os.system('cls')

num1 = float(input('Enter a real number: '))


def Sum(num1):    # функция нахождения суммы цифр числа(через перевод в str ТД)
    if num1 < 0:
        num1 *= -1
    num2 = 0

    for i in str(num1):
        if i != '.':
            num2 += int(i)

    return num2


print(f'Sum of digits: {Sum(num1)}')
