# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов 
# нужно ввести с клавиатуры. Формула для получения n-го 
# члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки

a = int(input('Введите первый элемент прогрессии: '))
n = int(input('Введите количество элементов массива: '))
d = int(input('Введите разность: '))
list1 = []

for i in range(n):
    list1.append(a+i*d)

print(list1)