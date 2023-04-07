from random import randint


hidden_board = [["_"] * 7 for x in range(7)]
guess_board = [["_"] * 7 for x in range(7)]
player_board = [["_"] * 7 for x in range(7)]

numbers_to_letters = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G'
    }

letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6
    }

player_score = 0
computer_score = 0


def start_game():
    create_ships(hidden_board)
    create_ships(player_board)
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
    print('      ______________________________________________________')
    print('     |           WELCOME TO MY GAME CALLED BATTLESHIP!      |')
    print('     |                                                      |')
    print('     |  You have 5 ships that are already placed on your    |')
    print('     |  game board. Now you have to guess where the ships   |')
    print('     |are placed on the computer game board. To do this, you|')
    print('     |have to decide the ships column and row ( marked with |')
    print('     | letters A-H and numbers 1-7).                         |')
    print("     | You have 10 turns to find all of the ships.          |")
    print('      ______________________________________________________')
    global name
    name = input("Please, enter your name:\n")
    while name == "" or name == " ":
        print("Error! Please, enter your name:")
        name = input("Please enter your name:\n")

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
        print(f" {name}, the computer missed!")
        player_board[computer_row][computer_column] = "-"    


       

def ship_location():
    print("   GUESS LOCATIONS OF THE SHIPS ON THE COMPUTER'S GAME BOARD")
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
                f" '{values}' is wrong! You should choose 1, 2, 3, 4, 5, 6 or 7"
        )
    except:
        print(f"Please, try again! You should choose 1, 2, 3, 4, 5, 6 or 7.\n")
        return False

    return True

def validate_column(values):
    try:
        if values not in letters_to_numbers:
            print(
                f"{values}' is wrong! You should choose A, B, C, D, E, F or G"
                )
    except:
        print(f"Please try again! You should choose A, B, C, D, E, F or G \n")
        return False

    return True


def hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "x":
                count += 1
    return count

def validate_continue_game(values):
    try:
        if values not in continue_game_options:
            print(
                f" '{values}' is wrong! Please press 'ok' or 'end game'."
                )
    except:
        print(f" Try again. Please press 'ok' or 'end game'.\n")
        return False

    return True    
    


def play_game():
    turns = 10
    global player_score

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
        row, column = ship_location()
        if guess_board[row][column] == "-" or guess_board[row][column] == "x":
            print('_____________________________________________')
            print('_____________________________________________')
            print("Error! You have already guessed that place!")
            print('_____________________________________________')
            print('_____________________________________________')
        elif hidden_board[row][column] == "*":
            print('____________________________________________________')
            print('____________________________________________________')
            print(f" You hit a ship!")
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
        if hit_ships(guess_board) == 5:
            print('____________________________________________________')
            print('____________________________________________________')
            print(
                f"Congratulations {name}, "
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
            print(f"||  {name}'s SCORE: {player_score}   || "
                    f" COMPUTER'S SCORE: {computer_score}  ||")
            print('_____________________________________________')
            print('_____________________________________________')
        if turns == 0:
            print(
                f"You ran out of turns {name}, the game is over.")
            print('                ___________________________')
            print('               |       GAME OVER!          |')
            print('               | Thank you for plaing      |')
            print('                ___________________________\n') 
         
                
            break
        if hit_ships(player_board) == 5:
            print(
                f"The computer won!")
            print('                ___________________________')
            print('               |       GAME OVER!          |')
            print('               | Thank you for plaing      |')
            print('                ___________________________\n')  
            print('Press enter to restart')
                
            break
        if hit_ships(guess_board) < 5:
            continue_game = input(
                    "To continue press 'ok' otherwise press 'end game'. \n").lower()
            while continue_game not in continue_game:
                validate_continue_game(continue_game)
                continue_game = input(
                    "To continue press 'ok' otherwise press 'end game'. \n").lower()
                    
            if continue_game == "ok" or continue_game == "ok":
                print(
                    "You have decided to continue playing the game.")
                continue
            elif continue_game == "end game" or continue_game == "end game":
                print(
                    "You have decided to finish the game,"
                    "the game is now over.")
                break
            else:
                print("Please enter 'yes' or 'no'")
                continue_game = input(
                    "Do you want to continue playing? y/n \n")
def main_menu():
    start_game()
    play_game()


main_menu()