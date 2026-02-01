import numpy as np
# from enum import Enum

class Evaluate:
    def evaluate(positions: np.array):
        #To-Do: CASES DONT ALWAYS WORK, CODE BREAKS, DOESN'T WHEN WINNER IS FOUND
        '''Checks to see if there is a winner for the
        tic-tac-toe game. Evaluates all rows, columns, 
        the diagonal, and antidiagonal, and if a winner is 
        in any of those, then returns the winning character
        ('X' or 'O'). If not, then returns None.'''

        # check rows and columns    
         
        # row_mask = np.all(positions == positions[:, [0]], axis=1)
        # col_mask = np.all(positions == positions[0,:], axis = 0)
        row_mask = np.all(positions == 'X', axis=1)
        col_mask = np.all(positions == 'X', axis = 0)
        row_mask = np.all(positions == 'O', axis=1)
        col_mask = np.all(positions == 'O', axis = 0)

        row_win = np.where(row_mask)[0]
        col_win = np.where(col_mask)[0]

        # check diagonal elements
        diag = len(np.unique(np.diag(positions))) == 1
        antidiag = len(np.unique(np.diag(np.fliplr(positions)))) == 1

        print(row_win, col_win, diag, antidiag)

        if diag == True or antidiag == True:
            return positions[1][1]
        elif len(row_win) != 0:
            return positions[row_win][0]
        elif len(col_win) != 0:
            return positions[0][col_win]
        elif np.char.isalpha(positions): # if the board is full and no winner
            return 'D'
        else:
            return None


ass = np.array([['X', 'O', 'X'],
                ['X', 'X', 'X'],
                ['X', 'O', 'O']])

# print(Evaluate.evaluate(ass))