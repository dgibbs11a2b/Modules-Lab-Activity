#----------------------------------------
#David Gibbs
#February 21, 2020
#
#This program computes the approximation of pi using the math module.
#It uses series addition and uses a for loop to count from 1 to 10 million
#in steps of 4. Each time through the for loop, two operations will occur.
#----------------------------------------
import math

pi = 0.0

for i in range(1, 10000000,4):
    pi += 4/i
#The addition operation of pi +4 / 1   
    pi -= 4/(i+2)
#The subtraction operation pi -4 /1+2 (or 3)
#Each time through the loop, it will increment i by 4 and continue
#Your approach can be simlified.  You can also just use pi= 355 / 113
print(pi)
#executes the for loop operation and displays it to the screen

print(math.pi)
#print's the value of pi from the math module for comparison
