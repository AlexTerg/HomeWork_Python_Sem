from math import pi
from random import randint
from sympy import collect
from os import listdir
# 1.	Вычислить число c заданной точностью d
d = input('Введите число\n').split('.')
print(round(pi, len(d[1])))

print('')
# 2.	Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number_N = int(input('Введите число\n'))

cnt = 2
mylist = []
while cnt < number_N + 1:
    if number_N % cnt == 0:
        mylist.append(cnt)
        number_N = int(number_N) / cnt
    else:
        cnt += 1

print(mylist)
print('')
# 3.	Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
lst = [1, 2, 2, 3, 4]
mylst = [i for i in lst if lst.count(i) == 1]
print(mylst)
print('')
# 4.	Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

k = int(input('Введите число k\n'))

def get_polynomial(k):
    if k == 0:
        return '0 = 0'
    array = [str(randint(0, 100)) for i in range(k + 1)]
    for i, v in enumerate(array):
        if i == len(array) - 2:
            array[i] = v + 'x' 
            break
        else:
            array[i] = v + 'x^' + str(k)
            k -= 1
    return ' + '.join(array) + ' = 0'

for i in range(1,3):
    with open(f'./text_{i}.txt', 'w') as file:
        file.write(get_polynomial(k))

# 5.	Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

polynomial_lst = []
for filename in listdir():
    if 'text_' in filename:
        with open(f'./{filename}', 'r') as data:
            polynomial = data.read()
        polynomial_lst.append(polynomial)

def sum_polynomial(lst):
    temp_lst = []
    for item in lst:
        item_replace = item.replace('x', '*x').replace('^', '**').replace(' = 0', '')
        temp_lst.append(collect(item_replace, 'x'))
        result = sum(temp_lst)
        temp_lst.clear()
        temp_lst.append(result)
    return ''.join(map(str, temp_lst)).replace('**', '^').replace('*x', 'x') + ' = 0'
with open('./sum_polynomial.txt', 'w') as file:
    file.write(sum_polynomial(polynomial_lst))




    
    



