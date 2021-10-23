#####################################
# Arlt Random Numbers
# Russell Arlt
# CIT 112 - Lesson 3 - Funky Functions
#####################################
from random import *
import time
import sys

def get_number_of_tries(): #creating a funtion with the DEF keyword.
    num_tries = input(name + " how many tries would you like to find the number? ") #asks for an input of a number
    try: #looks to return an integer
        return int(num_tries) #will return the integer that was input
    except ValueError: #if an integer wasn't input, it will instead run this code.
        print(f"{num_tries} is not a valid integer. Please try again.")#prints out telling the user that what they entered was wrong.
        return get_number_of_tries() #throws the user back into the top of the function.


name = input( "What should I call you? " )
if name == '':
    print( "You entered NOTHING! Now I will call you User" )
    name = 'User'

keep_playing = True
game_tries = 0
while keep_playing is True:
    rand_number = randint( 1, 100 )
    try_num = 0
    high_low = ''
    guessed = False # Tracks whether or not the user's guess was correct
    num_guesses = 0 # Counts how many guesses the user has made
    start_time = time.time() # Records when the game starts
    get_number_of_tries()

def numbercheck_wrong():
        try_num += 1
        if num_tries == try_num:
            game_tries += 1
            print("Whoopsie Do! Couldn't get it in time!")
            print("The answer was: " + str(rand_number))
            zip = input("Would you like to try again? (Y/N): ").lower()
            if zip == "y":
                guessed = True
                keep_playing = True
            elif zip != "y":
                print("You played " + str(game_tries) + " games!")
                print("See ya later!")
                keep_playing = False
                sys.exit()

        elif guess > rand_number:
            high_low = 'lower'
            print("My number is " + high_low + " than your guess. ")
        elif guess < rand_number:
            high_low = 'higher'
            print("My number is " + high_low + " than your guess. ")
def numbercheck_right():
        print("You're right, " + name + ", that was my number!")
        game_tries += 1
        print("It took you " + str(num_guesses) + " to find my number.")
        guessed = True
        end_time = time.time()  # Records when the game ends
        print("It took you " + str(end_time - start_time) + " seconds to guess my number. ")
        print("you have played " + str(game_tries) + " games!")
        zap = input("Would you like to try again? (Y/N): ").lower()
        if zap == "y":
            keep_playing = True
        elif zap != "y":
            print("You played " + str(game_tries) + " games!")
            print("See ya later!")
            keep_playing = False
#EOF