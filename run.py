"""
Modules:
"""
from random import randint
import time
import os
from colorama import Fore


hidden_board = [["_"] * 9 for x in range(9)]
guess_board = [["_"] * 9 for x in range(9)]
player_board = [["_"] * 9 for x in range(9)]


numbers_to_letters = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G',
    7: 'H',
    8: 'I'
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
    'I': 8
    }


continue_game_options = 'ok', 'end game'

PLAYER_SCORE = 0
COMPUTER_SCORE = 0


def clear():
    """
    Clear the terminal.
    """
    os.system("cls" if os.name == "nt" else "clear")


def start_menu():
    """
    Start the game menu.
    """
    print('\033[1;32m_________________________________________')
    print('_________________________________________')
    text = '    Hello and Welcome to Battleshipgame!\n'
    print(text.title())
    print('                        ____||__  _____||__  ')
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
    print(' At the begging, choose one of the options:')
    print('1. Play the game')
    print('2. Read Instructions.')
    start = input('Enter your ooption here:\n')

    if start == '1':
        start_game()
    elif start == '2':
        instructions()
    else:
        print(+ f'Inorrect!!! You entered: {start}. Please enter 1 or 2.\n')


def start_game():
    """Function start game."""
    # https://www.textfacescopy.com/loading-symbol.html
    create_random_ships(hidden_board)
    create_random_ships(player_board)
    print('\033[1;32m_________________________________________')
    message = '           battleship game                '
    print(message.upper())
    name = input("Please, enter your name:\n")
    print(f" Hello and welcome to my game, {name}!")
    while name == "" or name == " ":
        print(Fore.RED + "Error! Please, enter your name:")
        name = input("\033[1;32m Please enter your name:\n")
    print('\033[1;32m                   LOADING...')
    print('                  [■■■■■□□□□□] 50%')
    time.sleep(2)
    print('                   LOADING...')
    print('                  [■■■■■■■■■□]6 90%')
    time.sleep(2)
    clear()


def instructions():
    """
    Function to show the instructions.
    """
    message = '           BATTLESHIP GAME                '
    print(message.upper())
    print('\033[1;32m( _ __)¯`·._.·´¯`·._.·´¯¯`·._.·´¯`·._.·´¯¯`·._.·( _ __)')
    print('( _ __)                                         ( _ __).')
    print('( _ __)  WELCOME TO MY GAME CALLED BATTLESHIP!  ( _ __)')
    print('( _ __)                                         ( _ __)')
    print('( _ __)  You have 10 ships that are already     ( _ __)')
    print('( _ __)  placed on your game board. Now you     ( _ __)')
    print('( _ __)  have to guess where the ships are      ( _ __)')
    print('( _ __)  placed on the computer game board.     ( _ __)')
    print('( _ __)  To do this, you have to decide the     ( _ __)')
    print("( _ __)  the ships column and row (marked       ( _ __)")
    print('( _ __)  with letters A-I and number 1-7).      ( _ __).')
    print('( _ __)  You have 20 turns to find all of       ( _ __).')
    print('( _ __)               the ships.                ( _ __).')
    print('( _ __)                                         ( _ __).')
    print('( _ __)                      God Luck!          ( _ __).')
    print('( _ __)                         and             ( _ __).')
    print('( _ __)                      Have Fun!          ( _ __).')
    print('( _ __)                                         ( _ __).')
    print('( _ __)¯`·._.·´¯`·._.·´¯¯`·._.·´¯`·._.·´¯¯`·._.·( _ __) ')
    input('press enter to start a game.')


def print_board(board):
    """Function printing board."""
    print("  A|B |C |D |E |F |G |I |J ")
    row_number = 1
    for row in board:
        print(row_number, "|_".join(row))
        row_number += 1


def create_random_ships(board):
    """Function creating ships."""
    # https://github.com/gbrough/battleship/blob/main/single_player.py
    for ship in range(10):
        ship_row, ship_column = randint(0, 8), randint(0, 8)
        while board[ship_row][ship_column] == "✩":
            ship_row, ship_column = randint(0, 8), randint(0, 8)
        board[ship_row][ship_column] = "✩"


