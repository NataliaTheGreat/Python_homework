# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


print('Введите натуральное число N')
number = int(input())
count = 0
stepen=1
print("Все степени двойки, не превосходящие числа", number)
while count <= number:
    stepen *= 2
    print(stepen, end=' ')
    count += 1
