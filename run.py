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
