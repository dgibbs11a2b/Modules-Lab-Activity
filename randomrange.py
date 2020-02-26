#----------------------------------------
#David Gibbs
#February 21, 2020
#
#This program uses the random module to generate ten
#random integers between the values 25 and 35.
#----------------------------------------

import random
#imports the random module

for x in range(10):
#assigns the loop variable to "n"
#Set the limit to 36 so that 35 would get included in random integer range.
  print (random.randrange(25,35))
#prints random integers between 25 and 35 to the screen
