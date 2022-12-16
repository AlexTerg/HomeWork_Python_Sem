from os import listdir
def start_programm():
    value = int(input('Привет. Добро пожаловать в приложение по работе с телефонной книгой.\
        \nДля продолжение выберете действие\n1 - Создать справочник.\
        \n2 - Импортировать из txt в csv\n3 - Экспортировать из csv в txt\n'))
    return value


def get_second_name():
    second_name = input('Введите фамилию\n')
    return second_name


def get_first_name():
    first_name = input('Введите имя\n')
    return first_name



def get_phone_number():
    phone = input('Введите номер телефона\n')
    return phone


def get_description():
    description = input('Введите описание\n')
    return description


def get_file_format():
    value = int(input('В каком формате сохранить данные?\n1 - txt\n2 - csv\n'))
    return value

def get_filename():
    filename = input('Введите название файла\n')
    return filename

def get_continue():
    value = int(input('Добавить еще человека?\n1 - да\n2 - нет\n'))
    return value

def import_to():
    value = int(input('Импортировать из:\n1 - txt в csv\n2 - csv в txt\n'))
    return value

def get_directory():
    directory = input('Укажите папку где находится файл\n')
    
    for num, filename in enumerate(listdir(directory), 1):
        print(f'{num} - {filename}')
    file = int(input('Выберете файл. Цифра соответствует файлу\n'))
    filename = listdir(directory)[file - 1]
    return directory, filename
