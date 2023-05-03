#Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

import random
n = int(input('Введите число элементов массива '))
x = int(input('Введите число ' ))
lst = [random.randint(0, 20) for i in range(n)]
print("Наш исходный массив:", lst)

#удаляем повторяющиеся элементы из исходного списка
temp = []
for y in lst:
 if y not in temp: 
   temp.append(y)
lst = temp
new_lst = lst.copy()

print("Cамые близкие по величине элементы к заданному числу", x,":")

for i in range(len(lst)):
    lst[i] = abs(lst[i] - x)
min = lst[i]
for item in lst:
    if item < min and item != 0:
        min = item  
for i in range(len(lst)):
    if lst[i] == min:
       print(new_lst[i], end=' ')

print()  
      
#print(lst)
#print(new_lst)
#print (min)

