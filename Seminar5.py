# ФУНКЦИИ
def invest(rub):
    print(rub)
    return invest(rub+1)
invest(1)


# чтобы задержать время воспроизведения результата можно использовать time.sleep
import time
def invest(rub):
    print(rub)
    time.sleep(0.1)
    return invest(rub+1)
invest(1)

# суть у функции такая же как у цикла описанного ниже
import time
rub = 1 
for i in range(996):
    print(rub)
    time.sleep(0.1)
    rub +=1

# если нужно чтобы было больше 996 элементов можно изменить количество элементов в рекурсии 
import sys
sys.setrecursionlimit(1200)

import time
def invest(rub):
    print(rub)
    time.sleep(0)
    return invest(rub+1)
invest(1)

# если нужно чтобы было больше 996 элементов можно изменить количество элементов в рекурсии 
import sys
sys.setrecursionlimit(1200)

# но при этом СТЕК (количество элементов в памяти) может переполниться не дойдя до предела рекурсии
#  -> поэтому лучше использовать для остановки цикла Retun (аналог break для цикла) - это называется бази рекурсии

def invest(rub):
    print(rub)
    if rub == 100:
        return 100
    return invest(rub+1)+rub
summa = invest(1)
print(summa)


# другой пример с факториалом
def factorial(end):
    print(end)
    if end == 1:
        return 1
    return factorial(end-1)*end
fact = factorial(5)
print(fact)

# задача 31 - последовательность фибоначи:
# a0=0 a1 = 1 ak = ak-1 +ak-2
# найти N-число фибоначи

# 0 1 1 2 3 5 8 13 21 
def fibonaci(N):
    if N <= 1:
        return N
    return fibonaci(N-1)+fibonaci(N-2)
print(fibonaci(7))
# чтобы вывести всю последовательность фибоначи:
for i in range (20):
    print(fibonaci(i), end=" ")


# # задача 33 замените все оценки в школьном журнале с максимальных на минимальные 
# input - 5: 1 3 3 3 4
# output - 1 3 3 3 1


def revers(grades):
    min_grade = min(grades)
    max_grade = max(grades)
    list = []
    for grade in grades:
        if grade == max_grade:
            list.append(min_grade)
        else:
            list.append(grade)
    return list
grades = [1,3,3,3,4]
print(revers(grades))

# # задача 35 напишите функцию которое принимает число и проверяет является ли оно простым 
# input 5 output yes

def prime(N):
    if N <= 1:
        return False
    for i in range(2, N):
        if N % i == 0:
            return "no"
    return "yes"
print(prime(5))

# # задача 37 - дано натуральное число N и последовательность из N элементов
# требуется вывести в обратном порядке без ииспользования массивов и циклов 
# input 3 4 output 4 3 

def rev_list(N):
    num = input('введите число:')
    if N == 1:
        return num
    return rev_list(N-1)+num
print(rev_list(5))

# # пример решения  с рандомным набором 

import random
def rev_list(N):
    num = str(random.randint(1,9))
    print(num)
    if N == 1:
        return num
    return rev_list(N-1)+num
print(rev_list(2))