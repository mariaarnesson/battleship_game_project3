import random

def main_menu():

main_menu()

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

letters_to_numbers = {
    'A' = 0,
    'B' = 1,
    'C' = 2,
    'D' = 3,
    'E' = 4,
    'F' = 5,
    'G' = 6
}



def create_ships():

    column = input('Please, choose some letter between A-G: ')
    while column not in 'ABCDEFG':
        print('Incorrect! You should choose A, B, C, D, E, F or G')
        column = input('Please, choose a letter between A-G')

    row = input('Please, choose the row 1-7 of the ship')  
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
    print('Please, place the ship ', n + 1, 'on you game-board ')
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
    else 
        guesses_board[row_number][column_number] = 'o'
        print('MISS!')

    print_board(guesses_board)        






