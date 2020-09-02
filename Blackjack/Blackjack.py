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

    total = 0
    for x in player:
        total += deck_dict.get(x)
    return total


def quit_game(deck, player, cont):

    print("Thanks for playing!")
    cont = False

    return deck, player, cont


def fold(deck, player, cont):

    print("You have folded and have lost the round.")
    cont = False

    return deck, player, cont

def hit_player(deck, player, cont):

    i = random.randint(0, 51)
    while deck[i] == '_':
        i = random.randint(0, 51)
    player.append(deck[i])
    deck[i] = '_'

    return deck, player, cont


def run_game(deck, deck_dict):

    player, deck = assign_cards(deck)
    commands = {
        "hit": hit_player,
        "fold": fold,
        "quit": quit_game
    }

    cont = True
    while card_sum(player, deck_dict) < 21 and cont == True:
        print("Your hand:", player)
        ans = input("Hit, Fold or Quit?: ")

        while ans.lower() not in commands:
            ans = input("Hit, Fold or Quit?: ")

        deck, player, cont = commands.get(ans.lower())(deck, player, cont)

    if card_sum(player, deck_dict) > 21: print("Bust!")
    else: print("BLACKJACK!")

if __name__ == '__main__':

    deck, deck_dict = deck_values.get_deck()
    run_game(deck, deck_dict)