# 1 вопрос - как написать этот код с помощью генератора списка

import random
numbers = []
for i in range(5):
    numbers. append(random.randint(1,100))
print(numbers)
# Ответ:
import random
numbers=[random.randint(1,100) for i in range(5)]
print(numbers)

# 2 вопрос - как написать эту функцию в лямбда-виде
def is_odd(number:int):
    if number%2==1:
        return False
    return True
# Ответ:
is_odd = lambda number: False if number%2 else True

# 3 вопрос - как с помощью этой функции отфильтровать список 
import random
numbers=[random.randint(1,100) for i in range(5)]
print(numbers)
is_odd = lambda number: False if number%2 else True
# Ответ:
numbers = list(filter(is_odd, numbers))
print(numbers)


# 4 вопрос - что делает со списком ['a', 'b'] функция enumerate
data = ['a', 'b'] 
# Ответ:
data = list(enumerate(data))
print(data)
# [(0, 'a'), (1, 'b')]


# 5 вопрос - сложить элементы двух списков в порядке следования их индексов
numbers =[2,4,6,8,10,12]
carbons = [58,46,34,22,10,8]
# Ответ:
union =[]
for num1, num2 in zip(numbers, carbons):
    union.append(num1+num2)
print(union)


# 6 вопрос - получить из списка чисел список их факториалов 
from math import factorial
numbers =[1,2,3,4,5,6,7,8,9,10]

# Ответ:
fact =[]
for num in numbers:
    fact.append(factorial(num))
print(fact)
# решение через Map
factorials=list(map(factorial, numbers))
print(factorials)





# задача 47 - есть код который нельзя менять 
# переменная transformation = "???"
# values = [2,3,5,7,11,13,17,19,23,29]
# transformed_values=list(map(transformation, values))

# напишите такое лямбда-выражение tranformation чтобы tranformed_values выдавал копию values
# переменная transformation = "???"
# values = [2,3,5,7,11,13,17,19,23,29]
# transformed_values=list(map(transformation, values))


transformation = lambda x: x
values = [1,23,42, 'asdig']
transformed_values=list(map(transformation, values))
if values == transformed_values:
    print('ok')
else:
    print('fail')




# задача 49 - самая дальняя планета с самой большой площадью
# напишите функцию find_farthest_orbit(list_of_orbits) которая из списка планет отберет самую далекую
# круговые орбиты не рассматриваем 
# каждая орбита - кортеж из пары чисел - полуосей эллипса
# площадь эллипса S=pi*a*b где a и b - длины полуосей эллипса
orbits = [(1,3), (2.5, 10), (7,2), (6,6), (4,3)]
from math import pi

def find_farthest_orbit(orbits):
    s=[]
    s_orbits = list(map(lambda i: i[0]*i[1]*pi if i[0]!=i[1] else 0, orbits))
    max_num=max(s_orbits)
    max_index=s_orbits.index(max_num)
    return (orbits[max_index])


print(find_farthest_orbit(orbits))

# альтернативное решение 
from math import pi
def find_farthest_orbit(orb):
    return max(orb, key=lambda x: x[0]*x[1]*pi if x[0]!=x[1] else 0)
print(find_farthest_orbit(orbits))

# задача 51 - 
# напишите функцию same_by(characteristic, object) которая из списка проверяет все ли имею одинаковое значение
# и возвращает True если это так а иначе False


def same_by(characteristic, objects):
    if not objects:
        return True
    characteristic = [characteristic(obj) for obj in objects]
    return len(set(characteristic))==1

values  = [0,2,10,6]

if same_by(lambda x:x%2, values):
    print('same')
else:
    print('different')



