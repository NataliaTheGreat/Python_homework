#Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#*Пример:*

#6 ->  1  4  1
#24 -> 4  16  4
#60 -> 10  40  10

print('Введите количество журавликов, кратное 6')
number = int(input())
if number % 6 != 0:
    print ('Число должно быть кратно 6')
else:
    print("Петя и Сережа сделали по", number // 6, "журавликов")
    print("Катя сделала", number // 6 * 2, "журавликов")
    
    


 