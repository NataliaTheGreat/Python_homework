#Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
#Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

#*Пример:*

#385916 -> yes
#123456 -> no

print ('Введите шестизначное число')
number=int(input())
sum = 0
while number > 1000:
    digit = number % 10
    sum += digit
    number //= 10
sum2 = 0
while number > 0:
    digit = number % 10
    sum2 += digit
    number //= 10
if sum==sum2:
    print ('yes')
else:
    print ('no')   
