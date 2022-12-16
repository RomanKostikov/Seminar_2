# 3. Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.
"""Doc."""
import os
os.system('cls')
# first decision(find letters)
# str1 = "understand"
# str2 = str1.count('d')
# print("Count of d in understand is: "
#       + str(str2))

# second decision(group)(find word)
str_1 = input()
str_2 = input()

in_num = str_1.count(str_2)

print(in_num)
