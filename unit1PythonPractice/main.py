####################################################################################################
#
#   Date Written: 02/05/2023        By: Joseph P. Merten
#   Grand Circus Unit 1
#   This script is part of the pre-work for the Grand Circus Data Analytics & Engineering bootcamp
#   Unit URL:
#       https://docs.google.com/document/d/1Vx8NI_IKaZ5xqEOCesHTdrCO1-wqnsxNRZfovsmNlQQ/edit#
#
####################################################################################################
#   imports
import math

####################################################################################################
#   main code
print("Hello console!")

my_name = 'Joe Merten'
work_from_home = True
side = 15
radius = 10

print("My name is: "+my_name)                                       #   string concatenation
print("I work from home:", str(work_from_home))                     #   str function
print("The length of each side of the square:  {}".format(side))    #   .format method
print(f"The radius of the circle: {radius}")                        #   formatted string literal

square_area = side**2
square_perimeter = 4 * side
circle_area = math.pi * radius**2
circle_perimeter = math.pi * 2 * radius

print(f"The square area is: {square_area} and the perimeter is: {square_perimeter}.")
print(f"The circle area is: {circle_area} and the perimeter is: {circle_perimeter}.")
print("\n"*3)

####################################################################################################
#   Step 5: List of Travel Options
print("Step 5: List of Travel Options")
travel_options = ["foot", "bike", "car", "airplane"]
print(f"1) {travel_options[0]}")
print(f"2) {travel_options[1]}")
print(f"3) {travel_options[2]}")
print(f"4) {travel_options[3]}")

travel_type = input("How would you like to travel? ")

distance = 100
time = 0
cost = 0

if travel_type == "foot":
   print("Walking is free! Speed is 3mph.")
   cost = 0
   time = distance / 3
elif travel_type == "bike":
   rent_bike = input("Do you need to rent the bike? (yes or no) ")
   if rent_bike == "yes":
       print("Bike rental is $45! Speed is 10mph")
       cost = 45
   else:
       print("Biking is free! Speed is 10mph.")
       cost = 0
   time = distance / 10
elif travel_type == "car":
   print("Driving is $0.25/mi. Speed is 60mph.")
   cost = 0.25 * distance
   time = distance / 60
elif travel_type == "airplane":
   print("Flying is $0.10/mi. Speed is 400mph.")
   passenger_count = int(input("How many passengers? "))
   cost = 0.10 * distance * passenger_count
   time = distance / 400
else:
   print(f"Sorry. {travel_type} is an invalid option.")
print(f"Traveling {distance} miles by {travel_type} took {time} hours and cost ${cost}")

####################################################################################################
#   Step 9: Visualize Time and Cost
cost_bar = "Cost: "
time_bar = "Time: "
for i in range(math.ceil(cost)):
    cost_bar += "$"
for i in range(math.ceil(time)):
    time_bar += "/"
print(cost_bar)
print(time_bar)

