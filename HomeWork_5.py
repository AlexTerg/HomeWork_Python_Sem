from random import randint
from time import sleep
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# text = list(filter(lambda x: 'абв' not in x, (input('Введите текст\n').split())))
# print(' '.join(text))

# Создайте программу для игры с конфетами человек против человека.
while True:
    try:
        game_mode = int(input('Выберете с кем хотите сыграть:\n1 - человек\n2 - непобедимый bOT\nВведите цифру:\n'))
    except ValueError:
        print('Введите цифру 1 или 2!')
    else:
        break

candies = 100

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
        print(f'{name}, взял {player_candies} шт.\tОсталось {candy}')
        return player_candies

# Функция бота
def is_bot(candys):
    lose_numbers = [i * 29 for i in range(1, candys + 1)]
    for i in range(candys - 29, candys + 1):
        if candys in lose_numbers:
            return randint(1, 29)
        elif i % 29 == 0:
            return candys - i

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
            bot_candy = is_bot(candies)
            candies -= bot_candy
            bot_talk()
            print(f'bOT: Я возьму {bot_candy} шт. Осталось {candies}')
            if candies < 1:
                print(f'bOt победил!')






    
        




