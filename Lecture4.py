# ФУНКЦИИ ВЫСШЕГО ПОРЯДКА И РАБОТА С ФАЙЛАМИ
# пример простой функции:
def f(x):
    return x*x
print(f(5))
print(type(f))

a=f
# a- переменная которая хранит в себе ссылку на функцию f
print(a(6))
print(type(a))

def calc1(s):
    return s+s
def calc2(s):
    return s*s
def math(op, x):
    print(op(x))
#можно делать фцнкции с отсылками на другие функции или друг на друга
math(calc1, 5)
math(calc2, 5)

def calc3(b,c):
    return b+c
def calc4(b,c):
    return b*c
def math2(op, x, y):
    print(op(x, y))

math2 (calc3, 5, 2)
math2 (calc4, 5,2)

#написание функции можно укорачивать с помощью лямбда функции: 
calc5 = lambda b,c: b+c
math2(calc5, 5,2)

#или еще короче:
math2( lambda b,c: b+c, 5,2)


#Задача - в списке чисел нужно выбрать только четные числа и составить список пар(число;квадрат числа)

# Пример: 1 2 3 5 8 15 23 38
# Результат: [(2.4), (8,64), (38, 1444)]

data = [1,2,3,5,8,15,23,38]
res = list()

for i in data:
    if i%2==0:
        res.append((i, i**2))

print(res)

# решение через лямбда-функцию 

def select(f, col):
    return[f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = [1,2,3,5,8,15,23,38]
res = select(int, data)
print(res)
res = where(lambda x: x%2 ==0, res)
print(res)
res = list(select(lambda x: (x, x**2), res))
print(res)

# решение через map и filter
data = [1,2,3,5,8,15,23,38]
res = map(int, data)
res = filter(lambda x: x%2 ==0, res)
res = list(map(lambda x: (x, x**2), res))
print(res)


# Функция MAP - применяет на вход 2 аргумента - функцию и сам объект и  возвращает сам объект
list1 = [x for x in range(1,20)]
print(list1)

list1=list(map(lambda x:x+10, list1))
print(list1)

# задача - с клавиатуры вводится набор чисел через пробел - он считывается в качестве строки 
# - надо преобразовать list строк в list чисел

# .split() - функция которая преобразовывает строки в числа

data = '1 2 3 4 5 6 7 5 4 3 2 1'
print(data)
# data = data.split()
# print(data)

data = list(map(int, data.split()))
print(data)


# функция filter - содержит функцию и объект и 
# возвращает только те значения объекта по которым функция вернула значение TRUE

data = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
res=list(filter(lambda x: x%10==5, data)) #только те значения которые заканчиваются на 5
print(res)


# функция zip() применяется к набору итерируемых объектов и возвращает
# # итератор с кортежами из элемнтов входных данных
# zip ([1,2,3], ['o','d','t'], ['о','д','т'])
# # результат  - первый элемент из первого списка, второго и третьего и тд
# [1,'o','о'], [2,'d','д'], [3,'t','т']

# Пример
users =['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4,5,9,14,17]
data=list(zip(users, ids))
print(data)
#функция пробегает по минимальному входящему набору
salary =[111,222,333]
data = list(zip(users, ids, salary))
print(data)



# функция enumerate() применяется к итерируемому объекту и возвращает
# новый итератор с кортежами из индекса и элементов входных данных
# enumerate (['Казань', 'Смоленск', 'Рыбки'])
# # результат  - функция позволяет пронумеровать набор данных
# [(0, 'Казань'),(1,'Смоленск'),(2,'Рыбки')]

# Пример
users =['user1', 'user2', 'user3', 'user4', 'user5']
data=list(enumerate(users))
print(data)






# ФАЙЛЫ
# Для работы с файлом нужно
# 1) завести переменную связанную с текстовым файлом
# 2)указать путь к файлу
# 3) указать режим работы с файлом

# # Режимы работы с файлом: 
# a - append - открытие для добавления данных: 
# позволяет дописывать что-то в имеющийся файл 
# если попытка работы с несуществующим файлом, файл будет созадан и в него занесется запись

# r - read - открытие для чтения данных 
# позволяет читать данные из файла
# еслии попробовать считать данные из несуществующего файла программа выдаст ошибку 

# w - write - открытие для записи
# позволяет записывать данные и создавать файл если его не существует 

# W+ - позволяет открывать файл для записи и читать из него
# если файл не существует, то он будет создан 

# r+ - позволяет открывать файл для чтения и дописывать в него
# если файл не существует,программа выдаст ошибку 

# пример работы с режимом append
# файл открывается - в него вносятся изменения - файл закрывается

colors = ['red', '8898', 'blue']
data = open('file.txt', 'a')# здесуь указываем режим - так как a - файл создастся
data.writelines(colors) #разделителей не будет
data.close()


# чтобы не открывать и закрывать постоянно файл: 
# пример работы с режимом write
with open('file.txt', 'w') as data: #перезатирает данные каждый раз 
    data.write('line 1\n')
    data.write('line 2\n')    
print (56)


# пример работы с режимом read
path='file.txt'
data=open('file.txt', 'r')
for line in data:
    print(line)
data.close()


# БИБЛИОТЕКИ ДЛЯ РАБОТЫ С ОПЕРАЦИОННЫМИ СИСТЕМАМИ
# Модуль os
# чтобы начать работу нужно его импортировать
import os
# os.chdir(path)- смена текущей директории
# os.getcwd()- текущая рабочая директория 
os.chdir('c:/Users/Инга/GeekBrains/Python')
print(os.getcwd())
# os.path - вложенный модуль реализует несколько функций:
# os.path.basename(path) - базовое имя пути
# os.path.abspath - возвращает нормализованный обсолютный путь 
print(os.path.basename('c:/Users/Инга/GeekBrains/Python/backup.py'))
print(os.path.abspath('backup.py'))


# Модуль shutil - содержит набор функций для рботы с файлами и папками
# чтобы начать работу нужно его импортировать
# import shutil
# shutil.copyfile(src, dst) - копирует содержимое источника src(source) в назначаемый файл dst(destination)
# shutil.copy(src, dst) - копирует содержимое источника src(source) в  файл или папку dst(destination)
# shutil.rmtree(path) -удаляет текущую директорию и все поддиректории path должен указывать на директорию а не ссылку

