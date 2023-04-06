from random import randint
from itertools import zip_longest

# creates a list of 8 spaces, 8 times
hidden_board = [["_"] * 7 for x in range(7)]
guess_board = [["_"] * 7 for x in range(7)]
player_board = [["_"] * 7 for x in range(7)]

# converts letters to numbers and numbers to letters
letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6
    }
    
numbers_to_letters = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G'
    }
player_score = 0
computer_score = 0

continue_playing_options = ["ok", "end game"]

  # https://www.programiz.com/python-programming/methods/string/title  
  # https://www.programiz.com/python-programming/methods/string/upper
    
def start_game(): 
    create_ships(hidden_board)
    create_ships(player_board)
    print('_________________________________________')
    print('_________________________________________')
    text='    Hello and Welcome to Battleshipgame!'
    print(text.title())
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
    print('___________________________________________')
    print('___________________________________________')
    message = '           BATTLESHIP GAME                '
    print(message.upper())
    print('___________________________________________')
    print('___________________________________________')

    print('      ______________________________________________________')
    print('     |           WELCOME TO MY GAME CALLED BATTLESHIP!      |')
    print('     |                                                      |')
    print('     |  You have 5 ships that are already placed on your    |')
    print('     |  game board. Now you have to guess where the ships   |')
    print('     |are placed on the computer game board. To do this, you|')
    print ('    |have to decide the ships column and row ( marked with |')
    print('     | letters A-H and numbers 1-7).                         |')
    print("     | You have 10 turns to find all of the ships.          |")
    print('      ______________________________________________________')
    number = ['   ', '  1', '  2', '  3', ' 4',  ' 5']
    boats = ['', 'Carrier', 'Battleship', 'Destroyer', 'Submarine', 'Cruiser']
    scale = ['         SIZE', '   |1|', '|1|', ' |1|', '  |1|', '    |1|']

    for number, boats, scale, in zip_longest(number, boats, scale):
        print('______________________________')
        print(number, boats, scale)
        print('______________________________')
        
    print("____________________________________")
    global name
    name = input("Please, enter your name:\n")
    while name == "" or name == " ":
        print("Error! Please, enter your name:")
        username = input("Please enter your name:\n")
        input('Press Enter to continue')

def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 6), randint(0, 6)
        while board[ship_row][ship_column] == "*":
            ship_row, ship_column = randint(0, 6), randint(0, 6)
        board[ship_row][ship_column] = "*"
        
def print_board(board):
    print("  A|B |C |D |E |F |G")
    row_number = 1
    for row in board:
        print(row_number, "|_".join(row))
        row_number += 1        


def computer_guess(board):
    global computer_score
    computer_row, computer_column = randint(0, 6), randint(0, 6)
    if (player_board[computer_row][computer_column] == "-" or
            player_board[computer_row][computer_column] == "x"):
        computer_row = randint(0, 6)
        computer_column = randint(0, 6)
    elif player_board[computer_row][computer_column] == "*":
        input('Press Enter to continue')
        print(
            f"The computer guessed row {computer_row +1}"
            f" and column {numbers_to_letters[computer_column]}")
        player_board[computer_row][computer_column] = "x"
        computer_score += 1
        print(f"Your battleship has been hit!")
    else:
        input('Press Enter to continue')
        print(
            f"The computer guessed row {computer_row +1}"
            f" and column {numbers_to_letters[computer_column]}")
        player_board[computer_row][computer_column] = "-"
        print(f"The computer missed! {name}, You still have a chance to win!!")
def get_ship_location():
    print('____________________________________________________________')
    print("   GUESS LOCATIONS OF THE SHIPS ON THE COMPUTER'S GAME BOARD")
    print('____________________________________________________________')
    row = input('Please, choose the row 1-7 of the ship: \n')
    while row not in "1234567" or len(row) > 1 or row == "":
        validate_row(row)
        print('Incorrect! You should choose 1, 2, 3, 4, 5, 6 or 7')
        row = input('Please, choose a number between 1-7\n')
    column = input('Please, choose some letter between A-G: \n').upper()
    while column not in "ABCDEFGH" or len(column) > 1 or column == "":
        validate_column(column)
        print('Incorrect! You should choose A, B, C, D, E, F or G')
        column = input('Please, choose a letter between A-G \n').upper()
    return int(row) - 1, letters_to_numbers[column]

