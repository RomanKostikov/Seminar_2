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


# !!ВТОРОЙ ВАРИАНТ РЕШЕНИЯ!!(С ИСКЛЮЧЕНИЯМИ)
# def get_list(num_f):  # Функция заполнения списка
#     my_list_f = []
#     for i in range(num_f):
#         my_list_f.append(random.randint(-num_f, num_f))
#     return my_list_f


# flag = True  # Ввод числа N от пользователя и проверка на корректность
# while flag:
#     num = input('Введите число N>6: ')
#     if num.isdigit() and int(num) > 6:
#         num = int(num)
#         flag = False
#     else:
#         print('Введено не корректное значение ! Попробуйте еще раз!')

# my_list = get_list(num)
# print(my_list)
# # Работа с файлом проверка с исключением (открытие, присваивание переменным
# значений хранящихся в файле, закрытие файла)
# try:
#     file = open('file.txt', 'r')
#     first_index = int(file.readline())
#     second_index = int(file.readline())
#     third_index = int(file.readline())
#     four_index = int(file.readline())
#     file.close()
# except FileNotFoundError:
#     print('Файл не найден!')
#     exit()  # В случае обнаружения исключения прерываем выполнение программы

# # Перемножение данных хранящихся в листе согласно полученным индексам
# product_1 = my_list[first_index] * my_list[second_index]
# product_2 = my_list[third_index] * my_list[four_index]

# print(f'first_index - {first_index}, second_index - {second_index},'
#       f' third_index - {third_index}, four_index - {four_index}')
# print(f'{my_list[first_index]}*{my_list[second_index]} = {product_1}')
# print(f'{my_list[third_index]}*{my_list[four_index]} = {product_2}')
