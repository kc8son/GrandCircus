####################################################################################################
#
#   Date Written: 03/02/2023        By: Joseph P. Merten
#   Day 3 - Powers Table
#
####################################################################################################
#   imports

#   variables
count = 1
continue_flag = 'y'

#   main routine
print("Learn your squares and cubes!\n")

####################################################################################################
#   Outer loop to request limit...
while (continue_flag.lower() == 'y'):
    limit = int(input("Enter an integer: "))
    print("""
    Number\tSquared\tCubed
    =======\t=======\t======""")
    ####################################################################################################
    #   inner loop to print each number & powers
    while (count <= limit):
        print(f"\t{count}\t\t{count**2}\t\t{count**3}")
        count+=1
    print("-"*100+"\n")
    ####################################################################################################
    #   Add a multiplication table
    print("Multiplication Table:\n----------------------")
    for i in range(limit):
        print(f"\t{i+1}", end="")
    print("")
    for i in range(limit):
        print(f"\t=", end="")
    print("")
    for i in range(limit):
        print(f"{i+1} |", end="")
        for j in range(limit):
            print(f"\t{(i+1)*(j+1)}", end="")
        print("")
    print("")
    count = 1
    continue_flag = input("\n\nContinue? (y/n): ")


