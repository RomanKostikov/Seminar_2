# Реализуйте алгоритм перемешивания списка.
"""Doc."""
import random
import os
os.system('cls')


def lst(n):  # функция рандомного заполнения списка
    lst = []
    for _ in range(n):
        lst.append(random.randrange(-n, n))
    return lst


n = int(input('Enter the number of items: '))
numbers = lst(n)
print(numbers)
# перемешивание списка
for i in range(len(numbers)):
    random_num = random.randint(i, n-1)
    temp = numbers[i]
    numbers[i] = numbers[random_num]
    numbers[random_num] = temp

print(numbers)
