'''
Scissors cuts paper.
Paper covers rock.
Rock crushes lizard.
Lizard poisons Spock.
Scissors decapitates lizard.
Lizard eats paper.
Spock smashes scissors.
Paper disapproves Spock.
Spock vaporizes rock.
Rock crushes scissors.

Created by Russell Arlt
Idea stolen from roshambo.com
CIT 112 David Hosler
'''

import random #This allows the computer to pick from random numbers or lists.
import sys #This allows the computer to access system code.

tie_score = 0 #Setting the variables to increase after wins/loses/ties.
player_score = 0
computer_score = 0

def user_win(player_score): # function created to be called when the player wins, also increments the players score, and returns that value.
    print("\nYour choice is " + userChoice) #prints out the users choice
    print("\nThe computers choice is " + computerChoices) #prints out the computers choice
    print("\nYou won! Hooray!") #Celebrate!
    player_score += 1 # adding to player score.
    return player_score #returning player_score being incremented to the function, which will be called below.

def comp_win(computer_score): # function created to be called when the comp wins, also increments the comp score, and returns that value.
    print("\nYour choice is " + userChoice) #prints out the users choice
    print("\nThe computers choice is " + computerChoices) #prints out the computers choice
    print("\nYou lost! Oh no!") #Sad noises.
    computer_score += 1   #adding to the computer score
    return computer_score #returning computer_score being incremented to the function, which will be called below.

def whistle_blow(): #whistle blow means its quitting time!
    print("\nThanks for playing!")
    print("\nYour score is: " + str(player_score)) # shows the scores that were incrementally increased, or not if no games were played.
    print("\nComputers score is: " + str(computer_score))  # converted the scores to a string so they could be put with other strings.
    print("\nThere were " + str(tie_score) + " ties!")
    sys.exit() #exits the app

print("A variation on Rock paper scissors! Rock, Paper, Scissors, Lizard, Spock!")
print("You've already played Rock, Paper, Scissors, and this is just an expanded version of that!")
print("Heres the rules!")
print("Scissor cuts paper.\nPaper covers rock.\nRock crushes lizard.\nLizard poisons Spock.\nScissors decapitates lizard.")
print("Lizard eats paper.\nSpock smashes scissors.\nPaper disapproves Spock.\nSpock vaporizes rock.\nRock crushes scissors.\n")
userName = input("Tell me your name friend: ")
print("Ok " + userName + " lets play!!")

while True: #This will keep the game repeating until we hit a sys.exit() which will exit the game.
    userChoice = input("\nType a choice to begin- Rock, Paper, Scissors, Lizard, Spock, or quit to leave: ").lower() #takes the Users choice
    computerChoice = ("rock", "paper", "scissors", "spock", "lizard") # A list of computers choices
    playerChoices = ("rock", "paper", "scissors", "lizard" , "spock", "quit")# locks in what the user can type.
    while userChoice not in playerChoices: #here we force the user to enter a loop if they don't enter a correct variable.
        print("\nWhoops! Looks like you need a refresher. Please type rock, paper, scissors, lizard, or spock: ")
        userChoice = input("\n").lower()
    if userChoice == ('quit'):
        whistle_blow()
    computerChoices = random.choice(computerChoice) # this calls the computer choice to randomize its options from rock, paper, and scissors.
    if userChoice == computerChoices: #if/else if statements that determine tie, wins, loss, or nothing.
        print("\nYour choice is " + userChoice)
        print("\nThe computers choice is " + computerChoices)
        print("\nyou tied!")
        tie_score += 1 #adding to the tie score
    elif userChoice == 'rock':
        if computerChoices == 'paper':
            computer_score = comp_win(computer_score)
        elif computerChoices == 'scissors':
            player_score = user_win(player_score)
        elif computerChoices == 'lizard':
            player_score = user_win(player_score)
        elif computerChoices == 'spock':
            computer_score = comp_win(computer_score)
    elif userChoice == 'paper':
        if computerChoices == 'rock':
            player_score = user_win(player_score)
        elif computerChoices == 'scissors':
            computer_score = comp_win(computer_score)
        elif computerChoices == 'lizard':
            computer_score = comp_win(computer_score)
        elif computerChoices == 'spock':
            player_score = user_win(player_score)
    elif userChoice == 'scissors':
        if computerChoices == 'rock':
            computer_score = comp_win(computer_score)
        elif computerChoices =='paper':
            player_score = user_win(player_score)
        elif computerChoices =='lizard':
            player_score = user_win(player_score)
        elif computerChoices =='spock':
            computer_score = comp_win(computer_score)
    elif userChoice == 'lizard':
        if computerChoices == 'spock':
            player_score = user_win(player_score)
        elif computerChoices == 'paper':
            player_score = user_win(player_score)
        elif computerChoices == 'rock':
            computer_score = comp_win(computer_score)
        elif computerChoices == 'scissors':
            computer_score = comp_win(computer_score)
    elif userChoice == 'spock':
        if computerChoices == 'rock':
            player_score = user_win(player_score)
        elif computerChoices == 'scissors':
            player_score = user_win(player_score)
        elif computerChoices == 'paper':
            computer_score = comp_win(computer_score)
        elif computerChoices == 'lizard':
            computer_score = comp_win(computer_score)

