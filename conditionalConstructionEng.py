# os - library for working with the console

import os

# Setting the font color of the console
os.system('COLOR B')


def equal_count(count):
    # Output the number of equal numbers
    print('\nThe number of equal numbers:', count, end='.\n\n')


first = second = third = ''

# We enter integers

print('\nENTERING NUMBERS\n')

while not first.isnumeric():
    first = input("The first number: ")

while not second.isnumeric():
    second = input("The second number: ")

while not third.isnumeric():
    third = input("The third number: ")

# Convert str to int
first, second, third = int(first), int(second), int(third)

# Counting equal numbers
count = 0
statement0 = first == second == third
statement1 = (first == second or
              second == third or
              first == third)

if statement0:
    count = 3
elif statement1:
    count = 2

# Output the number of equal numbers
print('\nINFORMATION ABOUT NUMBERS')
equal_count(count)

try:
    os.system('PAUSE')  # Stopping the program
    os.system('CLS')  # Clearing the console screen
except:
    os.system('CLS')  # Clearing the console screen
