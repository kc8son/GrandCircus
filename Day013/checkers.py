####################################################################################################
#
#   Date Written: 03/27/2023        By: Joseph P. Merten
#   Day 13:Checkers Game - Imports and NumPy Intro
#
####################################################################################################
#   imports...
# from numpy import empty
import numpy as np


#   Functions
def build_board(board_size):
    """This function will build a 2 dimensional board of the specified size."""
    my_board = np.random.choice(["Red", "Black", "Empty"], (board_size, board_size))
    return my_board

def get_count(my_board):
    """This function will count how many positions for each color there are."""
    cell_counts = {}
    for row in my_board:
        for cell in row:
            if cell in cell_counts:
                cell_counts[cell] += 1
            else:
                cell_counts[cell] = 1
    return cell_counts

####################################################################################################
#   Main
if __name__ == "__main__":
   print("This file is not intended to be run.  It is only to be used as a library...")
