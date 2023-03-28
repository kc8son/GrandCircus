####################################################################################################
#
#   Date Written: 03/27/2023        By: Joseph P. Merten
#   Day 13:
#
####################################################################################################
#   imports
import pdb
import sys
import math

####################################################################################################
#   Variables

####################################################################################################
#   Functions

####################################################################################################
#   Classes
class Validator():
####################################################################################################
#
#   Date Written: 03/22/2023        By: Joseph P. Merten
#   Day 10: Circle Challenge - Python OOP: Classes
#
#   Date Modified: 03/23/2023       By: Joseph P. Merten
#   Added a validator class for the extended challenge.
#
####################################################################################################
#   imports
import pdb
import sys
import math

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

####################################################################################################
#   Lambdas

####################################################################################################
#   Main code
print("Welcome to the circle Tester")
# g_circle = Circle(input_radius())
g_circle = Circle(Validator.validate_radius())
while grow_flag.lower() == 'y':
    output_values(g_circle)
    # grow_flag = get_grow_flag(g_circle)
    grow_flag = Validator.validate_yn()
    if grow_flag == 'y':
        print("Stand by while your circle magically grows")
        g_circle.grow()
    else:
        print(f"The last radius of your circle was: {g_circle.get_radius()}")
        print("Goodbye")
