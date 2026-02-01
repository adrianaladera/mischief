import math
import numpy as np
from evaluate import Evaluate
from board import Board

def main():
    print("Hello! Welcome to Tic Tac Toe!")
    print("we are the bob unit")

    # try:
    #     user = str(input("Do you want to be X or O?\nI want to be: "))
    #     if user.upper() != 'O' and user.upper() != 'X':
    #         raise ValueError("Mcscuse me bonch that is not a valid option!")
    # except ValueError as e:
    #     print(f"Error: {e}. Please try again brother.")

    board = Board()
    chosen_positions = set()

    cunt = 0
    
    while Evaluate.evaluate(np.reshape(board.positions, (-1,3))) is not None and cunt < 9:
        print("RESHAPE THIS HOE")
        print(np.reshape(board.positions, (-1,3)))
        if cunt % 2 == 0:
            player = 'X'
        else:
            player = 'O'
        while new_pos := int(input(f"Player {player}, choose your next position! ")):
            if new_pos not in chosen_positions:
                break
        print(player, cunt)
        board.add_position(new_pos, player)
        board.print_board()
    
        cunt += 1
    
    if Evaluate.evaluate(np.reshape(board.positions, (-1,3))) is None:
        print("There is a draw!")
    else:
        print(f"{Evaluate.evaluate(np.reshape(board.positions, (-1,3)))} won the game!")
    
if __name__=="__main__":
    main()