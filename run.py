from random import randint
import time

# legend:

hidden_board = [["_"] * 10 for x in range(10)]
guess_board = [["_"] * 10 for x in range(10)]
player_board = [["_"] * 10 for x in range(10)]

numbers_to_letters = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G',
    7: 'H',
    8: 'I',
    9: 'J'
    }

letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9
    }

PLAYER_SCORE = 0
COMPUTER_SCORE = 0

continue_game_options = 'ok', 'end game'


def start_menu():
    """
    Start the game menu.
    """
    print('Choose one of the options to continue:')
    print('1. Play the game')
    print('2. Read Instructions.')
    start = input('Enter your ooption here:\n')

    if start == '1':
        start_game()
    elif start == '2':
        instructions()
    else:
        print(f'You entered: {start}. Please enter 1 or 2.\n')


def start_game():
    """Function start game."""
    # https://www.textfacescopy.com/loading-symbol.html
    print('                   LOADING...')
    print('                  [■■■■■□□□□□] 50%')
    time.sleep(2)
    print('                   LOADING...')
    print('                  [■■■■■■■■■□] 90%')
    time.sleep(1)
    create_random_ships(hidden_board)
    create_random_ships(player_board)
    print('_________________________________________')
    print('_________________________________________')
    text = '    Hello and Welcome to Battleshipgame!\n'
    print(text.title())
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
    print('___________________________________________')
    print('___________________________________________')
    name = input("Please, enter your name:\n")
    print(f" Hello {name}!")
    while name == "" or name == " ":
        print("Error! Please, enter your name:")
        name = input("Please enter your name:\n")


def instructions():
    """
    Function to show the instructions.
    """
    message = '           BATTLESHIP GAME                '
    print(message.upper())
    print('    ______________________________________________________ ')
    print('  / \                                                      \.')
    print(' |   |                                                      |.')
    print('  \_ |                                                      |.')
    print('     |           WELCOME TO MY GAME CALLED BATTLESHIP!      |')
    print('     |                                                      |')
    print('     |  You have 5 ships that are already placed on your    |')
    print('     |  game board. Now you have to guess where the ships   |')
    print('     |are placed on the computer game board. To do this, you|')
    print('     |have to decide the ships column and row ( marked with |')
    print('     | letters A-H and numbers 1-7).                        |')
    print("     | You have 10 turns to find all of the ships.          |")
    print('     |   ___________________________________________________|___')
    print('     |  /                                                      /.')
    print('     \_/dc____________________________________________________/.')
    input('press enter start a game.')


def print_board(board):
    """Function printing board."""
    print("  A|B |C |D |E |F |G |I |J | K ")
    row_number = 1
    for row in board:
        print(row_number, "|_".join(row))
        row_number += 1


def create_random_ships(board):
    """Function creating ships."""
    for ship in range(10):
        ship_row, ship_column = randint(0, 9), randint(0, 9)
        while board[ship_row][ship_column] == "✭":
            ship_row, ship_column = randint(0, 9), randint(0, 9)
        board[ship_row][ship_column] = "✭"


def computer_guess():

    """Function guessing computer play board."""
    global COMPUTER_SCORE
    computer_row, computer_column = randint(0, 9), randint(0, 9)
    if (player_board[computer_row][computer_column] == "-" or
            player_board[computer_row][computer_column] == "★"):
        computer_row = randint(0, 9)
        computer_column = randint(0, 9)
    elif player_board[computer_row][computer_column] == "✭":
        input('Press Enter to continue')
        print(
            f"The computer guessed row {computer_row +1}"
            f" and column {numbers_to_letters[computer_column]}")
        print("Your battleship has been hit!")
        player_board[computer_row][computer_column] = "★"
        COMPUTER_SCORE += 1
    else:
        input('Press Enter to continue')
        print(
            f"The computer guessed row {computer_row +1}"
            f" and column {numbers_to_letters[computer_column]}")
        print(" The computer missed!")
        player_board[computer_row][computer_column] = "-"


def ship_location():
    """Function locating ship."""
    print("   GUESS LOCATIONS OF THE SHIPS ON THE COMPUTER'S GAME BOARD")
    row = input('Please, choose the row 1-10 of the ship: \n')
    while row not in "12345678910" or len(row) > 1 or row == "":
        validate_row(row)
        print('Incorrect! You should choose 1, 2, 3, 4, 5, 6, 7, 8, 9 or 10')
        row = input('Please, choose a number between 1-10\n')
    column = input('Please, choose some letter between A-J: \n')
    while column not in "ABCDEFGH" or len(column) > 1 or column == "":
        validate_column(column)
        print('Incorrect! You should choose A, B, C, D, E, F, G, H, I or J')
        column = input('Please, choose a letter between A-J \n')
    return int(row) - 1, letters_to_numbers[column]


