import random

def assign_cards():

    player = []

    for x in range(2):
        y = random.randint(1, 10)
        player.append(y)

    return player

def card_sum(player):

    total = 0

    for x in player:
        total += x
    
    return total

def hit(player):

    player.append(random.randint(1, 10))

    return player

def run_game():

    player = assign_cards()

    while card_sum(player) < 21:
        print("Your cards total to", card_sum(player))
        answer = input("Hit or fold: ")
        while answer.lower() not in ["hit", "fold"]:
            answer = input("Hit or fold: ")
        if answer.lower() == "hit":
            player = hit(player)
        
    
    if card_sum(player) > 21:
        print("Bust!")
    elif card_sum(player) < 21:
        print("Stuff")
    else: print("Blackjack!")


if __name__ == '__main__':
    run_game()