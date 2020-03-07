
"""
Created on Tue Jul  15 2019

@author: Shahab Bangash
"""
epsilon = 0.0001
print("Enter root you want to find for a number. e.g 2 for squareroot and so on")
root = int(input("Root: "))
value = int(input("Now Enter any number to find it's root "))
tries = 0
guess = 1
while(abs(guess*guess-value)>epsilon):
    guess = ((root-1)*guess)/root + value/(root*(guess**(root-1)))
    tries+=1
print("Total tries it took: " + str(tries))
print("Answer: " + str(guess))
