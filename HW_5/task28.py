# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
#     Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#    2 2 4

a = int(input("Введите первое неотрицательное число: "))
b = int(input("Введите второе неотрицательноечисло: "))
def summ(c, d):
    if d == 0:
        return c
    return summ(c + 1, d - 1)
if a < 0 or b < 0:
   print("Числа должны быть неотрицательные. Перезапустите программу")
else:
    print(f"Сумма чисел {summ(a, b)}")