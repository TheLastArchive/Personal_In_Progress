from random import randint 
from pprint import pprint

player_1_grid = []
player_2_grid = []

def create_grid():
    """Creates the grids for both players using lists
    Uses global variables for ease of use"""

    global player_1_grid, player_2_grid

    for i in range(0, 10):
        player_1_grid.append([])
        player_2_grid.append([])        
        for x in range(0, 10):
            player_1_grid[i].append(" ")
            player_2_grid[i].append(" ")


def get_user_placements():
    """Get user's choice on where to place their ships"""

    ships = {"Carrier" : 5, "Battleship": 4, "Submarine": 3, "Cruiser": 3, "Destroyer": 2}
    print("Choose a cell (eg. E5) and an orientation ('horizontal' Left -> Right | 'vertical' Top -> Bottom)")
    
    for ship in ships:
        command = input(f"{ship}: ")
        place_user_ships(command, ships.get(ship))


def place_user_ships(command, ship_length):
    """TODO Use the user's input to add the ship placement's"""

    global player_1_grid

    letter_convert = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9}

    command = command.split(" ")
    if not command:
        print("Invalid command")
        return
    orientation = command[1]
    column_row = list(command[0])
    column = letter_convert.get(column_row[0].lower())
    if column is None:
        print("Out of range")
        return
    row = int(column_row[1])
    if row not in range(0, 10):
        print("Out of range")
        return

    if orientation.lower() == 'horizontal':
        for i in range(0, ship_length):
            player_1_grid[row][column + i] = 'S'
    else: #if orientation == vertical
        for i in range(0, ship_length):
            player_1_grid[row + i][column] = 'S'
    
    display_grid()
    pass


def display_grid():
    """Prints out the user's grid"""

    print('\n')
    print('      A    B    C    D    E    F    G    H    I    J\n')
    for i in range(0, 10):
        if i == 10:
            print(str(i), "", player_1_grid[i])
            print('\n')
        else:
            print(str(i) , " ", player_1_grid[i])
            print('\n')


if __name__ == '__main__':

    create_grid()
    get_user_placements()
