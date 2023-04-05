from random import randint


scores = {'computer': 0, 'player': 0}


# Board class adopted and modified from the CI's battleship tutorial
class Board:

    """
    Main board class. Sets board size, the number of ships,
     the player's name and the board type (player board or computer).
     Has methods for adding ships and guesses and printing the board
    """

    def __init__(self, size, number_of_ships, name, type):
        self.size = size
        self.board = [["_" for a in range(size)] for b in range(size)]
        self.number_of_ships = number_of_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print(self):
        # prints board
        for row in self.board:
            print("|_".join(row))

    def guess(self, a, b):
        # appends "X" at the chosen coordinates
        self.board[a][b] = "-"

        # appends "*" if chosen coordinates hits a target
        if (a, b) in self.ships:
            self.board[a][b] = "x"
            return "Hit"
        else:
            return "Miss"

    def add_ship(self, a, b, type="computer"):
        if len(self.ships) >= self.number_of_ships:
            print("Error: you cannot add any more ships!")
        else:
            self.ships.append((a, b))
            if self.type == "player":
                self.board[a][b] = "x"


    def random_point(size):
    
        """
        Helper function to return a random integer between o and size
        """
        return randint(0, size - 1)


    def validate_coordinates(a, b, board):
    
        """
        Function to validate coordinate inputs from users
        """
    
        try:
            a, b = int(a), int(b)
            board.board[a][b] in board.board
    
        except IndexError:
            print(f"This is incorrect!Please enter the row and column number between 0 - {board.size - 1}\n")
            return False
    
        except ValueError:
            print(f"This is incorrect! Please enter a number.\n")
            return False
    
        finally:
            if (a, b) in board.guesses:
                print("This field has already been entered before! Please enter another field.\n")
                return False
        return True


    def populate_board(board):
    
        """
        Function to add ships to the board's ships list
        """
    
        a = random_point(board.size)
        b = random_point(board.size)
        board.add_ship(a, b)


    def make_guess(board):
    
        """
        Function to get validated user guess and append it to the guesses list
        """
    
        while True:
            if board.type == "computer":
                a, b = random_point(board.size), random_point(board.size)
                if validate_coordinates(a, b, board):
                    board.guesses.append((a, b))
                    return a, b
                    break
    
            elif board.type == "player":
                a = input("Guess a row: ")
                b = input("Guess a column: ")
                if validate_coordinates(a, b, board):
                    board.guesses.append((a, b))
                    return a, b
                    break


    def scores_dashboard(board):
    
        """
        Prints the score dashboard status after each round
        """
    
        print("-" * 35)
        print("After this round, the scores are:")
        print(f"{board.name}: {scores['player']} Computer: {scores['computer']}")
        print("-" * 35)


    def print_board(computer_board, player_board):
    
        """
        Prints the player's board and the computer's board
        """
    
        print(f"{player_board.name}'s Board:")
        player_board.print()
        print()
        print("Computer's Board:")
        computer_board.print()
        print("-" * 35)


    def check_winner(scores, computer_board, player_board):
    
        """
        Function that checks the winner and displays the winning message
        """
    
        if scores["player"] == player_board.num_ships:
            print("GAME OVER!!")
            print(f"Well done {player_board.name}!! You are the Victor")
        elif scores['computer'] == player_board.number_of_ships:
            print("GAME OVER!!")
            print(f"Sorry, {player_board.name}!! You lost to the computer")


    def play_game(computer_board, player_board):
    
        """
        Main game function. Takes in the board instances as arguement
        and controls the game logic"""
    
        while True:
            # Get the player's guess and populate computer's board
            a, b = make_guess(player_board)
            a, b = int(a), int(b)
            player_board.guesses.append((a, b))
            print(f"Player guessed: {a, b}")
            if computer_board.guess(a, b) == "Hit":
                print("Player got a hit!")
                scores['player'] += 1
            elif computer_board.guess(a, b) == "Miss":
                print("Player missed this time")
    
            # Get computer's guess and populate player's board
            a, b = make_guess(computer_board)
            computer_board.guesses.append((a, b))
            print(f"Computer guessed: {a, b}")
            if player_board.guess(int(a), int(y)) == "Hit":
                print("Computer got a hit!")
                scores["computer"] += 1
            elif player_board.guess(a, b) == "Miss":
                print("Computer missed this time")
    
            scores_dashboard(player_board)
            print_board(computer_board, player_board)
            check_winner(scores, computer_board, player_board)
    
            # Get user's feedback to continue or to quit
            player_choice = input("Enter 'e' to quit, 'n' for new game and \
    any key to continue: ")
    
            if player_choice.lower() == "n":
                new_game()
            elif player_choice.lower() == "e":
                sys.exit("You have quit the game")


    def new_game():
    
        """
        Starts a new game. Sets the board size and number of ships, resets the
        scores and initialises the boards.
        """
    
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
        scores["computer"] = 0
        scores["player"] = 0
        print("-" * 37)
        print("Top left corner is row: 0, col: 0")
        print("-" * 37)
    
        # Get the player's name
        while True:
            player_name = input('Please input your name: ').capitalize()
            if player_name.isalpha():
                print()
                break
            else:
                print("Invalid entry: players name must be an alphabet")
    
        # Get board instances
        computer_board = Board(size, number_of_ships, "Computer", type="computer")
        player_board = Board(size, number_of_ships, player_name, type="player")
    
        # Append ships to the board instances
        for _ in range(number_of_ships):
            populate_board(player_board)
            populate_board(computer_board)
        print("-" * 35)
        print_board(computer_board, player_board)
        play_game(computer_board, player_board)
    
    
    new_game()