def computer_guess():

    """Function guessing computer play board."""
    COMPUTER_SCORE = 0
    computer_row, computer_column = randint(0, 8), randint(0, 8)
    if (player_board[computer_row][computer_column] == "-" or
            player_board[computer_row][computer_column] == "★"):
        computer_row = randint(0, 9)
        computer_column = randint(0, 9)
    elif player_board[computer_row][computer_column] == "✩":
        input('Press enter to continue')
        print(
            f"The computer guessed row {computer_row +1}"
            f" and column {numbers_to_letters[computer_column]}")
        print("Your battleship has been hit!")
        player_board[computer_row][computer_column] = "★"
        COMPUTER_SCORE += 1
    else:
        input('Press enter to continue')
        print(
            f"The computer guessed row {computer_row +1}"
            f" and column {numbers_to_letters[computer_column]}")
        print(" The computer missed!")
        player_board[computer_row][computer_column] = "-"


def ship_location():
    """Function locating ship."""
    # https://github.com/gbrough/battleship/blob/main/single_player.py
    print(
        "\033[1;32m GUESS LOCATIONS OF THE SHIPS ON THE COMPUTER'S GAME BOARD"
        )
    row = input('Please, choose the row 1-10 of the ship: \n')
    while row not in "123456789" or len(row) > 1 or row == "":
        validate_row(row)
        print(Fore.RED + 'Incorrect!')
        print(Fore.RED + 'You should choose 1, 2, 3, 4, 5, 6, 7, 8 or 9')
        row = input('\033[1;32m Please, choose a number between 1-9\n')
    column = input('Please, choose some letter between A-I: \n')
    while column not in "ABCDEFGHI" or len(column) > 1 or column == "":
        validate_column(column)
        print(Fore.RED + 'Incorrect!')
        print(Fore.RED + 'You should choose A, B, C, D, E, F, G, H or I')
        column = input('\033[1;32m Please, choose a letter between A-I \n')
    return int(row) - 1, letters_to_numbers[column]


def validate_row(place_number):
    """Function validating row."""

    try:
        if int(place_number) < 1 or int(place_number) > 9:
            print(Fore.RED + f"{place_number} is wrong!")
    except TypeError:
        print("\033[1;32m Please, try again!")
        print("You should choose 1, 2, 3, 4, 5, 6, 7, 8 or 9.\n")
        return False

    return True


def validate_column(values):
    """Function validating column."""
    try:
        if values not in letters_to_numbers:
            print(Fore.RED + f"'{values}' is wrong!")
    except ValueError:
        print("\033[1;32m Please try again!")
        print("You should choose A, B, C, D, E, F, G, H or I \n")
        return False

    return True


def hit_ships(board):
    """Function hitting ships."""
    # https://github.com/gbrough/battleship/blob/main/single_player.py
    count = 0
    for row in board:
        for column in row:
            if column == "★":
                count += 1
    return count


def validate_continue_game(stop_game):
    """Function contuating game."""
    try:
        if stop_game not in continue_game_options:
            print(Fore.RED + f" '{stop_game}' is wrong!")
            print(Fore.RED + "Please press 'ok' or 'end game'.")
    except ValueError:
        print("\033[1;32m  Try again.")
        print(" Please press 'ok' or 'end game'.\n")
        return False

    return True


def play_game():
    """Function playing game."""
    turns = 20
    global PLAYER_SCORE

    while turns > 0:
        print('\033[1;32m_____________________')
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
            print(Fore.RED + "Incorrect!")
            print(Fore.RED + "You have already guessed that place!")
            print('\033[1;32m_____________________________________________')
        elif hidden_board[row][column] == "✩":
            print('\033[1;32m__________________________________________')
            print("Well done!! You hit a ship!")
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
        print("You have " + str(turns) + " chances left!")
        print('_____________________________________________')
        print('_____________________________________________')
        print(f" |Your's Score: {PLAYER_SCORE}    |")
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
                print(Fore.RED + "Incorrect!!!")
                continue_game = input(
                    "\033[1;32m You should press 'ok' or 'end game'.\n")


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
        print(Fore.RED + 'Incorrect!!!')
        print(Fore.RED + f'You entered: {answer}. Please enter 1 or 2.')


def main_menu():
    """Function main menu."""
    start_menu()
    start_game()
    play_game()
    play_again()


main_menu()
