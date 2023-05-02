
# we can multiply the time in hours by 0.5, since he drinks 0.5 litres of water per hour of cycling. 
# Then we can round down the result to the nearest integer, since Nathan can only drink a whole number of litres.


import math

def calculate_liters(time_in_hours):
    liters = time_in_hours * 0.5
    return math.floor(liters)

# The math.floor() method rounds a number DOWN to the nearest integer, if necessary, and returns the result.


# we'll call the calculate_liters function with the time in hours as its argument to get the number of litres Nathan will drink,

# rounded to the nearest integer

print(calculate_liters(3))   # Output: 1
print(calculate_liters(6.7)) # Output: 3
print(calculate_liters(11.8))# Output: 5

