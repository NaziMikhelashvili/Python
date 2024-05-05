print (5, 8, 6)

#запуск команды:
#либо кнопка play справа в верхней части терминала либо CTRL F5, либо python + название файла
#типы переменных
# int - целые числа
# float - дробные числа
# bool - логический тип данных (true/false)
# str - строка

# чтобы задать переменной значение нужно просто назвать переменную и присвоить ей значение
n = 5
print (n)

# если значение переменной не известно можно присвоить значение None
m = None
print (m)

# также задаются и дробные значения
x = 1.89
print (x)

# строка задается с помощью кавычек - могут быть одинарными и двойными
n = 'fgfh'
n1 = "jghjkjh"
print (n)

# чтобы понять тип переменной можноиспользовать print type
print (type (n))
print (type (m))
print (type (x))

# чтобы кавычка выводилась как часть текста, перед ней нужно поставить слеш\
d = 'ghg\'hjj'
print (d)
# двойные кавычки также можно использовать внутри строки
e = 'ghg"hjhj"hjj'
print (e)

# чтобы закомментировать выражение, надо перед ним постаивть 
# - тогда выражение не будет выводиться при запуске программы

# чтобы закомментировать выражение из нескольких строк, надо перед ним и после него постаивть """
"""
print (type (n))
print (type (m))
print (type (x))
"""

# также чтобы закомментировать выражение из нескольких строк, можно выделить выражение 
# и последовательно нажать CTRL K + CTRL C

#  чтобы убрать комментирование с выражения, можно выделить выражение 
# и последовательно нажать CTRL K + CTRL U

# Интерполяция - это получение сложнйо строки из нексольких простых с помощью шаблонов

a = 5
b = 5.89 
c = 'hello'
# print (a, b, c)
# print (a, '-', b, '-', c)
# шаблон f-строки
print (f"{a}-{b}-{c}")
#еще один шаблон
print ("{} - {} - {}".format(a, b, c))


#приведение типов
# к целым числам
d = 5.89
print (d)
print (type(d))
d = int(d)
print (d)
print (type(d))
# к текстовым данным
d = str(d)
print (d)
print (type(d))
# к ним также можно добавлять и другие текстовые вставки
print (d + "hjh")
# приведение к логическим выражениям
k = 1
print (k)
print (type(k))
k = bool(k)
print(k)
print (type(k))

# изменение типа данных не всегда возможно- так строку текста нельзя перевсти в int


#ввод данных
# input ()
# чтобы сохранить вводимое значение нужно присвоить его какой-то переменной
print ('введите первое число')
# o = input ()
# чтобы впоследствии проводить с переменными операциями данным можно сразу присвоить тип
o = int(input ())
print (o)

#второй способ добавить призыв-сообщение: 
p = int(input ('введите второе число: '))
print (p)

print (o, '+', p, '=', o + p)

# арифметические операции 
# + сложение
# - вычитание
# * умножение
# / деление
# % остаток от деления
# // целочисленное деление
# ** вовзедение в степень

#приоритет по фнкциям - ** -> * -> / -> // -> % -> + -> -

#округление чисел
r = 6.9909
y = 90.8888
print (r*y)
#округление через функцию round
print (round(r*y, 3))

#сокращенные приставления - по аналогии с C# i++
iter = 2
iter +=3 # iter = iter + 3 - применимо для всех арифм операций

# Логические операции
# > Больше
# >= Больше или равно
# < Меньше
# <= Меньше или равно
# == Равно (проверяет равенство чисел)
# != не равно
# not НЕ (отрицание)
# and И (конъюнкция)
# or ИЛИ (дизъюнкция)

a = 1 > 4
print (a)
a1 = 1<4 and 5>2
print (a1)
a2 = 1==2
print (a2)
a3 = 1!=2
print (a3)
a4 = 'qwe'
a5 = 'qwe'
print (a4==a5)
a7 = 1<3<4<5<10
print(a7)

