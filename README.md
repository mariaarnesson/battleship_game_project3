# BATTLESHIP GAME PROJECT 3

![responsive](assets/image/responsive.png)
![game](assets/image/game.png)

# Table of content

- [Introduction](#introduction)
- [User Experience (UX)](#user-experience-ux)
    - [User Stories](#user-stories)
- [How to play](#how-to-play)
- [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#future-features)
 - [Designe](#designe)
 - [Testing](#testing)
 - [Deployment](#deployment)
 - [Credits](#Credits)


# Introduction
[View the live project here](https://battleship-game.herokuapp.com/)

This Battleships game is Portfolio Project 3 - Python Essentials created for Diploma in Full Stack Software Development at [Code Institute](https://codeinstitute.net/se/) . This project is about building a command-line application that allows users to manage a common dataset about a particular domain.

Battleship game is a Python Terminal Game, which runs in Heroku. 

The Battleships game is played on grids on which each player's fleet of battleships are marked. The locations of the fleets are concealed from the other player. Players call shots at the other player's ships, and the objective of the game is to destroy the opposing player's fleet.
The application provides a working battleships game for a single user to play against the computer. 
The game is played on a 9 x 9 board.
A player's ships are already placed on the board when the game starts. Useful information is displayed to help the user progress through the game. The first board at the top displays the current player's ship placement and guesses, and the bottom board shows their own guess history.

The winner is the one who sinks all the enemy ships first!

# User Experience (UX)
## User Stories:
- as a user I want to be welcomed by a start screen with name of the game.
- as a user i want the computer to create boards with ships hidden for me.

- as a user I want the board to be visible to me so I can see which ships are hits and which are misses. 

- as a user, I want to see the game board so I can see my hits and misses.

- as a user, I want to see both boards so I can see everything I need to play.

- as a user, I want to see whose turn it is so I know when it's my turn.

- as a user, I want to know who won.

# How to play 

After pressing on run the game, entering the user's name, the user can see the game instructions and a table showing the size of the ships. After placing the ships on game board, the user guesses where the ships are on the computer board. The game ends when the computer or the user guesses where all the ships are.

Battleship game is a version of the classic [Battleship game](https://en.wikipedia.org/wiki/Battleship_(game)) game of the same name. This implementation allows for a single player match (human vs computer).

# Features
## Existing Features

- Introductory text and drawing after starting the game:
![features_01](assets/image/features_01.png)

- Start text where the user is asked to enter user's name.
![features_03](assets/image/features_03.png)

- Further text where the loading is displayed. 
![features_04](assets/image/features_04.png)

- Introduction with game instructions.
![features_05](assets/image/features_05.png)

- the user game board and the computer game board are displayed.
![features_07](assets/image/features_07.png)
![features_08](assets/image/features_08.png)

- The user has is to guess where the ships are located on the computer board.
![features_11](assets/image/features_11.png)

- Error-checking:
![features_12](assets/image/features_12.png)
![features_13](assets/image/features_13.png)

- Game Over Message
![features_14](assets/image/features_14.png)





In this game a player have access to two game boards. First, the player have to place the ships on a game board. And afterwords shuold guess where the ships are placed on the opponent's game board. 

![board-game](assets/image/game-board.png) ![game_board](assets/image/game-board_1.png)



Guessed ships are marked with an '★'.The game ends when all the ships have been guessed.
## Future Features
- add size for ships

# Designe
- Flow Charts

The diagram below shows the structure of the functions presented in the run.py file:

![flowcharts](assets/image/flow_charts.png)

# Testing

Testing information can be found in separate [testing.md](TESTING.md) file

# Deployment

- This program was deployed to Heroku. The steps to deploy are as follows:
    - Login to Heroku
    - In the Heroku, select: Create new app
    - Enter name of the app
    - Enter region of the app
    - Navigate to the Settings tab.
    - In 'Config Vars' select 'PORT' as a key to and '8000' as a value
    - In 'Buildpacks' select 'Add buildpack' and choose python and nodejs.
    - From the tab on the top, select: Deploy.
    - Afrerword select Github and connect.
    - Enter the respository name on Github and select: Search
    - Click connect button.
    - In Manual deploy, select the 'Deploy Branch' option
    - Select 'Open app' on the right hand side of the screen
    - The app should appear in a new tab on the web browser
    - The live link can be found here - https://battleship-game.herokuapp.com/
# Credits
- [Pexel- ships at the sea](https://images.pexels.com/photos/445363/pexels-photo-445363.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1) - A image from this page was used to the background. 

- [Python Value Error](https://www.digitalocean.com/community/tutorials/python-valueerror-exception-handling-examples) - this page was used to write python code to value error.

- [Project 3 Teplate](https://github.com/Code-Institute-Org/python-essentials-template)- this template for Python was used.
- [PEP8](https://pep8ci.herokuapp.com/#) - this page was used for checking my code for PEP8 requirements
- (https://www.freepik.com/free-vector/vector-cartoon-pirate-ship-water-sand-beach-bay_4393922.htm#query=battleship&position=3&from_view=search&track=sph)




