from views import get_second_name, get_first_name, get_phone_number, get_description
import csv
import numpy


def get_user_lst():
    user_info = [get_second_name(), get_first_name(),
                 get_phone_number(), get_description()]
    return user_info


def write_user_txt(user_lst, filename):
    with open(f'{filename}.txt', 'a', encoding='utf-8') as file:
        for info in user_lst:
            file.write(f'{info}\n')


def write_user_csv(user_lst, filename):
    with open(f'{filename}.csv', mode='a', encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
        file_writer.writerow(user_lst)


def import_txt_to_csv(directory, filename):
    with open(f'{directory}/{filename}', 'r', encoding='utf-8') as file:
        text = file.read()
        text = text.split('\n')
        if text[-1] == '':
            text = numpy.array(text[:-1])
        else:
            text = numpy.array(text)
        new_text = text.reshape(-1, 4)
    with open(f'{directory}/{filename[:-4]}.csv', mode='w', encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
        for item in new_text:
            file_writer.writerow(item)


def export_csv_to_txt(directory, filename):
    text_lst = []

    with open(f'{directory}/{filename}', mode='r', encoding='utf-8') as r_file:
        file_read = csv.reader(r_file, delimiter=";")
        for i in file_read:
            for k in i:
                text_lst.append(k)

    with open(f'{directory}/{filename[:-4]}.txt', 'w', encoding='utf-8') as file:
        for i in text_lst:
            file.write(f'{i}\n')
