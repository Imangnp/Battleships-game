import random

# Global variable
NUMBER_OF_SHIPS = 4
BOARD_SIZE = 5
OPPONENT_NAME = "Computer"
player_score = 0
computer_score = 0


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

    # def init_board(self):
    
    # def add_guess_to_grid(self, guess: Guess) -> bool:

    # def valutate_guess(self):


class Game:

    def __init__(self):
        pass
        
    def start(self):
        player_board = Board("Player")
       
        player_board.print_grid()

        computer_board = Board("Computer")
       
        computer_board.print_grid()

    # def validate_input(self):

    

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()
