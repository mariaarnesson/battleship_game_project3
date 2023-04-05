from random import randint
from itertools import zip_longest


board = [
    ['_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_'],
    ]


guesses_board = [
    ['_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_'],
    ]
letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6
    }


def main_menu():

    start_game()
    play_game()
    end_game()


def start_game():
    print('WELCOME TO BATTLESHIP GAME \n')
    print('_________________________________________')
    print('_________________________________________')
    print('    Hello and Welcome to Battleshipgame!')
    print('_________________________________________')
    print('_________________________________________')
    print('                                       \n')
    print('                         ____||__  _____||__  ')
    print('                ____||_ )________( )_________(  ')
    print('               )_______( ____||__  _____||__   ')
    print('                ____||_ )________( )_________(  ')
    print('               )_______()________( )_________( ')
    print('                ____||_  ____||__  _____||__  ')
    print('               )_______()________( )_________( ')
    print('                    ||  )________( )_________( ')
    print('                  __||______||__________||_____ ')
    print('                  ___________________________   \n')
    print('                     _____________________')
    print('                     ____________________     ')
    name = input('Please, enter your name: ')
    print('Hello', name + '!')
    input('Press Enter to continue')

    print('___________________________________________')
    print('___________________________________________')
    print('           BATTLESHIP GAME                ')
    print('___________________________________________')
    print('___________________________________________')

    print('      ______________________________________________________')
    print('     |           WELCOME TO MY GAME CALLED BATTLESHIP!      |')
    print('     |                                                      |')
    print('     |  You have 5 ships and you can freely place them on   |')
    print('     |  your board. To do this, you have to decide which    |')
    print('     | column (marked with the letters A-H) and row (marked |')
    print('     | with the numbers 1-7) you will place them. Afterwards|')
    print("     | you need to guess the computer's ships placed on a   |")
    print('     | another game board.                                  |')

    number = ['   ', '  1', '  2', '  3', ' 4',  ' 5']
    boats = ['', 'Carrier', 'Battleship', 'Destroyer', 'Submarine', 'Cruiser']
    scale = ['         SIZE', '   |1|', '|1|', ' |1|', '  |1|', '    |1|']

    for number, boats, scale, in zip_longest(number, boats, scale):
        print('______________________________')
        print(number, boats, scale)
        print('______________________________')


def create_ships():

    column = input('Please, choose some letter between A-G: ')
    while column not in 'ABCDEFG':
        print('Incorrect! You should choose A, B, C, D, E, F or G')
        column = input('Please, choose a letter between A-G')
    row = input('Please, choose the row 1-7 of the ship: ')
    while row not in '1234567':
        print('Incorrect! You should choose 1, 2, 3, 4, 5, 6 or 7')
        row = input('Please, choose a letter between 1-7')
    return int(row)-1, letters_to_numbers[column]


def print_board(board):
    print('||A|B|C|D|E|F|G')

    row_number = 1
    for row in board:
        print('%d|%s|' % (row_number, '|'.join(row)))

        row_number = row_number + 1

def get_coor(self):
        """
        user will enter coordinates (row and column) for the ship to go
        """
        while (True):
            user_input = input("Please enter coordinates (row,col) ? ")
            try:
                # see that user entered 2 values seprated by comma
                coor = user_input.split(",")
                if len(coor) != 2:
                    raise Exception("Invalid entry, too few/many coordinates.");
                # check that 2 values are integers
                coor[0] = int(coor[0]) - 1
                coor[1] = int(coor[1]) - 1
                # check that values of integers are between 1 and 10 for both coordinates
                if coor[0] > 9 or coor[0] < 0 or coor[1] > 9 or coor[1] < 0:
                    raise Exception("Invalid entry. Please use values between 1 to 10 only.")
                # if everything is ok, return coordinates
                return coor
            # if the user enters something different
            except ValueError:
                print("Invalid entry. Please enter only numeric values for coordinates")
            except Exception as e:
                print(e)
def play_game():
    # loop for 5 ships
    for n in range(5):
        print('PLEASE, PLACE THE SHIP ', n + 1, 'ON YOUR GAME-BOARD')
        row_number, column_number = create_ships()

        # Check that there are no repeats
        if board[row_number][column_number] == 'X':
            print('There is already a ship in this place!')

        board[row_number][column_number] = 'X'
        print_board(board)

    guesses = 0
    while guesses < 5:
        print('____________________________________________________________')
        print("   GUESS LOCATIONS OF THE SHIPS ON THE COMPUTER'S GAME BOARD")
        print('____________________________________________________________')
        row_number, column_number = create_ships()

        if guesses_board[row_number][column_number] != '_':
            print('You have already guessed that place!')
            continue

        if board[row_number][column_number] == 'X':
            print('HIT!')
            guesses_board[row_number][column_number] = 'X'
        else:
            guesses_board[row_number][column_number] = '.'
            print('MISS!')
        print_board(guesses_board)
        guesses = guesses + 1


def end_game():
    print('GAME OVER!')
    print('                ___________________________')
    print('               |       GAME OVER!          |')
    print('               | Thank you for plaing      |')
    print('                ___________________________\n')


main_menu()
