# Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного 
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

# Диапазон от 6 до 12

# Вывод: [1, 9, 13, 14, 19]

from random import randint

min = int(input('Введите минимум: '))
max = int(input('Введите максимум: '))
list1 = [randint(-100,100) for i in range(30)]
list2 =[]
print(list1)
for i in range(len(list1)):
    if list1[i]>=min and list1[i]<=max: list2.append(i)
print(list2)