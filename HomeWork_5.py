from random import randint
from time import sleep
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = list(filter(lambda x: 'абв' not in x, (input('Введите текст\n').split())))
print(' '.join(text))

# Создайте программу для игры с конфетами человек против человека.
while True:
    try:
        game_mode = int(input('Выберете с кем хотите сыграть:\n1 - человек\n2 - непобедимый bOT\nВведите цифру:\n'))
    except ValueError:
        print('Введите цифру 1 или 2!')
    else:
        break

candies = 300

print(f'На столе {candies} конфет. За один ход можно забрать не более чем 28 конфет')

# Функция игры человека
def game_candies(name, candy):
    while True:
        try:
            player_candies = int(input(f'{name}, сколько конфет вы хотите взять?\n'))
        except ValueError:
            print('Введите число!')
        else:
            break
    if player_candies > 28:
        print('За один ход можно забрать не более чем 28 конфет')
    elif player_candies < 1:
        print('Надо обязательно взять хотя бы одну конфету')
    elif player_candies < 29:
        candy -= player_candies
        if candy < 0:
            candy = 0
            player_candies = "последние конфеты"
        print(f'{name}, взял {player_candies} шт. Осталось {candy}')
        return player_candies

# Функция бота
def is_bot(candys):
    lose_numbers = [i * 29 for i in range(1, candys + 1)]
    for i in range(candys - 29, candys + 1):
        if candys in lose_numbers:
            return randint(1, 29)
        elif i % 29 == 0:
            return candys - i

# Фразы бота
def bot_talk():
    num = randint(1, 6)
    sleep(1)
    if num == 1:
        print('bOT: хм...')
    elif num == 2:
        print('bOT: Проще простого)')
    elif num == 3:
        print('bOT: А ты хорош')
    else:
        return
    sleep(2)
    

# Игра с человеком
if game_mode == 1:
    first_player_name = input("Введите имя первого игрока\t")
    second_player_name = input("Введите имя второго игрока\t")
    lst_players = [first_player_name, second_player_name]
    first_move = randint(0, 2)
    i = first_move
    print(f'{lst_players[i]} ходит первый')
    while candies > 0:
        candy = game_candies(lst_players[i], candies) 
        if candy:
            candies -= candy
            if candies < 1:
                print(f'{lst_players[i]} победил')
            i += 1
        if i >= len(lst_players):
            i = 0
    
# Игра с ботом
if game_mode == 2:
    first_player_name = input("Введите имя первого игрока\t")
    sleep(1)
    print('bOT: Первый ход твой, даю тебе шанс...')
    while candies > 0:
        candy = game_candies(first_player_name, candies) 
        if candy:
            candies -= candy
            if candies < 1:
                print(f'{first_player_name} победил')
                break
            bot_candy = is_bot(candies)
            candies -= bot_candy
            bot_talk()
            print(f'bOT: Я возьму {bot_candy} шт. Осталось {candies}')
            if candies < 1:
                print(f'bOt победил!')


# Крестики нолики

def print_board(array):
    print("\n") 
    print(f" {array[0]} | {array[1]} | {array[2]}") 
    print('-----------') 
    print(f" {array[3]} | {array[4]} | {array[5]}") 
    print('-----------') 
    print(f" {array[6]} | {array[7]} | {array[8]}") 
    print("\n")

board_lst = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def check_win(board):
    win_position = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for i in win_position:
        temp = [k for k in i if k in board]
        if len(temp) == 3:
            return True


first_name = input('Введите имя первого игрока:\t')
second_name = input('Введите имя второго игрока:\t')
players = [first_name, second_name]
first_move = players[randint(0, 1)]
print(f'{first_move} ходит первым')
cnt = 0
first_player_pos = []
second_player_pos = []
temp_board = [i for i in range(1, 10)]
print_board(temp_board)
print('Обратите внимание!!!\nЧто бы поставить Х или O, необходимо указать цифру, которая соответствует ячейке')
while cnt < 9:
    while True:
        try:
            first_player_num = int(input(f'{first_move} Введите позицию '))

            if not 0 < first_player_num < 10:
                print('Введите число от 1 до 9')
                continue

            if ' ' not in board_lst[first_player_num - 1]:
                print('Эта позиция занята')
                continue
        except ValueError:
            print('Введите число от 1 до 9')
        else:
            break

    if len(first_player_pos) > len(second_player_pos):
        board_lst[first_player_num - 1] = 'O'
        second_player_pos.append(first_player_num)
    else:
        board_lst[first_player_num - 1] = 'X'
        first_player_pos.append(first_player_num)

    print_board(board_lst)

    if check_win(first_player_pos):
        print(f'Поздравляю, {first_name} победил')
        exit()
    elif check_win(second_player_pos):
        print(f'Поздравляю, {second_name} победил')
        exit()
    
    if first_move == players[0]:
        first_move = players[1]
    else:
        first_move = players[0]

    cnt += 1

print('Ничья!')

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def coding(string):
    encoding = ""
    i = 0
    while i < len(string):
        cnt = 1
 
        while i + 1 < len(string) and string[i] == string[i + 1]:
            cnt += 1
            i += 1
 
        encoding += str(cnt) + string[i]
        i += 1
    return encoding

with open('./text.txt', 'r', encoding='utf-8') as file:
    text = file.read() 
with open('./coding_text.txt', 'w', encoding='utf-8') as file:
    file.write(coding(text))

    







    
        




