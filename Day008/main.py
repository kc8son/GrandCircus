####################################################################################################
#
#   Date Written: 03/15/2023        By: Joseph P. Merten
#   SHOPPING LIST  https://docs.google.com/document/d/1e0yQY40vEe_hl-2cksXmAFQSzxh8sHb_XWjpADHqmws/preview
#
####################################################################################################
#   imports
import pdb
import sys

####################################################################################################
#   Variables
menu_list = {
    "Tomatoes":     2.50,
    "Bread":        1.25,
    "Mushrooms":    5.79,
    "Cereal":       1.89,
    "Butter":       3.15,
    "Eggs":         2.10,
    "Lettuce":      1.35
}

####################################################################################################
#   functions
def print_menu():
    i = 1
    print("Today's menu:\nPlease make a selection or type 'checkout'")
    for key in menu_list.keys():
        print(f"{i} - {key} - ${menu_list[key]:.2f}")
        i += 1

def get_selection():
    resonse = input("> ")
    #   Test 1 - check for numeric entry
    if resonse.isnumeric() and 0<
    print(x)
    #   Test 2 - scan for the full name
    #   Test 3 - scan for partiao name.

####################################################################################################
#   lambdas

###################################################################################################
#   Main routine.
print_menu()
get_selection()