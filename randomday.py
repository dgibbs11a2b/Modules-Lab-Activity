#----------------------------------------
#David Gibbs
#February 21, 2020
#
#This program uses the random.choice module to select a random
#day from the list of 7 days in a week. it will then display
#the randomly selected day to the screen
#----------------------------------------
import random

days_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#Here I've defined all seven days in the week
day_selection = random.choice(days_week)
#I've assigned "day_selection" to the random.choice module and asked it
#to choose a day of the week from the list of available days.
print ("The randomly selected day from the list of days is", day_selection)
#This will print the randomly selected day to the screen
