# Задача 1
print('Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.')

number = int(input('Введите число от 1 до 7\n'))

if 0 < number < 8:
    if number == 6 or number == 7:
        print('Да')
    else:
        print('Нет')
else:
    print('Некорректный ввод!')

# Задача 2  
print('Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.')

for i in [True, False]:
    for j in [True, False]:
        for k in [True, False]:
            print((not (i or j or k)) == ((not i) and (not j) and (not k)))

# Задача 3
print('Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,\nв которой находится эта точка (или на какой оси она находится).')

coordinate_x = int(input('Введите значение точки x\n'))
coordinate_y = int(input('Введите значение точки y\n'))

if coordinate_x != 0 and coordinate_y != 0:
    if coordinate_x > 0 and coordinate_y > 0:
        print('1 четверть')
    elif coordinate_x < 0 and coordinate_y > 0:
        print('2 четверть')
    elif coordinate_x < 0 and coordinate_y < 0:
        print('3 четверть')
    else:
        print('4 четверть')
else:
    print('Некорректный ввод!')
    
# Задача 4
print('Напишите программу, которая по заданному номеру четверти,\nпоказывает диапазон возможных координат точек в этой четверти (x и y)')

quarter_num = int(input('Введите номер четверти\n'))

if 0 < quarter_num < 5:
    if quarter_num == 1:
        print('x > 0 и y > 0')
    elif quarter_num == 2:
        print('x < 0 и y > 0')
    elif quarter_num == 3:
        print('x < 0 и y < 0')
    else:
        print('x > 0 и y < 0')
else:
    print('Некорректный ввод!')

# Задача 5
print('Напишите программу, которая принимает на вход координаты двух точек\nи находит расстояние между ними в 2D пространстве')

cnt = 0
array_coordinate = []
while cnt < 4:
    if cnt < 2:
        coordinate_a = int(input('Введите координаты первой точки X и Y\n'))
        array_coordinate.append(coordinate_a)
    else:
        coordinate_b = int(input('Введите координаты второй точки X и Y\n'))
        array_coordinate.append(coordinate_b)
    cnt += 1

result = ((array_coordinate[2] - array_coordinate[0]) ** 2 + (array_coordinate[3] - array_coordinate[1]) ** 2) ** 0.5
print(round(result, 3))


