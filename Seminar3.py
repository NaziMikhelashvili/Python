# Задача 17 - дан список чисел - определить сколько в нем разных чисел

list = [1,1,2,0,-1,3,4,4]
set1 = set(list)
print(len(set1))
#альтернативный вариант:
set = set ()
for i in list:
    set.add(i)
print (set)
print(len(set)) 

# Задача 19 - дана последовательность из N целых чисел и число K (целое положительное)
# Необходимо сдвинуть последовательность на К элементов вправо

list = [1,2,3,4,5]
k = 3
shift = list[k:]+list[:k]
print(shift)

#альтернативный вариант
list = [1,2,3,4,5]
k = 3
for i in range(k-1):
    list.insert(0, list.pop())
print (list)

# Задача 21 - напишите программу для печати вех уникальных значений в словаре

dict = [{"V": "S001"},{"V": "S002"},{"VI": "S001"},{"VI": "S005"},{"VII": "S005"},{"V": "S009"},{"VIII": "S007"}]
set = set()
for dictionary in dict:
    for value in dictionary.values():
        set.add(value)
print(set)

# альтернативное решение:
print((list(dictionary.values())[0].strip() for dictionary in dict))

# Задача 23 - дан массив из целых чисел
# посчитать количество эдементов массива больше предыдущего 

input = [0, -1, 5, 2, 3]
count = 0
for i in range(len(input)-1):
    if input[i]<input[i+1]:
        count +=1
print (count)
