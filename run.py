import random
import os

# Global variable
NUMBER_OF_SHIPS = 4
BOARD_SIZE = 5
OPPONENT_NAME = "Computer"
player_score = 0
computer_score = 0


# Holds information about a players guess in a row and column and player's name
class Guess:
    def __init__(self, row: int, column: int, striker: str):
        self.row = row
        self.column = column
        self.striker = striker

    # compares two Guess objects
    def __eq__(self, other):
        return (self.row == other.row and
                self.column == other.column and
                self.striker == other.striker)


# This class creates two boards for player and computer with
# randomly placed ships and empty spaces.
# It checks if player's input are numbers and valid to been verify.
# It also verifys if coordinates input by players hit a ship or is missed.
class Board:

    def __init__(self, name: str):
        self.grid = [['-' for _ in range(BOARD_SIZE)]
                     for _ in range(BOARD_SIZE)]
        self.name = name
        self.ship_counter = 0

    # Create the boards for player and opponent
    def print_grid(self, mask_ships=True):
        # Print boards with player and opponent lable
        print(f"\n{self.name}'s battlefield:\n")
        print("    0  1  2  3  4")
        print("  +----------------+")
        for row in range(BOARD_SIZE):
            print(row, end=" | ")
            for column in range(len(self.grid[row])):
                current_value = self.grid[row][column]
                # Masks Computer's ships
                if current_value == "@" and mask_ships:
                    print("-", end="  ")
                else:
                    print(current_value, end="  ")
            print("| ")
        print("  +----------------+\n")

    # Randomly creating coordinates for ships
    def init_board(self):
        while self.ship_counter < NUMBER_OF_SHIPS:
            x = random.randint(0, BOARD_SIZE-1)
            y = random.randint(0, BOARD_SIZE-1)
            if self.grid[x][y] != '@':
                self.grid[x][y] = '@'
                self.ship_counter += 1

    # takes input and checks if it hits a ship, updates the grid,
    # and returns a boolean indicating whether the game has ended.
    def add_guess_to_grid(self, guess: Guess) -> bool:

        # if the player's input hit a ship
        if self.grid[guess.row][guess.column] == '@':
            print(f"{guess.striker} hit a target!")
            self.grid[guess.row][guess.column] = '$'
            self.ship_counter -= 1

            # Announce the end of the game
            if self.is_game_finished():
                return True
            return False

        # if the player's input is missed
        if self.grid[guess.row][guess.column] == '-':
            print(f"{guess.striker} missed This time.")
            self.grid[guess.row][guess.column] = 'X'
            return False
        return False

    # Returns true if there are no ships left on the board,
    # indicating the game is over.
    def is_game_finished(self) -> bool:
        if self.ship_counter == 0:
            return True
        return False


# This class runs the game by printing menu to the console and
# letting the player to enter inputs such as username and coordinates.
# It also prints the crated boards for player and computer.
class Game:

    # Stores the guesses made by the player and the computer.
    def __init__(self, player_name: str) -> None:
        self.player_name = player_name
        self.guesses = {OPPONENT_NAME: []}


    def start(self) -> Bool:
        # clear the console
        os.system('clear')
        self.guesses[self.player_name] = []
    
        player = Board(self.player_name)
        os.system('clear')
        computer = Board(OPPONENT_NAME)
        # Initializes player's board
        player.init_board()
        player.print_grid(False)
        # Initializes  opponent's board
        computer.init_board()
        computer.print_grid(False)
        
        # Start the game
        is_player_turn = True

        while True:
            if is_player_turn:
                # Ask player to input Coordinates
                while True:
                    row_input = take_valid_input("Guess a row:\n ")
                    column_input = take_valid_input("Guess a column:\n ")
                    print("============================")

                    player_guess = Guess(row=row_input,
                                         column=column_input,
                                         striker=self.player_name)
                    # Verify if the guess is valid
                    if player_guess not in self.guesses.get(self.player_name):
                        is_player_turn = False

                        # Add the guess to the list of guesses for the player
                        self.guesses.get(self.player_name).append(player_guess)

                         # Verify if the guess hit a ship.
                        has_player_won = computer.add_guess_to_grid(
                                        guess=player_guess)

                        if has_player_won:
                            print(f"Game over!\n\n{self.player_name} won the game!")
                            self.__show_score(first=player, second=computer)
                        break # Break from the input guess validation

                    else:
                        print("Guess already taken, please guess again!")
                        continue

            # Computer generates random coordinates for its guess
            # by calling random.randint() method twice.
            while True:
                row_input = random.randint(0, BOARD_SIZE - 1)
                column_input = random.randint(0, BOARD_SIZE - 1)
                computer_guess = Guess(row=row_input,
                                       column=column_input,
                                       striker=OPPONENT_NAME)
                # Verify if the guess is valid
                if computer_guess not in self.guesses.get(OPPONENT_NAME):
                    # Add the guess to the list of guesses for computer
                    self.guesses.get(OPPONENT_NAME).append(computer_guess)
                    is_player_turn = True
                    # Verify if the guess hit a ship by add guess to the grid.
                    has_computer_won = player.add_guess_to_grid(
                                        guess=computer_guess)

                    if has_computer_won:
                        print(f"Game over!\n\n{OPPONENT_NAME} won the game!")
                        self.__show_score(first=player, second=computer)
                    # print(f"\n{player.name}'s Score: ",
                    #       NUMBER_OF_SHIPS - computer.ship_counter)
                    # print("Computer's Score: ",
                    #       NUMBER_OF_SHIPS - player.ship_counter)
                    # print("============================\n")
                    break
                else:
                    continue

            # Showing the score after each loop cycle
            self.__show_score(first=player, second=computer)
           
            player.print_grid(False)
            computer.print_grid(True)

    # Verify if the player's input is valid between 0 and BOARD_SIZE-1
    def __take_valid_input(self, msg):
        while True:
            try:
                str_input = input(msg)
                int_input = int(str_input)
                if int_input < 0 or int_input >= BOARD_SIZE:
                    raise ValueError("Please enter a number between 0 and 4!")
                return int_input
            except ValueError:
                print("Please enter a number between 0 and 4!")

    def __show_score(self, first: Board, second: Board):
            # in each cycle, every player's score is equal to the number of the ships that the other player has lost
            print(f"\n{first.name}'s Score: ", NUMBER_OF_SHIPS - second.ship_counter)
            print(f"\n{second.name}'s Score: ", NUMBER_OF_SHIPS - first.ship_counter)
            print("============================\n")

# Welcome message for the game and information about the game's rules
def display_welcome_msg():
    print(
            """
█▄▄ ▄▀█ ▀█▀ ▀█▀ █░░ █▀▀ █▀ █░█ █ █▀█ █▀
█▄█ █▀█ ░█░ ░█░ █▄▄ ██▄ ▄█ █▀█ █ █▀▀ ▄█\n
        """
        )
        # greeting
        print("==========================================================")
        print("Welcome to the Battleships game")
        print(f"Board Size: {BOARD_SIZE}. Number of ships: {NUMBER_OF_SHIPS}")
        print("Coordinates: Numbers betwen 0 and 4 for rows and columns")
        print("How to play:")
        print("""In this version of Battleship, the player competes against
the computer. Each player has a game board with ships placed
randomly. The player attempts to guess the coordinates of
the computer's ships by inputting numbers between 0 and 4
for the rows and columns.""")
        print("==========================================================\n")   



def main():
    display_welcome_msg()
    game = Game()
    game.start()


if __name__ == "__main__":
    main()
