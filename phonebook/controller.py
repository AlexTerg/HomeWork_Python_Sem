from views import start_programm, get_file_format, get_filename, get_continue, get_directory
from model import get_user_lst, write_user_txt, write_user_csv, import_txt_to_csv, export_csv_to_txt


def phonebook():
    value = start_programm()
    if value == 1:
        file_format = get_file_format()
        file_name = get_filename()
        value_continue = 1
        while value_continue != 2:
            user = get_user_lst()
            if file_format == 1:
                write_user_txt(user, file_name)
            elif file_format == 2:
                write_user_csv(user, file_name)
            value_continue = get_continue()
    elif value == 2:
        directory, filename = get_directory()
        import_txt_to_csv(directory, filename)
    elif value == 3:
        directory, filename = get_directory()
        export_csv_to_txt(directory, filename)
