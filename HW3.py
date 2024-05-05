# Задача 16 - нужно посчитать сколько раз встречается число X в массиве A[1..N]
# Пользователь вводит N количество элементов в массиве, затем N целых чисес в массиве и число X 

N = int (input('введите количество элементов в массиве: '))
X = int (input('введите искомое число: '))
count = 0
for i in range (N):
    v = (int(input('введите элемент массива: ')))
    if v == X:
        count +=1
print (count)

# Задача 18 - найти в массиве A[1..N] самый близкий элемент к заданному числу X

N = int (input('введите количество элементов в массиве: '))
x = int (input('введите искомое число: '))
list_1 = range (N)
close = list_1[0]
for i in list_1:
    v = (int(input('введите элемент массива: ')))
    new = v-x
    if new < v-close or new <close-v:
        close = v
print (close)

#альтернативное решение 
list_1 = [1, 2, 3, 4, 5]
k = 6
list_1 = [2, 4, 1, 6, 8, 2, 9, 3, 2, 5]
k = 10
close = list_1[0]
for i in list_1:
    new = i-k
    if abs(new) < k-close or abs(new) <close-k:
        close = i
print (close)

#альтернативное решение
m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number)

# Задача 20 - напишите программу для вычисления стоимости очков в игре скраббл - на вход только 1 слово
# из только английскийх букв и русских букв

# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:

# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# dictionary = {1 : 'AEIOULNSTRАВЕИНОРСТ',2: 'DGДКЛМПУ', 3: 'BCMPБГЁЬЯ', 4: 'FHVWYЙЫ', 5: 'KЖЗХЦЧ',8: 'JXШЭЮ', 10 : 'QZФЩЪ'}
# k = input('введите слово: ')
# word = k.upper()  # переводим все буквы в верхний регистр
# count = 0
# for i in word:
#     for i,j in dictionary.values:
#         count = count + j
# print(count)


points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
k = input('введите слово: ')
word = k.upper()  # переводим все буквы в верхний регистр
count = 0
for i in word:
    if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        for j in points_en:
            if i in points_en[j]:
                count = count + j
    else:
        for j in points_ru:
            if i in points_ru[j]:
                count = count + j
print(count)

#записная книга
contacts = { "мама": 56565, "папа": 45478, "сестра": 89989}
for i in contacts:
    print(i)

for key in contacts.keys():
    print(key)

print(contacts.keys())

for number in contacts.values():
    print(number)

for contact, number in contacts.items():
    print (number, contact)