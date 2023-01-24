# Battleships-game
The Battleship game is the third Portfolio project for Diploma in Full Stack Software Development at Code Institute.
This is a digital version, written int Python, of the well known board game Battleship. The scope of the game is to input coordinates in order to hit the enemies ships until one of the players successfully strikes all of the opponent’s ships. 

You can find the live link here: [Battleships-game](https://battleships-game.herokuapp.com/)

![Responsive](./assets/images/Screenshot-respansive.png)

___

# Table of Contents

- [Overview](#Overview)
    * [Project](#Project) 
    * [How to play](#how-to-play)
 - [Features](#features) 
    * [Start screen](#start-screen) 
    * [Game Boards](#game-boards)
    * [score](#score)  
    * [The End](#end) 
    * [Future Scope](#future-scope)   
- [Testing](#testing)
    * [Validator Testing](#validator-testing)
- [Deployment](#deployment)
- [Technologies](#technologies) 
- [Bugs](#bugs)
- [Credits](#credits)

---

# Overview
  ## Project
  The game starts with a welcoming introduction and explanation of the rules.
  In this case, the game board is represented by a 5x5 grid where '-' represents an empty cell, '@' represents a ship, '$' represents a hit, and 'X' representsa miss.
  The player don’t need to select where to allocate the ships, as they are randomly assigned.

  The user is asked to enter the name before the game can start. 

  When the game starts, the player is presented with their new board on which the ships are indicated with the symbol “@“ . The computer’s board, on the other hand, only displays blank spaces .The objective of the game is to strategically select the cell that might contain the opponent’s ships. 
  To select the cell, the user must input the coordinates by indicating a row number and a column number. 

  If the ship has been successfully hit by one of the players it will be indicated with the symbol “ $”, otherwise it will be marked with an “X”. 
  The game concludes when one player sinks all of the opponent ships. 

  ## How to play
  In this version the player competes against the computer. Each player has a game board with ships placed randomly. The player attempts to guess the coordinates of the computer’s ships by inputting numbers between 0 and 4 for rows and columns.


# Features
  ## Start screen
    ### Greeting
    ### How to play
    ### Input Username

  ![Start screen]()

  ## Game Boards
    ### Computer's battlefield
    ### Players's battlefield
    ### Guess a row
    ### Guess a column

  ![Boards]()

  ## score
    ### Players score

  ![Scores]()

  ## The End
    ### The winner
    ### Input if to restart

  ![The End]()

  ## Future Scope
    ### Choose the board size
    ### Choose the number of ships
    ### Choose the player number


# Testing
  ## Validator Testing

  ![Validator](./assets/images/Screenshot-validator.png)

# Deployment

# Technologies

# Bugs

# Credits

[Back to Top](#)

---

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)