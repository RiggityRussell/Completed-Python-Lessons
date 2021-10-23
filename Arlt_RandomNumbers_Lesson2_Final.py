#####################################
# Arlt Random Numbers Lesson 2 Final
# Originally Written by: David Hosler
# Expanded by: Russell Arlt
# CIT 112 - Lesson 2
#####################################
from random import *
import time
import sys


name = input( "What should I call you? " )
if name == '':
    print( "Fine, don't tell me. I'll just refer to you as Human." )
    name = 'Human'
keep_playing = True
game_tries = 0
while keep_playing is True:
    rand_number = randint( 1, 100 )
    try_num = 0
    high_low = ''
    guessed = False # Tracks whether or not the user's guess was correct
    num_guesses = 0 # Counts how many guesses the user has made
    start_time = time.time() # Records when the game starts
    print(name + " how many tries would you like to find the number?")
    num_tries = int(input())
    while guessed is False:
        guess = int( input( "What number am I thinking of? " ) )
        num_guesses += 1
        if guess != rand_number:
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
                print( "My number is " + high_low + " than your guess. ")
        else:
            print( "You're right, " + name + ", that was my number!" )
            game_tries += 1
            print( "It took you " + str( num_guesses ) + " to find my number." )
            guessed = True
            end_time = time.time() # Records when the game ends
            print( "It took you " + str( end_time - start_time ) + " seconds to guess my number. " )
            print("you have played " + str(game_tries) + " games!")
            zap = input("Would you like to try again? (Y/N): ").lower()
            if zap == "y":
                keep_playing = True
            elif zap != "y":
                print("You played " + str(game_tries) + " games!")
                print("See ya later!")
                keep_playing = False

#EOF