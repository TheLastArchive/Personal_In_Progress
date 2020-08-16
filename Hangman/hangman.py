import random
import sys


def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()


def get_user_input():
    return input('Guess the missing letter: ')


def ask_file_name():
    file_name = input("Words file? [leave empty to use short_words.txt] : ")
    if not file_name:
        return 'short_words.txt'
    return file_name


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    return word


def random_fill_word(word):

    random_index = random.randint(0, len(word) - 1)
    dupe_check = word[random_index]
    temp = list(word)
    i = 0
    
    while i <= len(word) - 1:
        if i == random_index or dupe_check == temp[i]:
           i+= 1
        else:
            temp[i] = '_'
            i += 1

    return "".join(temp)


def is_missing_char(original_word, answer_word, char):

    i = 0
    temp1 = list(original_word)
    temp2 = list(answer_word)

    if char in temp2: return False

    while i <= len(original_word) - 1:
        if char == temp1[i]: return True
        else: i += 1
    return False


def fill_in_char(original_word, answer_word, char):

    temp1 = list(original_word)
    temp2 = list(answer_word)
    i = 0

    while i <= (len(original_word) -1): #running the while loop through the entire word allows for
        if char == temp1[i]:            #duplicate letters to be revealed
            temp2[i] = char
            i += 1
        else: i += 1
    return "".join(temp2) #returns answer_word with new character


def do_correct_answer(original_word, answer, guess):
    answer = fill_in_char(original_word, answer, guess)
    print(answer)
    return answer


def do_wrong_answer(word, number_guesses, answer):

    if number_guesses == 0:
        draw_figure(0)
        print("Sorry, you are out of guesses. The word was: " +word)
    else:
        print('Wrong! Number of guesses left: '+str(number_guesses))
        draw_figure(number_guesses)
        print(answer)


def draw_figure(number_guesses):
    
    if number_guesses == 4:
        print("/----\n|\n|\n|\n|\n_______")
    elif number_guesses == 3:
        print("/----\n|   O\n|\n|\n|\n_______")
    elif number_guesses == 2:
        print("/----\n|   O\n|  /|\ \n|\n|\n_______")
    elif number_guesses == 1:
        print("/----\n|   O\n|  /|\ \n|   |\n|\n_______")
    else:
        print("/----\n|   O\n|  /|\\\n|   |\n|  / \\\n_______")
    

def win(word, number_guesses):

    print("Congratulations!")
    print(" \O/\n  | \n  |\n / \ ")


def run_game_loop(word, answer):

    print("Guess the word: "+answer)
    number_guesses = 5
    while number_guesses != 0 and word != answer:
        guess = get_user_input()
        if guess.lower() in ["exit", "quit"]:
            print("Bye!")
            break
        if is_missing_char(word, answer, guess):
            answer = do_correct_answer(word, answer, guess)
        else:
            number_guesses -= 1
            do_wrong_answer(word, number_guesses, answer)
    if word == answer: win(word, number_guesses)
            

if __name__ == "__main__":

    if len(sys.argv) > 1:
        words_file = sys.argv[1]
    else: words_file = ask_file_name()

    words = read_file(words_file)
    selected_word = select_random_word(words)
    current_answer = random_fill_word(selected_word)
    run_game_loop(selected_word, current_answer)
