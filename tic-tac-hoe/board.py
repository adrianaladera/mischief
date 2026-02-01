from enum import Enum
from numpy import array

class PositionState(str, Enum):
    EMPTY = " "
    X = "X"
    O = "O"


class Board:

    def __init__(self):
        self.positions = array([" " for _ in range(9)])
        print("Select a position in the grid on your turn")
        self.print_board(state=[i for i in range(9)])

    def add_position(self, new_position: int, player: str):
        self.positions[new_position] = player
        
    def print_board(self, state=None):
        print("\x1b[4m{}|{}|{}\n\x1b[0m\x1b[4m{}|{}|{}\n\x1b[0m{}|{}|{}".format(*state or self.positions))

board = Board()
board.print_board()