def validate_row(place_number):
    """Function validating row."""

    try:
        if int(place_number) < 1 or int(place_number) > 10:
            print(
                f"'{place_number}' is wrong!"
            )
    except TypeError:
        print("Please, try again!")
        print("You should choose 1, 2, 3, 4, 5, 6, 7, 8, 9 or 10.\n")
        return False

    return True


def validate_column(values):
    """Function validating column."""
    try:
        if values not in letters_to_numbers:
            print(
                f"'{values}' is wrong!"
                )
    except ValueError:
        print("Please try again!")
        print("You should choose A, B, C, D, E, F, G, H, I or J \n")
        return False

    return True


def hit_ships(board):
    """Function hitting ships."""
    count = 0
    for row in board:
        for column in row:
            if column == "★":
                count += 1
    return count


def validate_continue_game(values):
    """Function contuating game."""
    try:
        if values not in continue_game_options:
            print(
                f" '{values}' is wrong! Please press 'ok' or 'end game'."
                )
    except ValueError:
        print(" Try again.")
        print(" Please press 'ok' or 'end game'.\n")
        return False

    return True


def play_game():
    """Function playing game."""
    turns = 20
    global PLAYER_SCORE

    while turns > 0:
        print('_____________________')
        print('_____________________')
        print("    Your Board")
        print('_____________________')
        print('_____________________')
        print_board(player_board)
        print('')
        print('')
        print('_____________________')
        print('_____________________')
        print("  Computer's Board")
        print('_____________________')
        print('_____________________')
        print_board(guess_board)
        row, column = ship_location()
        if guess_board[row][column] == "-" or guess_board[row][column] == "★":
            print('_____________________________________________')
            print("Incorrect! You have already guessed that place!")
            print('_____________________________________________')
        elif hidden_board[row][column] == "✭":
            print('____________________________________________________')
            print(" You hit a ship!")
            print('____________________________________________________')
            guess_board[row][column] = "★"
            turns -= 1
            computer_guess()
            PLAYER_SCORE += 1
        else:
            print('____________________________________________________')
            print("You missed!")
            print('____________________________________________________')
            guess_board[row][column] = "-"
            turns -= 1
            computer_guess()
        if hit_ships(guess_board) == 10:
            print('____________________________________________________')
            print("Congratulations!")
            print("you have sunk all of the battleships!")
            print('____________________________________________________')
            print('                ___________________________')
            print('               |       GAME OVER!          |')
            print('               | Thank you for plaing      |')
            print('                ___________________________\n')
            play_again()
            break
        print('_____________________________________________')
        print('_____________________________________________')
        print("You have " + str(turns) + " chances left!")
        print('_____________________________________________')
        print('_____________________________________________')
        print(f" |Your's Score: {PLAYER_SCORE}|")
        print(f" |Computer's Score: {COMPUTER_SCORE}|")

        if turns == 0:
            print("You ran out of turns, the game is over.")
            print('                ___________________________')
            print('               |       GAME OVER!          |')
            print('               | Thank you for plaing      |')
            print('                ___________________________\n')
            play_again()
            break
        if hit_ships(player_board) == 10:
            print(
                "The computer won!")
            print('                ___________________________')
            print('               |       GAME OVER!          |')
            print('               | Thank you for plaing      |')
            print('                ___________________________\n')
            play_again()
            break
        if hit_ships(guess_board) < 10:
            continue_game = input(
                    "To continue press 'ok' otherwise press 'end game'. \n")
            while continue_game not in continue_game:
                validate_continue_game(continue_game)
                continue_game = input(
                    "To continue press 'ok' otherwise press 'end game'. \n")
            if continue_game == "ok" or continue_game == "ok":
                continue
            elif continue_game == "end game" or continue_game == "end game":
                print('                ___________________________')
                print('               |       GAME OVER!          |')
                print('               | Thank you for plaing      |')
                print('                ___________________________\n')
                play_again()
                break
            else:
                print("Incorrect!!!")
                continue_game = input(
                    "You should press 'ok' or 'end game'.\n")


def play_again():
    """
    Function for playing again.
    """
    print('Choose one of the options:')
    print('1. Play the Game Again.')
    print('2. End Game')
    answer = input('Enter your option here: ')

    if answer == '1':
        start_game()
    elif answer == '2':
        exit()
    else:
        print(f'You entered: {answer}. Please enter 1 or 2.')


def main_menu():
    """Function main menu."""
    start_menu()  
    start_game()
    play_game()
    play_again()


main_menu()
