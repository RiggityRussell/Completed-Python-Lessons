##########################
#Rock Paper Scissors Game#
#Russell Arlt            #
#Lesson 3 - Final Draft  #
#CIT 112                 #
##########################
import random #This allows a randomized choice to be used.
import sys

tie_score = 0 # Setting the variables to increase after wins/loses/ties.
player_score = 0 # Setting the variables to increase after wins/loses/ties.
computer_score = 0 # Setting the variables to increase after wins/loses/ties.

def user_win(player_score): # function created to be called when the player wins, also increments the players score, and returns that value.
    print("\nYour choice is " + user_choice) #prints out the users choice
    print("\nThe computers choice is " + computer_choice) #prints out the computers choice
    print("\nYou won! Hooray!") #Celebrate!
    player_score += 1 # adding to player score.
    return player_score #returning player_score being incremented to the function, which will be called below.

def comp_win(computer_score): # function created to be called when the comp wins, also increments the comp score, and returns that value.
    print("\nYour choice is " + user_choice) #prints out the users choice
    print("\nThe computers choice is " + computer_choice) #prints out the computers choice
    print("\nYou lost! Oh no!") #Sad noises.
    computer_score += 1   #adding to the computer score
    return computer_score #returning computer_score being incremented to the function, which will be called below.

def whistle_blow(): #whistle blow means its quitting time!
    print("\nThanks for playing!")
    print("\nYour score is: " + str(player_score)) # shows the scores that were incrementally increased, or not if no games were played.
    print("\nComputers score is: " + str(computer_score))  # converted the scores to a string so they could be put with other strings.
    print("\nThere were " + str(tie_score) + " ties!")
    sys.exit() #exits the app

while True: #the while statement will keep the user inside the game until the statement is False, or we hit a break/quit point.
    print("\nRock Paper Scissors Game! Type a choice to begin, or type quit to leave!") #The beginning of the game.
    computer_choices = ("rock", "paper", "scissors") #computer choices locks in what the computer can choose from.
    player_choices = ("rock", "paper", "scissors", "quit") #player choices locks in what the user can type, and diffrentiates so I'm not typing user choice, user choices.
    user_choice = input("\n").lower() #Users input.
    while user_choice not in player_choices: #A different type of exception handling than what we normally do.
        print("\nWhoops! Looks like you need a refresher. Please type rock, paper, or scissors: ") #This restates the question, and at the end makes whatever the user types lowercase.
        user_choice = input("\n").lower()
    if user_choice == ('quit'): #This lets the user leave the game.
        whistle_blow() #goes to the function to quit the game.
    computer_choice = random.choice(computer_choices) #this calls the computer choice to randomize its options from rock, paper, and scissors.
    if user_choice == computer_choice: #if/else if statements that determine tie, wins, or loses.
        print("\nYour choice is " + user_choice) #starts with if the player and computer are equal
        print("\nThe computers choice is " + computer_choice)
        print("\nyou tied!") #didn't make a function for tie as it is only used once.
        tie_score += 1 #adding to the tie score
    elif user_choice == 'rock': #if the player and computer and not equal it checks it against the next variables.
        if computer_choice == 'paper':
            computer_score = comp_win(computer_score)  #here we call the function created at the top, comp_win
        elif computer_choice == 'scissors':
            player_score = user_win(player_score) #here we call the other function, user_win.
    elif user_choice == 'paper':
        if computer_choice == 'rock':
            player_score = user_win(player_score)
        elif computer_choice == "scissors":
            computer_score = comp_win(computer_score)
    elif user_choice == 'scissors':
        if computer_choice == 'rock':
            computer_score = comp_win(computer_score)
        elif computer_choice =='paper':
            player_score = user_win(player_score)
    play_again = input("\nWould you like to play again? (Yes/No): ").lower() #here is where we restart the while loop, or break out from the while loop to quit the game.
    if play_again !="yes":
        whistle_blow()
