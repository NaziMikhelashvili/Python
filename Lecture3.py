# ФУНКЦИИ, РЕКУРСИИ, АЛГОРИТМЫ
# Функция - фрагмент программы используемый многократно 
# обозначение функции в питоне def

def sum_numbers(n):
    sum = 0
    for i in range(1, n+1):
        sum +=i
    print(sum)

sum_numbers(5)

# вместо print можно использовать return чтобы программа заевршила работу
def sum_numbers1(n):
    sum1 = 0
    for i in range(1, n+1):
        sum1 +=i
    return sum1
    print('stop')

print(sum_numbers1(6))

# правило работы с функциями - сколько аргументов принимаем, столько и передаем и наоборот
# примеры ошибок 
# def sum_numbers(n, y):
# sum_numbers(5)

# или 
# def sum_numbers(n):
# sum_numbers(5, 'hgh')


# МОДУЛЬ - множество функций
 
# часто заводятся отдельно в рабочих файлах и затем импортируются
 
import modul1
print(modul1.max(5,9))

# другой способ импорировать функцию: 
from modul1 import max
print(max(10,9))

# если хотим импортировать функцию напрямую но не знаем название или не хотим перечислять
from modul1 import * # чтоб импортировались все функции

# чтобы было удобнее работать с модулями можно менять их названия на время работы программы:
import modul1 as m1
print(m1.max(12,9))


# РЕКУРСИИ - функкция, вызывающая сама себя
# всегда нужно указывать базис - место, где функция прекратит работу

# пример - вводится число n - нужно вывести n-первых чисел последовательности фибоначи 
# (где каждое число равно сумме 2 предыдущих)

def fib(n):
    if n in [1,2]: #базис рекурсии - если его не указать то вылезет ошибка что вылезли за предел дапазона
        return 1
    return fib(n-1)+fib(n-2)

list_1 = []
for i in range(1,10):
    list_1.append(fib(i))
print(list_1)


# АЛГОРИТМЫ - набор инструкция для задачи 
# 2 алгоритма сортировок:
# 1) быстрая сортировка - за счет разбиения большого на маленькое

# пример - 1 человек загадывает числа от 1 до 1000 - второй угадывает
# можно сортировать диапазоны в которых лежат числа (>50, <100 и тд пока не выйдем на конкретное число)

def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i<= pivot]
    more = [i for i in array[1:] if i > pivot]
    return quick_sort(less)+[pivot]+quick_sort(more)
print(quick_sort([14, 5, 9, 6, 4, 89]))



# 2) сортировка слиянием - через деление на 2 и упорядочивание 

def merge_sort(nums):
    if len(nums) >1:
        mid = len(nums) //2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i=j=k=0
        while i< len(left) and j <len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i+=1
            else:
                nums[k]=right[j]
                j+=1
            k+=1

        while i< len(left):
            nums[k] = left[i]
            i+=1
            k+=1

        while j< len(right):
            nums[k] = right[j]
            j+=1
            k+=1

list1 = [1, 5, 8, 9, 5]
merge_sort(list1)
print(list1)