import random


def read_file(file_name):

    read_file = open(file_name, 'r')
    words = read_file.readlines()
    read_file.close()

    return words


def select_random_word(words):

    word = words[random.randint(0, (len(words) - 1))]
    l = word[random.randint(0 , (len(word) - 2))]

    print("Guess the word:", word.replace(l , '_' , 1))

    return word , l

def get_user_input(l):
   
    answer = input("Guess the missing letter: ")
    if (answer == l):
        print("Correct!")
    else:
        print("Wrong!")

    return answer 

def get_user_file():

    words_file = input("Use your own .txt file? Leave blank for short_words.txt: ")
    if (words_file == ""):
        words_file = "short_words.txt"

    return words_file

def run_game(file_name):
    
    words = read_file(file_name)
    word , l = select_random_word(words)
    answer = get_user_input(l)
    print('The word was: '+word)


if __name__ == "__main__":

    words_file = get_user_file()
    run_game(words_file)
