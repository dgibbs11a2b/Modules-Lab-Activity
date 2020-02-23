#----------------------------------------
#David Gibbs
#February 23, 2020
#
#This program receives input from the user as a positive integer
#It will then calculate the factorial of this input value.
#----------------------------------------
import math


number = int(input("Give me a non-negative integer: "))
#Receives input from user as a positive integer
factorial = 1
#assigns variable "factorial" to the number 1 

for i in range(number):
	factorial = factorial * (i+1)
#iterative takes factorial and mulitplies the value of i and increments by 1
print("The factorial of the number you gave me,",number,"is",factorial)
#Displays the factorial of the number entered to the screen
