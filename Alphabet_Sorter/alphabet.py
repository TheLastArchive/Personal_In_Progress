
from typing import Text


def get_user_file():

    file_name = input("Enter the name of the file to be sorted: ")
    try:
        open_file = open(file_name, 'r')
    except FileNotFoundError:
        print('File does not exist')
    else:
        words = open_file.readlines()
        open_file.close()
        print(words)


def save_data(words):

    f = open("/home/wtc/Alex_Stuff/Python-Practice/Alphabet_Sorter/test.txt", 'w')
    f.write(str(words))
    f.close()

def sort_file(words):

    path = '/home/wtc/Alex_Stuff/Python-Practice/Alphabet_Sorter/DIO.txt'

    f = open(path, 'r')
    storage = f.read()
    f.close()
    words = storage
    save_data(words)


words = get_user_file()
sort_file(words)