from random import randint


def main_menu():
    print('WELCOME TO BATTLESHIP GAME \n')
print('_______________________________________________________________________')
print('_______________________________________________________________________')
print('    Hello and Welcome to Battleshipgame!')
print('_______________________________________________________________________')
print('_______________________________________________________________________')

print('\n')
print('                 /||\ ')
print('                / ||_\  ')  
print('               /  ||__\  ')
print('              /   ||___\  ')
print('             /    ||____\  ')
print('            /     ||_____\  ')
print('           /      ||______\  ')
print('          /       ||_______\  ')  
print('         /        ||        \   ')
print('       _/_________||_________\________ ')
print('       \_____________________________/      ')
print('        \___________________________/  ')
print('         \_________________________/   \n')
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
print('                  \ // ///  /////   /////  // /')
print('                   \                         / ')
print('                    \_______________________/ ')
print('                                                  \n')
print('                      /                             ')
print('                     / |                                  ')
print('                    /  |\                                ')
print('           _______ /  /| \                              ')
print('          /______//  / |  \                       ')
print('         /______//  /  |   /\                         ')
print('                /  /   | //  \                          ')
print('               /  /    ///    \           ')
print('              /  /   ////      \              ')
print('             /  /  /////        \                        ')
print('            /  / ///// |         \  ')
print('           /  //////// |          \  ')
print('          /  //_/_/_/  |          |   ')
print('         /  //_/_/_/   |           |   ')
print('     ___/__/___| |__\__|_________/  ')
print('     \__________________________/  ')
print('      \________________________/    ')
print('       \______________________/  ')
print('                                             \n')
name = input('Please, enter your name: ')
print('Hello', name + '!')
input('Press Enter to continue')


print('__________________________________________________________________________')
print('__________________________________________________________________________')
print('           BATTLESHIP GAME                ')
print('__________________________________________________________________________')
print('__________________________________________________________________________')

print('      ______________________________________________________')
print('     |           WELCOME TO MY GAME CALLED BATTLESHIP!      |')
print('     |                                                      |')
print('     |  You have 5 ships and you can freely place them on   |')
print('     |  your board. To do this, you have to decide which    |')
print('     | column (marked with the letters A-J) and row (marked |')
print('     |with the numbers 1-10) you will place them. Afterwards|')
print("     | you need to guess the computer's ships placed on a   |")
print('     | another game board.                                  |')
print('      ______________________________________________________' )

main_menu()
#Board for holding ship locations
USER_BOARD = [["__"] * 10 for x in range(10)]
# Board for displaying hits and misses
COMPUTER_BOARD = [["__"] * 10 for i in range(10)]

def print_board(board):
    print("    A    B    C    D    E    F    G    H    I   J   ")
    print(" |____|____|____|____|____|____|____|____|____|__|")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "__|".join(row)))
        row_number += 1

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
#computer create 5 ships
def create_ships(board):
    for ship in range(9):
        ship_row, ship_column = randint(0,9), randint(0,9)
        while board[ship_row][ship_column] == "_X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "_X"

def get_ship_location():
    row = input("Enter the row of the ship (1-10): ").upper()
    while row not in "12345678910":
        print('Not an appropriate choice, please select a valid row')
        row = input("Enter the row of the ship (1-10): ").upper()
    column = input("Enter the column of the ship (A-J):  ").upper()
    while column not in "ABCDEFGHIJ":
        print('Not an appropriate choice, please select a valid column')
        column = input("Enter the column of the ship (A-J): ").upper()
    return int(row) - 1, letters_to_numbers[column]

#check if all ships are hit
def number_hit_ships(board):
    number = 0
    for row in board:
        for column in row:
            if column == "X":
                number += 1
    return number

if __name__ == "__main__":
    create_ships(USER_BOARD)
    trials = 9
    while trials > 0:
        print('Guess a battleship location')
        print_board(COMPUTER_BOARD)
        row, column = get_ship_location()
        if COMPUTER_BOARD[row][column] == "_¤":
            print("You guessed that one already.")
        elif USER_BOARD[row][column] == "_X":
            print("Hit")
            COMPUTER_BOARD[row][column] = "_X" 
            trials-= 1  
        else:
            print("MISS!")
            COMPUTER_BOARD[row][column] = "_¤"   
            trials -= 1     
        if number_hit_ships(COMPUTER_BOARD) == 9:
            print("You win!")
            break
        print("You have " + str(trials) + " trials left")
        if trials == 0:
            print("You ran out of trials. GAME OVER")
            print('GAME OVER!')
print('                ___________________________')
print('               |       GAME OVER!          |')
print('               | Thank you for plaing      |')
print('                ___________________________\n')
print('                      ((  (( ))  ))  ')
print('                   (((( ( (    )) ))      ')
print('                  ((/   ( (     ))|) ))     ')
print('                 (( | _  \/  _  \/| )) ))    ')
print('                ))  | 0      0    |  ))((    ')
print('                ))) )     _      / (((( ))    ')
print('               ((  ( (    __    /((((((((     ')
print('                (( ) )  \ ___ / )) ))((\/     ')
print('                \/ \/ ( ( |  |  )) \/((       ')
print('                       \/ |  |      \/    ') 
               
            