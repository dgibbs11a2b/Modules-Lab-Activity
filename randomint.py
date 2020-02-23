#----------------------------------------
#David Gibbs
#February 21, 2020
#
#This program uses the random module to generate a random
#odd integer to the screen between the values 0 and 100.
#The first is my primary example and then I've offered
#a secondary example.
#----------------------------------------

import random   

#imports the random module
random_odd_integer = random.randrange(1, 100, 2)
#generates a random odd number from a range of 0 to 100 starting with
#1 as the odd number in the range
print(random_odd_integer)
#displays the random odd number to the screen
#I could only get this to work by using "1" as my starting range value.


random_odd_integer = (random.randint(0,100)) * 2 + 1
print(random_odd_integer)
#This is an alternative method to using the above code which will also
#generate an odd number to the screen.
#Here I used "0" as my starting range value
