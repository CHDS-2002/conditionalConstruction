# os - библиотека для работы с консолью

import os

# Зададим цвет шрифта консоли
os.system('COLOR B')


def equal_count(count):
    # Выводим количество равных чисел
    print('\nКоличество равных чисел:', count, end='.\n\n')


first = second = third = ''

# Вводим целые числа

print('\nВВОД ЧИСЕЛ\n')

while not first.isnumeric():
    first = input("Первое число: ")

while not second.isnumeric():
    second = input("Второе число: ")

while not third.isnumeric():
    third = input("Третье число: ")

# Преобразуем str в int
first, second, third = int(first), int(second), int(third)

# Считаем равные числа
count = 0
statement0 = first == second == third
statement1 = (first == second or
              second == third or
              first == third)

if statement0:
    count = 3
elif statement1:
    count = 2

# Выводим количество равных чисел
print('\nИНФОРМАЦИЯ О ЧИСЛАХ')
equal_count(count)

try:
    os.system('PAUSE')  # Останавливаем работу программы
    os.system('CLS')  # Очищаем экран консоли
except:
    os.system('CLS')  # Очищаем экран консоли
