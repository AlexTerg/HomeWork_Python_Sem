from math import prod
import numpy
import random

# Задача 1
print('Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.')
number = float(input('Введите число\n'))
array_number = [int(i) for i in str(number) if i != '.']
print(sum(array_number))

# Задача 2
print('Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.')

number_N = int(input('Введите число\n'))

array_N = [prod(range(1, i + 1)) for i in range(1, number_N + 1)]
print(array_N)

# Задача 3
print('Задайте список из n чисел последовательности (1 + (1 / n)) ** n и выведите на экран их сумму')

number_n = int(input('Введите число\n'))

array_n = [(1 + (1 / i)) ** i for i in range(1, number_n + 1)]

print(sum(array_n))


# Задача 4
print('Задайте список из N элементов, заполненных числами из промежутка [-N, N].\nНайдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.')

num_N = int(input('Введите число N\n'))
random_array = [random.randint(-num_N, num_N) for i in range(num_N)]
new_array = [i for i in numpy.random.randint(-10, 10, 10)]

with open('./file.txt', 'w') as file:
    for i in new_array:
        file.write(str(i) + '\n')
with open('./file.txt', 'r') as file:
    result = 1
    for i in file:
        if -num_N < int(i) < num_N:
            result *= random_array[int(i)]
print(result)

# Задача 5
print('Реализуйте алгоритм перемешивания списка')

my_list = [i for i in range(10)]
for i in my_list:
    rnd_index = random.randint(0, len(my_list) - 1)
    temp = my_list[i]
    my_list[i] = my_list[rnd_index]
    my_list[rnd_index] = temp
print(my_list)


