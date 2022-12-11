from math import gcd
# В модуле math есть функция math.gcd(a, b), возвращающая наибольший общий делитель (НОД) двух чисел. Вычислите и напечатайте наибольший общий делитель для списка натуральных чисел. Ввод чисел продолжается до ввода пустой строки.

numbers_lst = []

while True:
    try:
        num = int(input('Введите число. Для завершения, введите пустую строку\n'))
        numbers_lst.append(num)
    except ValueError:
        break

print(gcd(*numbers_lst))

# 2. Орел и решка

text = 'ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР'


def coding(string):
    encoding = ""
    i = 0
    while i < len(string):
        cnt = 1

        while i + 1 < len(string) and string[i] == string[i + 1]:
            cnt += 1
            i += 1

        encoding += str(cnt) + string[i] + ' '
        i += 1
    return encoding


def max_tails_of_coin(lst):
    temp = list(map(lambda x: int(x[:-1]), filter(lambda x: 'Р' in x, lst)))
    return max(temp)


text_coding_lst = coding(text).split()
print(max_tails_of_coin(text_coding_lst))

# 3.Напишите программу для построения горизонтальных столбчатых диаграмм с помощью символа звёздочки.

numbers = input('Enter numbers ').split()


def isdiagram(lst):
    diagram = list(map(lambda x: int(x) * '*', lst))
    return diagram


diagram_lst = isdiagram(numbers)

for i in diagram_lst:
    print(i)
