#####################################
# RandomNumber.py
# Written by: David Hosler
# CIT 112 - Lesson 1
#####################################

#####################################
# Assignment instructions
#   Find each instance of REPLACE_ME in the
#   code below, and replace it with
#   appropriate variable names
#####################################
from random import *
import time

rand_number = randint( 1, 100 )
name = input( "What should I call you? " )
if name == '':
    print( "Fine, don't tell me. I'll just refer to you as Human." )
    name = 'Human'

high_low = ''
guessed = False # Tracks whether or not the user's guess was correct
num_guesses = 0 # Counts how many guesses the user has made
start_time = time.time() # Records when the game starts

while guessed is False:
    guess = int( input( "What number am I thinking of? " ) )
    num_guesses += 1
    if guess != rand_number:
        if guess > rand_number:
            high_low = 'lower'
        else:
            high_low = 'higher'
        print( "My number is " + high_low + " than your guess. ")
    else:
        print( "You're right, " + name + ", that was my number!" )
        print( "It took you " + str( num_guesses ) + " to find my number." )
        guessed = True
        end_time = time.time() # Records when the game ends
        print( "It took you " + str( end_time - start_time ) + " seconds to guess my number. " )

#EOF