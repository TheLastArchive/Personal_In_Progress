import random
import deck_values

def assign_cards(deck):

    player = []

    for x in range(2):
        index = random.randint(0, 51)
        while deck[index] == '_':
            index = random.randint(0, 51)   
        player.append(deck[index])
        deck[index] = '_'
    
    return player, deck


def run_game(deck):

    player_hand, deck = assign_cards(deck)
    
    print("Your starting hand is", player_hand)
    

if __name__ == '__main__':

    deck = deck_values.get_deck()
    run_game(deck)