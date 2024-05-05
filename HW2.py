# Задача 10 - n монеток (некоторые верх решкой -некоторые гербом)
# найти минимальное число монеток которые надо перевернуть чтобы все были одной стороной

coins1 = int (input('введите 0/1 если 1-монета лежит гербом/решкой вверх: '))
coins2 = int (input('введите 0/1 если 2-монета лежит гербом/решкой вверх: '))
coins3 = int (input('введите 0/1 если 3-монета лежит гербом/решкой вверх: '))
coins4 = int (input('введите 0/1 если 4-монета лежит гербом/решкой вверх: '))
coins5 = int (input('введите 0/1 если 5-монета лежит гербом/решкой вверх: '))

coins = [coins1, coins2, coins3, coins4, coins5]
count1 = 0
count2 = 0
for i in coins:
    if i ==0:
        count1 +=1
    else: 
        count2 +=1
if count1<count2:
    print (count1)
else:
    print(count2)


# Задача 12 - Петя загадывает Кате 2 натуральных числа X и Y (<=1000) и дает 2 подсказки
# называет сумму этих чисел S и произведение P - нужно отгадать числа


s = int (input ('введите сумму чисел X и Y: '))
p = int (input ('введите произведение чисел X и Y: '))

## s = x+y 
# ## p = X*Y
# p = x*(s-x)
# x^2 -s*x-p = 0
d =  s*s-4*p
x = (s + d**0.5)/2
x = int (x)
y = s - x
if x<y:
    print (x, y)
else: 
    print (y, x)


# solutions = []
# for i in range(1, 1001):
#     for j in range(1, 1001):
#         if s == i + j and p == i * j:
#             solutions.append((min(i, j), max(i, j)))
# solutions = list(set(solutions))

# for solution in solutions:
#     print(solution[0], solution[1])
    

# Задача 14 - вывести все целые степени двойки (2^k) не превосходящие числа N
N = int (input ('введите число: '))
k = 1
a = 1
while a<=N:
    print (a)
    a = 2**k
    k +=1
flag = False