#условия - управляющие конструкции IF, IF-else
# отступы: 
# 1 отступ - кнопка Tab или 4 пробела
    # .
    # .
# if condition
    #...
# else:
    #..

# если проверяются несколько условий то используется elif
# if condition1:
    #...
# elif condition2:
    #...
# elif condition3:
    #...
# else:
    #..

#сложные условия: 
# if condition1 and condition2: - оба условия должны быть верными
    #...
# if condition1 or condition2: - хотя бы одно из условий верно
    #...

user = input ('введите имя: ')
if user == 'Маша':
    print ('ура, Маша')
elif user == 'Марина':
    print ('ура, Марина')
else:
    print ('привет ,', user)

# цикл while - позволяет выполнить блок кода, пока условие является верным
#while condition:
    #...

v = 423
sum = 0
while v > 0:
    v1 = v%10
    sum = sum + v1
    v = v // 10
print (sum)

# цикл while-else - блок else выполняется кода тело цикла перестает работать самостоятельно
#while condition:
    #...
#else:
    #...

i=0
while i<5:
    i = i + 1
else:
    print('все')
print(i)

# несамостоятельное прекращение работы цикла - break
j=0
while j<5:
    if j == 3:
        break
    j = j + 1
else:
    print('все')
print(j)
#метод break лучше не использовать - на смену ему лучше использовать метод flag

s = int(input())
flag = True
z = 2
while flag: # можно также написать flag == True
    if s % z == 0: #если остаток от деления числа s на z равен 0
        flag = False #цикл завершит свою работу
        print(z)
    elif z > s // 2: #делитель превышает заданное число деленное на 2
        print (s)
        flag = False
    z +=1


# цикл For, функция range()
# цикл For используется в основном для перебора значений
#For e in enumeration:
    # ...

for e in 1, -2, 4, 6:
    print(e)

# Range выдает значения из диапазона с шагом 1, начало по умолчанию 0
# r1 = range (5) # будут генерироваться значения от 0 в указанном количестве 0, 1, 2, 3, 4
# r2 = range (2, 5) # будут генерироваться значения от начала диапазона до конца не включая его 2, 3, 4
# r3 = range (-5, 0)
# r4 = range (1, 10, 2) # 3 аргумент обозначает шаг 1, 3, 5, 7, 9
# r5 = range (100, 0, -20) # 100, 80, 60, 40, 20

r1 = range (100, 0, -20) 
for e1 in r1:
    print(e1)

#цикл for можно также использовать для строк
for i1 in "qwerty":
    print(i1)

#сложный цикл for 
line = ""
for i2 in range(5):
    line = ''
    for i3 in range(5):
        line +='*'
    print (line)

# Работа со строками
text = "Ляляля - песенка моя"
# функции
print (len(text)) # len - позволяет узнать размер строки
print ('моя' in text) # функция будет проверять есть ли заданный кусок в тексте - результат True/False
print (text.lower()) # функция переводит все символы в нижний регистр
print (text.upper()) # функция переводит все символы в верхний регистр
print (text.replace('моя', 'МОЯ')) # функция позволяет поменять сочетания символов в строке

# элементы текста также можно выводить по символам


print (text[0]) # первый символ
print (text[len(text)-1]) # последний символ
print (text[-1]) # последний символ
print (text[-5]) # пятый символ с конца
print (text[:]) # все символы
print (text[:2]) # все символы от начала до указанного элемента 2
print (text[2:]) # все символы от указанного элемента 2 до конца
print (text[2:10]) # все символы от указанного элемента 2 до 10 элемента не включая его
print (text[2:10]) # все символы от указанного элемента 2 до 10 элемента не включая его
print (text[2:10:4]) # все символы от указанного элемента 2 до 10 элемента не включая его с шагом 4
text = text[2:4] + text [-9] +text[:6] #компоненты текста можно складывать
print (text)

# множественное описание элементов
a=1
b=2 # =
a, b = 1, 2

a=1
b=1 # =
a=b=1