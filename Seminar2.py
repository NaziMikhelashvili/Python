# Задача 9
# по заданному целому неотрицательному значению n вычислите n! (факториал) - произведение числе от 1 до n
# решить задачу используя цикл while

n = int (input('введите целое неотрицательное число: '))
i=1
f=1
while i<=n:
    f = i*f
    i += 1
print(f)

# Задача 11
# дано наутарльное число A>1. Опреднелите каким по счету числом фибоначи оно является то есть 
# найдите такое чиcло n что F(n)=A. Если A не является чиcлом фибоначи выведите число - 1
# фибонначи - число равно сумме двух предыдущих чисел

a = int (input('введите натуральное число: '))
fib = 0
n1 = 1
n2 = 1
count = 2 # так как первые числа уже известны
while fib <= a:
    fib = n1+n2 # сложили 2 посл числа 
    n1=n2 # поменяли предпоследнее число
    n2=fib # поменяли последнее число
    # # можно также написать
    # n1, n2 = n2, fib
    count +=1
    if n1 > a:
        count = 0
if count != 0:
    print(count)
else:
    print (-1)

# Задача 13 - жители пытаются оценить оттепель (период когда средняя температура ежедневно превышала 0 градусов)
# пользователь вводит число N - общее количество рассматриваемых дней от 1 до 100. 
# в следующих строках располагается N целых чисел с температурами от -50 до 50 градусов
# Input 6-> -20 30;-40;50;10;-10
# Output 2
N = int (input('введите количество рассматриваемых дней от 1 до 100: '))
count = 0
max = 0
for i in range (N):
    temp = (int(input('введите температуру: ')))
    if temp >0:
        count += 1
    else:
        max = count
        count = 0
    if (count > max):
        max = count
print(max)


# Задача 15 - Иван Васильевич выбирает 2 образца арбуза - нужен самый легки и самый тяжелый
# Пользователь вводит  N - количество арбузов
# Вторая строчка - N целых чисел с массами арбузов
# Input 5 -> 5 1 6 5 9 
# Output 1 9

w = int (input('введите количество арбузов: '))
for i in range (w):
    a = (int(input('введите массу арбузов: ')))
    if i == 0:
        max = a
        min = a
    elif a > max:
        max = a
    elif a < min:
        min = a
print(min)
print(max)