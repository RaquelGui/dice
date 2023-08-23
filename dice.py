#dice.py

# importing module
import random 

#definition of function dice
def dice():
    return random.randint(1,6)

#input
start = input("Do you want to roll the dice? (y/n) ")

while True:
    
    if start == "y":
        print("The number is: ", dice())
    
    elif start == "n":
        print("Ok. Let's play later.")
        break #Finish the game

    else:
        print("Thanks for playing.")

    repeat = input("Do you want to roll the dice again? (y/n) ")
    if repeat != "y":
        print ("Thanks for playing.")
        break  # Finish the game