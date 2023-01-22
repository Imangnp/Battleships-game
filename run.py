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
    
    # def add_guess_to_grid(self):

    # def valutate_guess(self):


class Game:

    def __init__(self):
        pass
        
    def start(self):
        player_board = Board("Player")
        player_board.init_board()
        player_board.print_grid()

        computer_board = Board("Computer")
        computer_board.init_board()
        computer_board.print_grid()

        is_player_turn = True
        has_player_won = False
        has_computer_won = False
        while True:
            if is_player_turn:
                # Ask player to input Coordinates
                while True:
                    row_input = input("Guess a row:\n ")
                    column_input = input("Guess a column:\n ")
                    print("=======================")

                    player_guess = Guess(row=row_input,
                                         column=column_input,
                                         striker=player_name)

    # def validate_input(self):

    

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()
