####################################################################################################
#
#   Date Written: 03/22/2023        By: Joseph P. Merten
#   Day 10: Circle Challenge - Python OOP: Classes
#
####################################################################################################
#   imports
import pdb
import sys
import math

####################################################################################################
#   Classes
class Circle():
    def __init__(self, radius):
        self.radius = radius
    def calculate_diameter(self):
        return 2 * self.radius
    def calculate_circumference(self):
        return 2 * math.pi * self.radius
    def ç(self):
        return math.pi * self.radius * self.radius
    def grow(self):
        self.radius += 1
    def get_radius(self):
        return self.radius

####################################################################################################
#   Variables
grow_flag = 'y'

####################################################################################################
#   Functions
def input_radius():
    """This function will get a valid decimal number."""
    print("Welcome to the circle Tester")
    print("Enter a radius:")
    my_radius = -1
    while my_radius < 0:
        my_response = input("> ")
        try:
            my_radius = float(my_response)
            if my_radius < 0:
                print("Please enter a positive value.")
        except:
            print("Invaslid entry, please enter a floating point number...")
            my_radius = -1
    return my_radius

def output_values(my_circle):
    """This outputs our calculations for the circle."""
    print(f"Diameter: {my_circle.calculate_diameter()}")
    print(f"Circumference: {my_circle.calculate_circumference()}")
    print(f"Area: {my_circle.calculate_circumference()}")
def get_grow_flag(my_circle):
    "This determines if we want to grow the circle another unit larger."
    my_resp = 'x'
    while my_resp != 'n' and my_resp != 'y':
        my_resp = input("Would you like your circle to grow?\n > ")
    if my_resp == 'y':
        print("Stand by while your circle magically grows")
        my_circle.grow()
    elif my_resp == "n":
        print("Goodbye")
    else:
        print("Something is wrong...")
        return "n"
    return my_resp

####################################################################################################
#   Lambdas

####################################################################################################
#   Main code
g_circle = Circle(input_radius())
while grow_flag.lower() == 'y':
    output_values(g_circle)
    grow_flag = get_grow_flag(g_circle)

