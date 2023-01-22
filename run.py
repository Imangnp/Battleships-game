import random

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
            print(row, end = " | ")
            for column in range(len(self.grid[row])):
                current_value = self.grid[row][column]
                # Masks Computer's ships
                if current_value == "@" and mask_ships:
                    print("-", end="  ")
                else:
                    print(current_value, end = "  ")
            print("| ")
        print("  +----------------+\n")

    # Randomly creating coordinates for ships
    def init_board(self):
        while self.ship_counter < NUMBER_OF_SHIPS:
            x = random.randint(0, NUMBER_OF_SHIPS)
            y = random.randint(0, NUMBER_OF_SHIPS)
            if self.grid[x][y] != '@':
                self.grid[x][y] = '@'
                self.ship_counter += 1
    
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


    def is_game_finished(self) -> bool:
        if self.ship_counter == 0:
            return True
        return False

class Game:

    def __init__(self):
        self.guesses = {OPPONENT_NAME: []}
        
    def start(self):
        # Ask the player for a username
        player_name = input("Please enter your username:\n")
        self.guesses[player_name] = []
        player = Board(player_name)
        computer = Board(OPPONENT_NAME)
        # Initializes player's board
        player.init_board()
        player.print_grid(False)
        # Initializes  opponent's board
        computer.init_board()
        computer.print_grid(False)
        # Start the game
        is_player_turn = True
        has_player_won = False
        has_computer_won = False
        while True:
            if is_player_turn:
                # Ask player to input Coordinates
                while True:
                    row_input = int(input("Guess a row:\n "))
                    column_input = int(input("Guess a column:\n "))
                    print("=======================")

                    player_guess = Guess(row=row_input,
                                         column=column_input,
                                         striker=player_name)
                    # Verify if the guess is valid
                    if player_guess not in self.guesses.get(player_name):
                        is_player_turn = False
                        self.guesses.get(player_name).append(player_guess)
                        # Verify if the guess hit a ship.
                        has_player_won = computer.add_guess_to_grid(
                                        guess=player_guess)
                        break
                    else:
                        print("Guess already taken, please take a new guess!")
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
                if computer_guess not in self.guesses.get(player_name):
                    is_player_turn = True
                    # Verify if the guess hit a ship by add guess to the grid.
                    has_computer_won = player.add_guess_to_grid(
                                        guess=computer_guess)

                    print(f"\n{player.name}'s Score: ",
                          NUMBER_OF_SHIPS - computer.ship_counter)
                    print("Computer's Score: ",
                          NUMBER_OF_SHIPS - player.ship_counter)
                    print("=======================\n")
                    break
                else:
                    continue

            player.print_grid(False)
            computer.print_grid(True)

            if has_player_won:
                print(f"Game over!\n{player_name} won the game!")
                exit(0)
            elif has_computer_won:
                print(f"Game over!\n\n{OPPONENT_NAME} won the game!")
                exit(0)

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()
