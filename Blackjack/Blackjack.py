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


def card_sum(player, deck_dict):

    return

def hit_player(deck, player):

    i = random.randit(0, 51)
    player.append(deck[i])
    deck[i] = '_'

    return deck, player


def run_game(deck, deck_dict):

    player_hand, deck = assign_cards(deck)
    
    while card_sum(player_hand, deck_dict) < 21:
    

if __name__ == '__main__':

    
    deck, deck_dict = deck_values.get_deck()
    run_game(deck, deck_dict)