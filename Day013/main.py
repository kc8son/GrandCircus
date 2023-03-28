####################################################################################################
#
#   Date Written: 03/27/2023        By: Joseph P. Merten
#   Day 13:Checkers Game - Imports and NumPy Intro
#
####################################################################################################
#   imports
import pdb
import sys
import math
import checkers

####################################################################################################
#   Variables
board_size = 0

####################################################################################################
#   Functions

####################################################################################################
#   Classes
class Validator():
    def validate_yn():
        "This METHOD determines if we want to grow the circle larger."
        my_resp = 'x'
        while my_resp != 'n' and my_resp != 'y':
            my_resp = input("Would you like your circle to grow?\n> ")
            if my_resp != 'n' and my_resp != 'y':
                print("Invalid response, please enter 'y' or 'n'...")
        return my_resp
    def validate_int(my_prompt, min, max):
        """This method will display a message and validate that the response is an
        integer within the boundaries specified by min & max"""
        my_resp = min - 5   #force untrue...
        while not min <= my_resp <= max:
            print(my_prompt)
            my_resp = input()
            try:
                my_resp = int(my_resp)
            except:
                my_resp = min - 5
            if not min <= my_resp <= max:
                print("Invalid entry, pleae try again...")
        return my_resp

####################################################################################################
#   Lambdas

####################################################################################################
#   Main code
print("Welcome to GC checkers...")
board_size = int(Validator.validate_int("Please enter a board size betwee 2 and 64", 2, 64))
checker_board = checkers.build_board(board_size)
print(checker_board)
g_counts = checkers.get_count(checker_board) # checkers.get_count(checker_board):
print(g_counts)
