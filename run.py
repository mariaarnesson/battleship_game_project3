import random

def main_menu():
    print('WELCOME TO BATTLESHIP GAME \n')

print('_______________________________________________')
print('    Hello and welcome to Battleshipgame!')
print('_______________________________________________')

print('\n')
print('                 /|| ')
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





#create a game board

board = [
    ['_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_'],
]

letters_to_numbers = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6}


def create_ships():

    column = input('Please, choose some letter between A-G: ')
    while column not in 'ABCDEFG':
        print('Incorrect! You should choose A, B, C, D, E, F or G')
        column = input('Please, choose a letter between A-G')

    row = input('Please, choose the row 1-7 of the ship: ')  
    while row not in '1234567':
        print('Incorrect! You should choose 1, 2, 3, 4, 5, 6 or 7')
        row = input('Please, choose a letter between 1-7')  

    return int(row) -1, letters_to_numbers[column]    

def print_board(board): 
    print('||A|B|C|D|E|F|G')  

    row_number = 1
    for row in board:
        print('%d|%s|' % (row_number, '|'.join(row)))

        row_number = row_number + 1

# loop for 5 ships
for n in range(5):
    print('PLEASE, PLACE THE SHIP ', n + 1, 'ON YOUR GAME-BOARD ')
    row_number, column_number = create_ships() 

    if board[row_number][column_number] == 'X':
        print('There is already a ship in this place!')

        board[row_number][column_number] = 'X'
        print_board(board)

# the other one game-board 
guesses_board = [
    ['_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_'],

]   

guesses = 0
while guesses < 5:
    print('Guess locations of the ships')
    row_number, column_number = create_ships()

    if guesses_board[row_number][column_number] != '_':
        print('You have already guessed that place!')
        continue

    if board[row_number][column_number] == 'X':
        print('HIT!')
        guesses_board[row_number][column_number] ='X'
        guesses = guesses + 1
    else:
        guesses_board[row_number][column_number] = '.'
        print("MISS!")    
    

    print_board(guesses_board)        






