# ПОВТОРЕНИЕ СПИСКОВ

# задача 39 - даны 2 списка - нужно вывести те элементы 1 списка которых нет во втором списке.
# пользователь вводит N число элементов 1 списка, N чисел - элементы списка, M - число элементов 2 списка и элементы

import random
def list_creation(num):
    list=[]
    for i in range (0, num):
        list.append(random.randint(1,100))
    return list

N = int(input('введите число элементов 1 списка:'))
M = int(input('введите число элементов 2 списка:'))
N_list = list_creation(N)
M_list = list_creation(M)
print (N_list)
print (M_list)
new_list = []
for num in N_list:
    if num not in M_list:
        new_list.append(num)
print(new_list)


# генератор списков 
# 1 способ
nums = []
for i in range(5):
    n = int(input('введите число: '))
    nums.append(n)
# 2 способ
nums = []
for i in range(5):
    nums.append(int(input('введите число: ')))
# 3 способ
nums = [int(input('введите число: ')) for i in range(5)]
print(nums)
# 4 способ
def create_arr(length):
    nums = [int(input('введите число: ')) for i in range(length)]
    print(nums)

create_arr(int(input('введите длину массива: ')))

# задача 41 - дан список - нужно определить количество элементов у которых 2 соседних элемента меньше данного.
# вводится число N элементов и сами элементы 

import random
def list_creation(num):
    list=[]
    for i in range (0, num):
        list.append(random.randint(1,100))
    return list

N = int(input('введите число элементов списка:'))
N_list = list_creation(N)
print(N_list)
i=1
count = 0
while i < len(N_list):
    left = N_list[i-1]
    mid = N_list[i]
    right = N_list[i-len(N_list)+1]
    if left<mid and right< mid:
        count +=1
    i +=1
print (count)

# задача 43  - дан список чисел - нужно посчитать сколько в нем пар элементов равных друг другу 
# без рекурсии: 
def count(arr):
    count = 0
    for i in range (len(arr)):
        for j in range (i+1, len(arr)):
            if arr[i]==arr[j]:
                count +=1
    return count
# c рекурсией: 
def recursive (numbers):
    if len(numbers)<=1:
        return 0
    first_num=numbers[0]
    rest_nums = numbers[1:]
    count = 0
    for i in rest_nums:
        if first_num == i:
            count +=1
    return count + recursive(rest_nums)
    
arr = [8, 4, 2, 5, 9, 2, 6, 4, 8, 3]
print(count(arr))
print(recursive(arr))


# задача 45 - 2 числа n и m называются дружественными если и сумма делителей включая 1 но исключая само число 
# равна самому числу. по данному числу k выведите все пары дружественных чисел не больше k
# каждая пара должна быть выведена только 1 раз (перестановка чисел не создает новую пару)

num = 10000

def friendlyNumber(num):
    res=0
    for div in range(1, int(num/2+1)):
        if num%div==0:
            res+=div
    return res

for i in range (2, num):
    m=friendlyNumber(i)
    n=friendlyNumber(m)
    if n==i and n <m:
        print(n,' ',m)
