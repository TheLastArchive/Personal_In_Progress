
def get_user_file():

    file_name = input("Enter the name of the file to be sorted: ")
    try:
        open_file = open(file_name, 'r')
    except FileNotFoundError:
        print('File does not exist')
    else:
        words = open_file.readlines()
        return words

def sort_words(words):

get_user_file()