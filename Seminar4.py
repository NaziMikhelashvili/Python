# Задача 25 - программа которая принимает на вход строку и отслеживает сколько раз встречался
# каждый символ и добавляет к ним постфикс _n
# для решени задачи нужно использовать функцию .split()

string = input("введите строку:").split()

result = dict()

for i in string:
    if i in result.keys():
        print(f'{i}_{result[i]}', end=" ")
        result[i]+=1
    else:
        print(i, end = " ")
        result[i]=1

print(result)



# альтернативное решение - через добавление в словарь

string2 = input("введите строку:").split()

result2 = dict()
new_result=""
for i in string2:
    if i in result2.keys():
        new_result+=(f'{i}_{result2[i]}')
        result2[i]+=1
    else:
        new_result+=i
        result2[i]=1
    new_result+=" "
print(new_result)


# альтернативное решение - через список

string3 = input("введите строку:").split()

result3 = dict()
new_result2=[]
for i in string3:
    if i in result3.keys():
        new_result2.append(f'{i}_{result3[i]}')
        result3[i]+=1
    else:
        new_result2.append(i)
        result3[i]=1
print(new_result2)
# чтобы вывести все результаты через пробел строкой а не списком можно воспользоваться функцией join
print(" ".join(new_result2))
# также добавить пробелы перед выводимым значением можно с помощью звездочки в начале выводимого параметра:
print(*new_result2)

# Задача 27 - пользователь вводит строку - словолм считается несколько символов без пробелов подряд 
# нужно определить количество слов в заданном тексте

text = input("введите строку:").lower().split()
text_new = set(text)
print (len(text_new))


# сайт codewars позволяет решать задачи и смотреть на чужие решения чтобы формировать насмотренность
# описание функций - docs.python.org


# Задача 29 - задана последовтельнотсь целых неотрицательных чисел нужно определить значение
# наибольшего элемента последовательности которая завершается первым
# встретившимся нулем

max = 0
num = None
while num !=  0:
    num = int (input('введите число: '))
    if num > max:
        max = num
print (max) 