import random

def deck_to_list():

    f = open('deck.txt', 'r')
    deck = f.read()
    f.close()
    deck = deck.split("#")

    return deck


def assign_cards(deck):

    player = []

    for x in range(2):
        index = random.randint(0, 51)
        while deck[index] == '_':
            index = random.randint(0, 51)   
        player.append(deck[index])
        deck[index] = '_'
    
    return player, deck


def run_game():

    print("Welcome to Blackjack!")
    

if __name__ == '__main__':
    run_game()