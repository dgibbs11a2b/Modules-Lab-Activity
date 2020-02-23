#----------------------------------------
#David Gibbs
#February 22, 2020
#
#This program allows you to convert radians to degrees. It receives your input
#and will then echo your input and display the calculated value
#----------------------------------------

import math

pi=22/7
#This is the best approximation representing pi
radian = float(input("Please enter the radians to calculate: "))
#This receives floating input from the user as radians to calculate
degree = radian*(180/pi)
#This calculates the degrees my first dividing pi by 180 and then multiplying
#it by the radian input
print ("You entered", radian)
#This echos the user's input
print("The calculated value from radian to degrees is", degree)
#This displays the the calculated value to the screen
