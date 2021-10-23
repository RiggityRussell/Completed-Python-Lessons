#Rock Paper Scissors Game
#Russell Arlt
#CIT 112

#This allows a randomized choice to be used.
import random
import sys

#Setting the variables to increase after wins/loses/ties.
tie_score = 0
player_score = 0
computer_score = 0

#the while statement will keep the user inside the game until the statement is False, or we hit a break/quit point.
while True:

#The beginning of the game.
    print("\nRock Paper Scissors Game! Type a choice to begin, or type quit to leave!")
#computer choices locks in what the computer can choose from.
    computer_choices = ("rock", "paper", "scissors")
#player choices locks in what the user can type, and diffrentiates so I'm not typing user choice, user choices.
    player_choices = ("rock", "paper", "scissors", "quit")
#Users input below.
    user_choice = input("\n").lower()
#This doesnt allow the user to type anything other than what is in player choices without being told to try again.
#Originally I tried a != 'rock' or 'paper' or 'scissors'. that did not work.
    while user_choice not in player_choices:
    #This restates the question, and at the end makes whatever the user types lowercase. learned the hard way its not tolower.
        print("\nWhoops! Looks like you need a refresher. Please type rock, paper, or scissors: ")
        user_choice = input("\n").lower()
#This lets the user leave the game.
    if user_choice == ('quit'):
        print("\nThanks for playing!")
        #shows the scores that were incrementally increased, or not if no games were played.
        #converted the scores to a string so they could be put with other strings.
        print("\nYour score is: " + str(player_score))
        print("\nComputers score is: " + str(computer_score))
        print("\nThere were " + str(tie_score) + " ties!")
        #quits the app.
        sys.exit()
#this calls the computer choice to randomize its options from rock, paper, and scissors.
    computer_choice = random.choice(computer_choices)
#if/else if statements that determine tie, wins, or loses.
#starts with if the player and computer are equal
    if user_choice == computer_choice:
        print("\nYour choice is " + user_choice)
        print("\nThe computers choice is " + computer_choice)
        print("\nyou tied!")
        #adding to the tie score
        tie_score += 1
#if the player and computer and not equal it checks it against the next variables.
    elif user_choice == 'rock':
        if computer_choice == 'paper':
            print("\nYour choice is " + user_choice)
            print("\nThe computers choice is " + computer_choice)
            print("\nYou lost! Oh no!")
            #adding to the computer score
            computer_score += 1
        elif computer_choice == 'scissors':
            print("\nYour choice is " + user_choice)
            # took a leap of faith that \n works in python as well. It does!
            print("\nThe computers choice is " + computer_choice)
            print("\nYou won! Hooray!")
            #adding to player score.
            player_score += 1
    elif user_choice == 'paper':
        if computer_choice == 'rock':
            print("\nYour choice is " + user_choice)
            print("\nThe computers choice is " + computer_choice)
            print("\nYou won! Hooray!")
            player_score += 1
        elif computer_choice == "scissors":
            print("\nYour choice is " + user_choice)
            print("\nThe computers choice is " + computer_choice)
            print("\nYou lost! Oh no!")
            computer_score += 1
    elif user_choice == 'scissors':
        if computer_choice == 'rock':
            print("\nYour choice is " + user_choice)
            print("\nThe computers choice is " + computer_choice)
            print("\nYou lost! Oh no!")
            computer_score += 1
        elif computer_choice =='paper':
            print("\nYour choice is " + user_choice)
            print("\nThe computers choice is " + computer_choice)
            print("\nYou won! Hooray!")
            player_score += 1

#here is where we restart the while loop, or break out from the while loop to quit the game.
    play_again = input("\nWould you like to play again? (Yes/No): ").lower()

    if play_again !="yes":
        print("\nThanks for playing!")
        print("\nYour score is: " + str(player_score))
        print("\nComputers score is: " + str(computer_score))
        print("\nThere were " + str(tie_score) + " ties!")
        sys.exit()

#Below is a random scattering of things I tried that did not work out, or became obsolete.
#if user_choice != ('rock' or 'paper' or' scissors' or 'quit'):
    #print("THATS WRONG!")
#random_choice = random.choice(list(rock, paper, scissors))
#Prints both mine and the computers choices.
    #print("Your choice is " + user_choice)
    #print("\nThe computers choice is " + computer_choice)

"""
#I went and learned how to create functions, not well though, to cut down on copy/paste and typing.
#I could not get the win, lose, tie, variables to go up when I used these though.
#defining the function, calling it user_win, and within it is what will be printed anytime the player wins.
def user_win():
    print("\nYour choice is " + user_choice)
    #took a leap of faith that \n works in python as well. It does!
    print("\nThe computers choice is " + computer_choice)
    print("\nYou won! Hooray!")
#defining the function, calling it comp_win, and within it is what will be printed anytime the computer wins.
def comp_win():
    print("\nYour choice is " + user_choice)
    print("\nThe computers choice is " + computer_choice)
    print("\nYou lost! Oh no!")
"""