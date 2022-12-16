# 2. Для натурального n создать словарь индекс-значение, состоящий из
#  элементов последовательности 3n + 1.
#     *Пример:*
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
"""Doc."""
import os
os.system('cls')
n = int(input('Enter a natural number n: '))
dictionary = {}
for i in range(1, n+1):
    dictionary.update({i: 3*i+1})
print(dictionary)
