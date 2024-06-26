# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# На вход подается 2 числа через пробел: n m
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо

#решение без множеств
var1 = '5 4' 
var2 = '1 3 5 7 9' 
var3 = '2 3 4 5' 
var1 = [int(num) for num in var1.split()]
var2 = [int(num) for num in var2.split()]
var3 = [int(num) for num in var3.split()]
result=[]
len1, len2 = var1
for i in range(len1):
    for j in range(len2):
        if(var2[i]== var3[j]):
            result.append(var2[i])
    # result.sort()
print(sorted(result))

#решение с множествами
var1 = '5 4' 
var2 = '1 3 5 7 9' 
var3 = '2 3 4 5' 

var2 = set(var2)
var3 = set(var3)
result=var2&var3
print(*sorted(result))

# альтеррнативное решение:
# mol = [int(x) for x in var1.split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in var2.split()]
# k = set(a)
# for i in k:
#    set_1.add(i)
# b = [int(x) for x in var3.split()]
# k1 = set(b)
# for i in k1:
#    set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#    print(i, end=' ')


# В фермерском хозяйстве в Карелии выращивают чернику.
# Черника растет на круглой грядке, и кусты черники высажены по окружности грядки.
# Каждый куст черники имеет урожайность, которая соответствует количеству ягод на этом кусте.
# Урожайность черничных кустов представлена в виде списка arr, где arr[i] - это урожайность 
# (количество ягод) i-го куста.
# В фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Каждый собирающий модуль может собрать ягоды с одного куста и с двух соседних кустов. 
# Собирающий модуль находится перед определенным кустом, и он может выбирать, с какого куста начать сбор ягод.
# Ваша задача - написать программу, которая определит максимальное число ягод, которое может
# собрать один собирающий модуль за один заход, находясь перед некоторым кустом грядки.
# На вход программе подается список arr, где arr[i] (1 ≤ arr[i] ≤ 1000) - урожайность i-го куста черники. 
# Размер списка не превышает 1000 элементов.

arr = [5, 8, 6, 4, 9, 2, 7, 3]
result_count=[]
for i in range(len(arr)-1): #так как последнее число в списке не получится взять
    result_count.append(arr[i]+arr[i+1]+arr[i-1])
result_count.append(arr[0]+arr[-1]+arr[-2])
print(max(result_count))
