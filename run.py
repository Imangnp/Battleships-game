import random
import os

# Global variable
NUMBER_OF_SHIPS = 4
BOARD_SIZE = 5
OPPONENT_NAME = "Computer"
player_score = 0
computer_score = 0


# Holds information about players guess in rows and columns and player's name
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


class Board:
    """
    This class creates two boards for player and computer with
    randomly placed ships and empty spaces.
    It displays the results of inputted coordinates by printing
    "hit($)" or "miss(X)" on the game boards.
    Once all of the ships on the board have been hit, the game will end.
    """

    def __init__(self, name: str):
        self.grid = [['-' for _ in range(BOARD_SIZE)]
                     for _ in range(BOARD_SIZE)]
        self.name = name
        self.ship_counter = 0

    # Create the boards for player and opponent
    def print_grid(self, mask_ships=True):
        # Print boards with player and opponent lable
        print(f"{self.name}'s battlefield:")
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

    # Takes input and checks if it hits a ship, updates the grid,
    # and returns a boolean indicating whether the game has ended.
    def add_guess_to_grid(self, guess: Guess) -> bool:

        # If the player's input hit a ship add $ to the choosen coordinate
        if self.grid[guess.row][guess.column] == '@':
            print(f"{guess.striker} hit a target!")
            self.grid[guess.row][guess.column] = '$'
            self.ship_counter -= 1

            # Announce the end of the game
            if self.is_game_finished():
                return True
            return False

        # If the player's input is missed add X to the choosen coordinate
        if self.grid[guess.row][guess.column] == '-':
            print(f"{guess.striker} missed This time.")
            self.grid[guess.row][guess.column] = 'X'
            return False
        return False

    # Returns true if there are no ships left on the board.
    def is_game_finished(self) -> bool:
        if self.ship_counter == 0:
            return True
        return False


class Game:
    """
    This class manages the flow of the game, allows the player to enter inputs.
    It checks if input coordinates by players hit the target or not
    and updates scores.
    It also give restart option to player.
    """

    def __init__(self, player_name: str) -> None:
        # Stores the guesses made by the player and the computer.
        self.player_name = player_name
        self.guesses = {OPPONENT_NAME: []}

    def start(self):
        # To restart the game
        self.__reset()
        self.guesses[self.player_name] = []
        player = Board(self.player_name)
        os.system('clear')
        computer = Board(OPPONENT_NAME)
        # Initializes player's board
        player.init_board()
        player.print_grid(False)
        # Initializes  opponent's board
        computer.init_board()
        computer.print_grid(True)

        # Start the game
        is_player_turn = True

        while True:
            if is_player_turn:
                # Ask player to input Coordinates
                while True:
                    row_input = self.__take_valid_input("Guess a row: ")
                    column_input = self.__take_valid_input("Guess a column: ")
                    print("============================")

                    player_guess = Guess(row=row_input,
                                         column=column_input,
                                         striker=self.player_name)
                    # Verify if the guess is valid
                    if player_guess not in self.guesses.get(self.player_name):
                        is_player_turn = False

                        # Add the guess to the list of guesses for the player
                        self.guesses.get(self.player_name).append(player_guess)

                        # Verify if guess hit a ship by adding guess to th grid
                        has_player_won = computer.add_guess_to_grid(
                                        guess=player_guess)

                        if has_player_won:
                            print(f"\n\nGame over!")
                            print(f"{self.player_name} is the winner!")
                            self.__show_score(first=player, second=computer)
                            return self.__show_game_exit_menu()
                        break  # Break from the input guess validation

                    else:
                        print("Guess already taken, please guess again!")
                        continue

            '''
            Computer generates random coordinates for its guesses
            by calling random.randint() method twice.
            '''
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
                    # Verify if guess hit a ship by adding guess to the grid
                    has_computer_won = player.add_guess_to_grid(
                                        guess=computer_guess)

                    if has_computer_won:
                        print(f"\n\nGAME OVER!")
                        print(f"{self.player_name} is the winner!")
                        self.__show_score(first=player, second=computer)
                        return self.__show_game_exit_menu()
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
        '''
        In each cycle, every player's score is equal to
        the number of the ships that the other player has lost
        '''
        print(
            f"\n{first.name}'s Score: ", NUMBER_OF_SHIPS - second.ship_counter)
        print(f"{second.name}'s Score: ", NUMBER_OF_SHIPS - first.ship_counter)
        print("============================\n")

    # Give option to the player to exit or restart the game when it is over
    def __show_game_exit_menu(self):
        while True:
            play_again = input("Do you want to play again? (yes/y or no/n)\n")
            if play_again.lower() in ["yes", "y"]:
                return True
            elif play_again.lower() in ["no", "n"]:
                return False
            else:
                print("Invalid input. Please enter (yes/y or no/n)")
                continue

    def __reset(self):
        self.guesses = {OPPONENT_NAME: []}


# Welcome message for the game and information about the game's rules
def display_welcome_msg():
    print(
            """
█▄▄ ▄▀█ ▀█▀ ▀█▀ █░░ █▀▀ █▀ █░█ █ █▀█ █▀
█▄█ █▀█ ░█░ ░█░ █▄▄ ██▄ ▄█ █▀█ █ █▀▀ ▄█
        """
        )
    # greeting
    print("==========================================================")
    print("Welcome to the Battleships game")
    print(f"Board Size: {BOARD_SIZE}. Number of ships: {NUMBER_OF_SHIPS}")
    print("Coordinates: Numbers betwen 0 and 4 for rows and columns")
    print("\nHow to play:")
    print("""In this version of Battleship, the player competes against
the computer. Each player has a game board with ships placed
randomly. The player attempts to guess the coordinates of
the computer's ships by inputting numbers between 0 and 4
for the rows and columns.""")
    print("==========================================================\n")


# Prompted player for a username and added validation to ensure input.
def validate_user_name() -> str:
    while True:
        user_input = input("Please enter your username:\n")
        if user_input:
            return user_input
        else:
            print("User input can not be empty!")
            continue


# To organize and call other functions
def main():
    # Clear the console
    os.system('clear')
    # Run the introduction page and how to play
    display_welcome_msg()
    # Ask the player for a username
    player_name = validate_user_name()
    # Run the game
    game = Game(player_name)
    while game.start():
        continue
    # Message of the end of the game
    print(f"\n\n{player_name}, thanks for playing my wonderful game!!!")


if __name__ == "__main__":
    main()
