# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

array_numbers = [2, 3, 5, 9, 3, 8, 6]

print(sum(array_numbers[1::2]))
print('')

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

second_index = -1
array_result = []
for i in range(round(len(array_numbers) / 2)):
    array_result.append(array_numbers[i] * array_numbers[second_index])
    second_index -= 1
print(array_result)
print('')

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

array = [1.1, 1.2, 3.1, 5, 10.01]

array_float = [i - int(i) for i in array if type(i) == float]
result = max(array_float) - min(array_float)
print(round(result, 2))
print('')

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

number = 15
result = ''
while number > 0:
    temp = str(number % 2)
    result = temp + result
    number = int(number / 2)
        

print(result)
print('')

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

x = int(input('Введите число\n'))
fib_arr = [0] * (2 * x + 1)
fib_arr[x + 1], fib_arr[x - 1] = 1, 1
k = -1
for i in range(x + 2, 2 * x + 1):
    fib_arr[i] = fib_arr[i - 1] + fib_arr[i - 2]
    fib_arr[-i - 1] = fib_arr[i] * k
    k *= -1
print(fib_arr)



