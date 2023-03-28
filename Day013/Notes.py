# External libraries...
#   Common imports...
import random as rnd
import pandas as pd
import numpy as np
import math
from datetime import date   # Only imports a specific function
from datetime import datetime

# print(dir(math))
# help(math)

# print(math.cos(math.pi/2))
# print(math.cos(math.pi/2.0))

#   initialie random
rnd.seed(5)

#   Get a randome range
# x = rnd.randrange(10)
# print(rnd.randrange(10))
# print(rnd.randrange(10))
# print(rnd.randrange(10))
# print(rnd.randrange(10))
# print(rnd.randrange(10))

# random choice...
people = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot"]
# print(rnd.choice(people))
# print(rnd.choice(people))
# print(rnd.choice(people))
# print(rnd.choice(people))
# print(rnd.choice(people))

#   shuffle...
print(people)
rnd.shuffle(people)# Re-orders the list...
print(people)

print(datetime.now())
print(date.today())