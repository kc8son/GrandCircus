####################################################################################################
#
#   Date Written: 03/06/2023        By: Joseph P. Merten
#   Day 4 - Heating & Cooling
#
####################################################################################################
#   imports

####################################################################################################
#   variables
actual_temp = 94
desired_temp = 71
window = 2
default_run_time = 3


####################################################################################################
#
def run_furnace(run_time, actual_temp):
    """This function will run the furnace for the specified number of minutes to raise the temperature"""
    print(f"Running furnace for {run_time} minutes")
    return actual_temp + 3

def run_ac(run_time, actual_temp):
    """his function will run the ac for the specified number of minutes to lower the temperature"""
    print(f"Running ac for {run_time} minutes")
    return actual_temp - 3

####################################################################################################
#   main routine
#   We want to allow a window as specified in the window variable.  This will
#   define our comfort window.  I.E. the number of degrees above or below our desired_temp
#   before we start the heat or ac.
for i in range(9):
    print(f"Current temp = {actual_temp}, desired temp = {desired_temp}")
    if actual_temp < desired_temp - window:
        actual_temp = run_furnace(default_run_time, actual_temp)
    elif actual_temp > desired_temp + window:
        actual_temp = run_ac(default_run_time, actual_temp)
    else:
        print("within target range...")
    print(f"Current temp = {actual_temp}, desired temp = {desired_temp}")
    print("-"*100)