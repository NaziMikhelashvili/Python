# СПИСКИ

# Список - упорядоченный конечный набор элементов (тот же массив с любым типом данных)
list_1 = [] #создание пустого списка
list_1 = list() #создание пустого списка
# вывести список:
print(list_1)
list_1 = [7, 9, 11, 13, 15, 17]
print(list_1)
# чтобы вывести список без квадратных скобок:
print(*list_1)
# нумерация в списках начинается с 0 
# чтобы вывезти размер списка:
print(len(list_1))
# чтобы вывести первый элемент списка 
print(list_1[0])
# чтобы вывести третий элемент списка 
print(list_1[2])
# чтобы вывести последний элемент списка 
print(list_1[-1])
# чтобы вывести предпоследний элемент списка 
print(list_1[-2])

# для работы с элементами списка можно использовать цикл for
for i in list_1:
    print (i)

# чтобы добавить элемент в список
list_1.append(8)
print(list_1)


list=[]
print(list)
for i in range(5):
    list.append(i)
    print(list)

# Функции при работе со списками
# Удаление конкретного элемента из списка

list_2=[12,7,-1,21,0]
list_2.pop() #удаление последнего значения 
print(list_2)
# при этом с помощью данной функции можно и вывести удаляемое значение:
a=list_2.pop()
print(a)
# с помощь функции pop можно также удалить конкретный порядоковый элемент списка 
print(list_2.pop(0))
print(list_2)

# добавление элемента на нужную позицию - функция insert
list_3=[12,7,-1,21,0]
print(list_3.insert(2,21)) #первое значение - это позиция в которую вставляем элемент, второе - значение
print(list_3)

# СРЕЗЫ
list = [1,2,3,4,5,6,7,8,9,10]
print(list[0]) #1
print(list[1]) #2
print(list[-1]) #10
print(list[-5]) #6
print(list[:]) # весь список [1,2,3,4,5,6,7,8,9,10]
print(list[:2]) #до указанного индекса не включая его [1,2]
print(list[-2:]) #с указанного индекса[9,10]
print(list[2:9]) # заданные элементы без последнего индекса [1,2,3,4,5,6,7,8,9]
print(list[0:len(list):6])#с начала до конца с шагом 6 [1, 7] - можно также записать как:
print(list[::6]) #[1, 7]

# КОРТЕЖ - неизменяемый список = занимает мало места (пароли хосты и тд)

t = () #создание пустого кортежа - обозначается круглыми спискмаи в отличие от списка
print(type(t)) #<class 'tuple'>
t = (1, ) #создание непустого кортежа -
print(type(t))
#  в конце должна оставаться запятая
t = (1, 2, 3, ) #создание непустого кортежа -
print(type(t))

# чтобы преобразовать список в кортеж
v = [1,8,9]
print(v)
print(type(v))
v=tuple(v)
print(v)
print(type(v))

# чтобы распаковать кортеж и вывести его элементы
a, b, c = v
print (a,b, c)

# Кортеж - сходство со списком
p = (1,3,5,)
print(p)

#можно также выводить конкретный элемент
print(p[1])

# можно пройтись по элементам кортежа с помощью for
for i in p:
    print (i)
for i in range(len(p)):
    print (p[i])


# Кортеж - отличие от списков -  элементы менять нельзя
t = (1,3,5,)
# t[0]=2
# print(t) - вылезет ошибка 


# СЛОВАРИ - неупорядоченные коллекции произвольных объектов с доступом по ключу
# в списках ключ - индекс элемента, в словарях - значение ключа (строка, число)

d ={} # создание словаря через фигурные скобки
d = dict() 

# Чтобы добавлять значение в словарь нужно указывать ключ 'q' и значение 'qwerty'
d['q']='qwerty'
print(d)
d['w']='werty'
print(d)
print(d['q'])
print(d['w'])

# ПРИМЕР

dictionary = {}
dictionary = {'up': '!', 'left': '-', 'down': 'I', 'right': '+'}
print(dictionary) #{'up': '!', 'left': '-', 'down': 'I', 'right': '+'}
print(dictionary['left']) #-
# типы ключей могут отличаться
dictionary[898]=8989
print(dictionary) #{'up': '!', 'left': '-', 'down': 'I', 'right': '+', 898: 8989}

# при попытке вывести значение, которого нет в словаре вылезет ошибка
# print(dictionary['type']) # KeyError: 'type'

