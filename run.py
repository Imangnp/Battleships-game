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
    def print_grid(self):
        # Print boards with player and opponent lable
        print(f"\n{self.name}'s battlefield:\n")
        print("    0  1  2  3  4")
        print("  +----------------+")
        for row in range(BOARD_SIZE):
            print(row, end = " | ")
            for column in range(len(self.grid[row])):
                current_value = self.grid[row][column]
                
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

        # if the player's input is missed
        if self.grid[guess.row][guess.column] == '-':
            print(f"{guess.striker} missed This time.")
            self.grid[guess.row][guess.column] = 'X'
            return False
        return False

    def check_if_winner(self):
        if self.ship_counter == 0:
            return True
        return False


class Game:

    def __init__(self):
        pass
        
    def start(self):

        player = Board("Player")
        computer = Board("Computer")
        # Initializes player's board
        player.init_board()
        player.print_grid()
        # Initializes  opponent's board
        computer.init_board()
        computer.print_grid()
        # Start the game
        is_player_turn = True
        while True:
            if is_player_turn:
                # Ask player to input Coordinates
                while True:
                    try:
                        row_input = int(input("Guess a row:\n "))
                        column_input = int(input("Guess a column:\n "))
                        print("=======================")
                        if row_input not in range(BOARD_SIZE) or column_input not in range(BOARD_SIZE):
                            raise ValueError
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number between 0 and 4.")
                player_guess = Guess(row=row_input,
                                     column=column_input,
                                     striker=("Player"))
                if computer.add_guess_to_grid(player_guess):
                    has_player_won = True
                    break
                is_player_turn = False
            else:
                # Computer makes a guess
                row_input = random.randint(0, BOARD_SIZE - 1)
                column_input = random.randint(0, BOARD_SIZE - 1)
                computer_guess = Guess(row=row_input,
                                       column=column_input,
                                       striker=OPPONENT_NAME)
                if player.add_guess_to_grid(computer_guess):
                    has_computer_won = True
                    break
                is_player_turn = True
            player.print_grid()
            computer.print_grid()
        if has_player_won:
            print("Player wins!")
        elif has_computer_won:
            print("Computer wins!")
    

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()
