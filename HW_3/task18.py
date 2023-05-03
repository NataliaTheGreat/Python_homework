#Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

import random
print('Введите число элментов массива ')
n = int(input())
print('Введите число ')
x = int(input())
lst = [random.randint(0, 20) for i in range(n)]
print("Наш исходный массив:", lst)

#удаляем повторяющиеся элементы из исходного списка
temp = []
for y in lst:
 if y not in temp: 
   temp.append(y)
lst = temp
new_lst = lst.copy()

print("Cамые близкие по величине элементы к заданному числу", x)

for i in range(len(lst)):
   lst[i] = abs(lst[i] - )
min=lst[i]
for i in range(len(lst)):
   if lst[i]<min and lst[i]!=0:
       min = lst[i]
for i in range(len(lst)):
   if lst[i] == min:
      print(new_lst[i],end=' ')
print()  
      
#print(lst)
#print (min)

