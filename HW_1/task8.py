#Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать 
#один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
#*Пример:*
#3 2 4 -> yes
#3 2 1 -> no

print ('Введите размер шоколадки n')
n = int(input())
print ('Введите размер шоколадки m')
m = int(input())
print ('Введите размер долек k')
k = int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')