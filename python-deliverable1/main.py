####################################################################################################
#
#   Date Written: 02/06/2023        By: Joseph P. Merten
#   Grand Circus Unit 1
#   This script is part of the pre-work for the Grand Circus Data Analytics & Engineering bootcamp
#   Project 1: Mini Golf Score Tracker
#   Unit URL:
#       https://docs.google.com/document/d/1XeYHRVBLj-j78Kc-raPog683L1plueNCtfm3O0FauUY/preview#heading=h.kokqlnfwub7b
#
#   Assignment:  Using PyCharm, build a Python program that tallies up your round of mini golf
#   and prints a message at the end with your total par.  This project is worth 10 points.
#   You must score a minimum of 8 points.
#
####################################################################################################
#   imports
import math

####################################################################################################
#   main code
player_name = input("Welcome to GC mini golf! What is your name? \n")

####################################################################################################
#   Get number of holes to play: 3 or 6, compute total_course_par and initialize cumulative_score
hole_count = 0
while hole_count != 3 and hole_count != 6:
    hole_count = int(input(f"Hi, {player_name}! Would you like to play 3 or 6 holes?\n"))
total_course_par = 3 * hole_count
cumulative_score = 0

####################################################################################################
#  Play the specified number of holes.
for i in range(hole_count):
    strokes = int(input(f"How many putts for hole {i+1}? (par: 3) \n"))
    cumulative_score += strokes

####################################################################################################
#  Print the player's results
total_score = cumulative_score - total_course_par
if total_score == 0:
    print(f"Good game, {player_name}. Your total score was: 0.")
elif total_score > 0:
    print(f"Nice try, {player_name}. Your total score was: +({total_score}).")
else:
    print(f"Great job, {player_name}. Your total score was: -({total_score*-1}).")
print("")   #   extra print() for criteria #5

