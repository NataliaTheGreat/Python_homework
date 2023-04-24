#Задача 2: Найдите сумму цифр трехзначного числа. 
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0)

print ('Введите трехзначное число')
number=int(input())
sum = 0
while number > 0:
    digit = number % 10
    sum += digit
    number //= 10
print("Сумма цифр числа:", sum)