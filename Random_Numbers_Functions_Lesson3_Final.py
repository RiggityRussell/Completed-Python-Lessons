#####################################
# Arlt Random Numbers Lesson 3 Final
# Originally Written by: David Hosler
# Expanded by: Russell Arlt
# CIT 112 - Lesson 3
#####################################
from random import *
import time
import sys

def get_number_of_tries():  # creating a funtion with the DEF keyword.
    num_tries = input(name + " how many tries would you like to find the number? ")  # asks for an input of a number for number of tries
    if num_tries != "0":  # Makes sure that the number isn't a zero, even though it is in a string form at the moment.
        try:  # looks to return an integer
            int(num_tries)  # will check the user input an integer
        except ValueError:  # if an integer wasn't input, it will instead run this code.
            print(f"{num_tries} is not a valid integer. Please try again.")  # prints out telling the user that what they entered was wrong.
            return get_number_of_tries()  # throws the user back into the top of the function.
    elif num_tries == "0": #checks to see if they input 0
        print("NO! Not zero!")  #Yells at the user for putting in a zero.
        return get_number_of_tries() #throws them back to the top of the function
    return int(num_tries) #returns the int num_tries out of the function

def user_guess():  # creating a funtion with the DEF keyword.
    guess = input("What number am I thinking of? ")  # asks for an input of a number for guessing
    try:  # looks to return an integer
        return int(guess)  # will return the integer that was input
    except ValueError:  # if an integer wasn't input, it will instead run this code.
        print(f"{guess} is not a valid integer dawg, come on now!")  # prints out telling the user that what they entered was wrong.
        return user_guess()  # throws the user back into the top of the function.

def play_moooore():  # a function that asks if user wants to play again
    zip = input("Would you like to try again? (Y/N): ").lower() #asks the user if they would like to play again
    if zip == "y": #if the user says yes
        guessed = True #guessed will still be true
        keep_playing = True #keep_playing will still be true
        return (guessed, keep_playing)
    elif zip != "y":
        print("You played " + str(game_tries) + " games!")
        print("See ya later!")
        sys.exit()

name = input("What should I call you? ")
if name == '':
    print("Fine, don't tell me. I'll just refer to you as Human.")
    name = 'Human'
keep_playing = True
game_tries = 0
while keep_playing is True:
    rand_number = randint(1, 100)
    try_num = 0
    high_low = ''
    guessed = False  # Tracks whether or not the user's guess was correct
    num_guesses = 0  # Counts how many guesses the user has made
    start_time = time.time()  # Records when the game starts
    num_tries = get_number_of_tries()  # number of tries is pulled from the function get_number_of_tries
    while guessed is False:
        guess = user_guess()
        num_guesses += 1
        if guess != rand_number:
            try_num += 1
            if num_tries == try_num:
                game_tries += 1
                print("Whoopsie Do! Couldn't get it in time!")
                print("The answer was: " + str(rand_number))
                (guessed, keep_playing) = play_moooore()

            elif guess > rand_number:
                high_low = 'lower'
                print("My number is " + high_low + " than your guess. ")
            elif guess < rand_number:
                high_low = 'higher'
                print("My number is " + high_low + " than your guess. ")
        else:
            print("You're right, " + name + ", that was my number!")
            game_tries += 1
            print("It took you " + str(num_guesses) + " to find my number.")
            guessed = True
            end_time = time.time()  # Records when the game ends
            print("It took you " + str(end_time - start_time) + " seconds to guess my number. ")
            print("you have played " + str(game_tries) + " games!")
            (guessed, keep_playing) = play_moooore()

# EOF