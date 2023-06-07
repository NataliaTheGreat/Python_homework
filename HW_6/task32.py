# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)


import random
n = int(input('Введите число элементов массива '))
min = int(input('Задайте минимум ' ))
max = int(input('Задайте максимум ' ))
lst = [random.randint(0, 20) for i in range(n)]
print("Наш исходный массив:", lst)

for item in lst:
    if item >= min and item <= max:
        print("Индексы элементов в заданном диапазоне:", lst.index(item), end = ' ')  
      
#print(lst)
#print(new_lst)
#print (min)

