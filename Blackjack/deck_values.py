
def get_deck():

    open_file = open('deck.txt', 'r')
    deck = open_file.read()
    open_file.close()
    deck = deck.split("#")

    deck, deck_dict = get_values(deck)
    return deck, deck_dict

def get_values(deck):

    i = 1
    values = []

    for x in range(len(deck)):
        values.append(i)
        if deck[x].find("/") != -1:
            i += 1
            string = deck[x]
            deck[x] = string.strip("/")
    
    deck_dict = deck_to_dict(deck, values)
    return deck, deck_dict


def deck_to_dict(deck, values):

    deck_dict = {}

    for x in range(len(deck)):
        deck_dict[deck[x]] = values[x]
    return deck_dict

#deck, deck_dict = get_deck()
