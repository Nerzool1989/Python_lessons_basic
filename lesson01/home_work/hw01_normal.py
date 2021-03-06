
__author__ = 'Канцеров Александр Павлович'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

num = input('Введите число: ')						
						
max_numb = 0						
    for i in num:						
        if int(i) > max_numb:						
        max_numb = int(i)						
print('Самая большая цифра введенного числа:', max_numb)						

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

first = input('Введите первое число ') 				
second = input('Введите второе число ') 				
second, first = first, second 				
print(first, "Теперь это первое число") 				
print(second, "А это второе") 				

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math

print("Программа решения квадратного уравнения вида ax**2 + bx + c = 0")
a = int(input("Введите первый коэф a: "))
b = int(input("Введите второй коэф b: "))
c = input("Введите свободно член c, если имеется: ")
print(type(c))

if c == "":
    c = 0
else:
    c = int(c)
print(type(c))

x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
print('x1 =', x1, '  x2 =', x2)
