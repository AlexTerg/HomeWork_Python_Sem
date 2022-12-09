# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# text = list(filter(lambda x: 'абв' not in x, (input('Введите текст\n').split())))
# print(' '.join(text))

# Создайте программу для игры с конфетами человек против человека.
candies = 100
first_player_name = input("Введите имя первого игрока\t")
second_player_name = input("Введите имя второго игрока\t")
lst_players = [first_player_name, second_player_name]
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
        print(f'{name}, взял {player_candies} шт.\tОсталось {candy}')
        return player_candies

i = 0
while candies > 0:
    candy = game_candies(lst_players[i], candies) 
    if candy:
        candies -= candy
        if candies < 1:
            print(f'{lst_players[i]} победил')
        i += 1
    if i >= len(lst_players):
        i = 0



def is_bot(candys):
    for i in range(candys - 29, candys + 1):
        if i % 29 == 0:
            return candys - i



    
        