def validate_row(values):
    try:
        [int(value) for value in values]
        if int(values) < 1 or int(values) > 7:
            print(
                f"Number between 1-7 required, you provided '{values}'."
           )
    except:
        print(f"Sorry number between 1-7 required, please try again.\n")
        return False

    return True


def validate_column(values):
    try:
        if values not in letters_to_numbers:
            print(
                f"Letter between A-G required, you provided '{values}'."
                )
    except:
        print(f"Sorry letter between A-G required, please try again.\n")
        return False

    return True


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "x":
                count += 1
    return count
def validate_continue_playing(values):
    try:
        if values not in continue_playing_options:
            print(
                f"Please press 'ok' or 'end game', you provided '{values}'."
                )
    except:
        print(f"Sorry 'ok'/'end game' required, please try again.\n")
        return False

    return True

def play_game():
    turns = 10
    global user_score

    while turns > 0:
        print('_____________________')
        print('_____________________')
        print(f"    {name}'s Board")
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
        row, column = get_ship_location()
        if guess_board[row][column] == "-" or guess_board[row][column] == "x":
            print('_____________________________________________')
            print('_____________________________________________')
            print("Error! You have already guessed that place!")
            print('_____________________________________________')
            print('_____________________________________________')
        elif hidden_board[row][column] == "*":
            print('____________________________________________________')
            print('____________________________________________________')
            print(f" You hit a  battleship!")
            print('____________________________________________________')
            print('____________________________________________________')
            guess_board[row][column] = "x"
            turns -= 1
            computer_guess(player_board)
            player_score += 1
        else:
            print('____________________________________________________')
            print('____________________________________________________')
            print(f"You missed!")
            print('____________________________________________________')
            print('____________________________________________________')
            guess_board[row][column] = "-"
            turns -= 1
            computer_guess(player_board)
        if count_hit_ships(guess_board) == 5:
            print('____________________________________________________')
            print('____________________________________________________')
            print(
                f"Congratulations {username}, "
                "you have sunk all of the battleships!")
            print('____________________________________________________')
            print('____________________________________________________')
            print("The game is now over.")
            break
            print('_____________________________________________')
            print('_____________________________________________')
            print("You have " + str(turns) + " chances left!")
            print('_____________________________________________')
            print('_____________________________________________')
            print(f"||  {username}'s SCORE: {player_score}   || "
                     f" COMPUTER'S SCORE: {computer_score}  ||")
            print('_____________________________________________')
            print('_____________________________________________')
            if turns == 0:
                print(
                    f"You ran out of turns {username}, the game is over.")
                print('                ___________________________')
                print('               |       GAME OVER!          |')
                print('               | Thank you for plaing      |')
                print('                ___________________________\n') 
                print('Press enter to restart')
                
                break
            if count_hit_ships(player_board) == 5:
                print(
                    f"The computer"
                    " has sunk all of your battleships!")
                print('                ___________________________')
                print('               |       GAME OVER!          |')
                print('               | Thank you for plaing      |')
                print('                ___________________________\n')  
                print('Press enter to restart')
                
                break
            if count_hit_ships(guess_board) < 5:
                continue_playing = input(
                        "To continue press 'ok' otherwise press 'end game'. \n").lower()
                while continue_playing not in continue_playing_options:
                    validate_continue_playing(continue_playing)
                    continue_playing = input(
                        "To continue press 'ok' otherwise press 'end game'. \n").lower()
                       
                if continue_playing == "ok" or continue_playing == "ok":
                    print(
                        "You have decided to continue playing the game.")
                    continue
                elif continue_playing == "end game" or continue_playing == "end game":
                    print(
                        "You have decided to finish the game,"
                        "the game is now over.")
                    break
                else:
                    print("Please enter 'yes' or 'no'")
                    continue_playing = input(
                        "Do you want to continue playing? y/n \n")
                        
def main():
    start_game()
    play_game()
    
    
main()