# чтобы удалить элемент -функция DEL
del(dictionary['left'])
print(dictionary) #{'up': '!', 'down': 'I', 'right': '+', 898: 8989}

# для работы с элементами словаря 
print(dictionary.items())
for (k,v) in dictionary.items():
    print(k,v) #k- keys ключи, v- values значение

for item in dictionary:
    print (item) #выведутся только ключи
    print('{}:{}'.format(item, dictionary[item])) #выведутся ключи и значения



# МНОЖЕСТВА - содержат в себе уникальные неповторяющиеся значения не обязательно упорядоченные
# Множество может сожержать значения разных типов
# Создание множества: 
colors = {'red', 'green', 'blue'} #создается с помощью фигурных скобок
print(colors) #{'red', 'green', 'blue'}
# чтобы добавить в множество значение - функция ADD
colors.add('red')
print(colors) #{'red', 'green', 'blue'} - так как значения в множестве не повторяются значение не добавилось
colors.add('gray')
print(colors) #{'blue', 'green', 'gray', 'red'}
# чтобы добавить в множество значение - функция REMOVE
colors.remove('red')
print(colors) #{'gray', 'blue', 'green'}
# # если пытаться удалить несуществующий элемент вылезет ошибка 
# colors.remove('red')
# print(colors) # KeyError: 'red'
# чтобы проверить есть ли значение в множестве можно использовать discard
colors.discard('red')# если значение есть то удалится, если нет то не выведет ошибку
# чтобы удалить все элементы из множества - функция Clear
colors.clear() 
print(colors) #set()

# с помощью функции set можно также задавать свое множество
q = set()

# Операции с множествами

a = {1,2, 3,5,6}
b = {2,5,8,13,21}

c = a.copy() #скопировать множество 
print(c) #{1, 2, 3, 5, 6}
u = a.union(b) #объединить множества
print(u) #{1, 2, 3, 5, 6, 8, 13, 21}
i = a.intersection(b) #пересечение множеств
print(i) #{2, 5}
d1 =a.difference(b) #вычитание множеств
print(d1) #{1, 3, 6}
d2 =b.difference(a) #вычитание множеств
print(d2) #{8, 13, 21}
q =a.union(b).difference(a.intersection(b))
print(q) #{1, 3, 6, 8, 13, 21}

# создание замороженного множества (которое нельзя изменить)
a = {1,8,6}
b=frozenset(a) 


# Генератор списков - list comprehension

# list_1 = [exp for item in iterable] 
# list_2 = [exp for item in iterable if (conditional)]



# Задача - создать список из чисел от 1 до 100

# сначала создать список из чисел
list = []
for i in range(1, 101):
    list.append(i)
print(list)
# эту фнкцию можно записать так:
list = [i for i in range(1,101)]
print(list)

# Задача - создать список из четных чисел от 1 до 100
list = [i for i in range(1,101) if i%2==0]
print(list)
#если мы хотим умножать делить и пр арифм операции
list = [i*2 for i in range(1,101) if i%2==0]
print(list)

#если мы хотим создать пары каждому из чисел (кортежи)
list = [(i,i) for i in range(1,101) if i%2==0]
print(list)


# ПРОФИЛИРОВАНИЕ И ОТЛАДКА

# 1 - синтаксические ошибки SyntaxError
# отсутствие : в функциях if, while for
num1 =5
num2 =7
if num2 > num1:
    print(num2)

# 2 - Indentation error (отсутствие отступов)
else: 
    print(num1)

# 3 - Type error (типовая ошибка) - сложение числа с текстом
# text = 'python'
# s = 5
# print (text + s) #TypeError: can only concatenate str (not "int") to str
    
#4 - ZeroDivisionError (деление на 0)
# num1 =5
# num2 =0
# print(num1/num2) #ZeroDivisionError: division by zero
    
# #5 - KeyError (ошибка ключа) - ключа не существует
# dict = {'q': 'qwerty', 'w': 'werty'}
# print (dict['t']) #KeyError: 't'
    
# # 6 - NameError (ошибка использования перемеенной не существующей)
# name ='Ivan'
# print(names) #NameError: name 'names' is not defined. Did you mean: 'name'?
    
# 7 - ValueError - ошибка значения - текст нельзя преобразовать в число
text = 'Python'
print(int(text)) #ValueError: invalid literal for int() with base 10: 'Python'