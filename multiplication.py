#######################
#Russell Arlt         #
#CIT 112  David Hosler#
#Multiplication Quiz  #
#######################
import sys
import pyinputplus as pyip
import random as rand
import time

def main(): #starting a main function
    max_multi = pyip.inputInt("what is the max single value multiplier you want to see?: ", min=1, max=9) #making variable max_multi take only an integer input, at a min of 1 and max of 9
    quest_num = pyip.inputInt("how many questions would you like to answer?", min=1, max=999)  # setting variable equal to the input value of another integer. If not repeats.
    input("Press enter to start the quiz!")  # lets start this quiz.
    correct, incorrect = questions(quest_num, max_multi) #The variables correct and incorrect will be equal to the questions where we are taking the quest num and max multi
    stats(correct, incorrect) #passing correct and incorrect into the stats function
    play_again() #calling the play again function

def questions(quest_num, max_multi): #creation of the function questions, taking in quest num and max multi
    correct = 0 #starting variable correct at 0
    incorrect = 0 #starting variable incorrect at 0
    while True: # loop
        for num in range(0, quest_num): #for variable in range 0 to the number of questions to answer.
            num_random_one = rand.randint(0, max_multi) #creating a random number between 0 and the max multi number declared
            num_random_two = rand.randint(0, max_multi) #creating a second random number between 0 and the max multi number declared
            print(f"what is {num_random_one} x {num_random_two}?") #asking the user to do math!
            the_number = num_random_one * num_random_two # creating the answer from the random numbers
            tries = 0 #variable for the number of tries they will have.
            while True: #new loop
                try: # lets try this
                    answer = pyip.inputInt("answer: ", timeout=10, limit=3) #the answer they supply must be an int and we set a timeout of 10 and limit 3
                except pyip.RetryLimitException: #if this exception is thrown
                    print("limit of 3 reached, question incorrect.") #What is said if thats thrown
                    print(f"correct answer is: {the_number}") #shows the correct number
                    incorrect += 1 #increases the incorrect variable
                    break #breaks the loop
                except pyip.TimeoutException: #if this exception is thrown
                    print("timeout, question incorrect.") #print this
                    print(f"correct answer is: {the_number}")  # shows the correct number
                    incorrect += 1 #increment incorrect variable by 1
                    break #break
                if answer == the_number: # if the answer the user gives is equal to the number
                    print("Correct! You is smart and good.") #print this
                    correct += 1 #increment correct variable by 1
                    break #break
                elif answer is not the_number:# if they don't input the correct answer
                    incorrect += 1 #increment incorrect 1
                    tries += 1 #increment tries 1
                    if tries < 3: #count the number of tries, if its less than 3
                        print("wrong, try again") #let them try again!
                    elif tries >= 3: # count the number of tries if it is more than or equal to 3
                        print("correct attempt limit reached.") # they didn't get it in time!
                        print(f"correct answer is: {the_number}") #show them the folly of their ways
                        break #break it down!
                    continue #continue back up!
                else: #if somehow you get here, not sure how you would.
                    print("secret zone!") #easter egg
                    continue #keep going
        return correct, incorrect #return both correct and incorrect variables

def stats(correct, incorrect): #defining the stats function that is taking correct and incorrect
    toc = time.time() #takes the time at the moment that the user is in this spot.
    newtime = toc - tic # subtracts the original time from toc
    print("lets look at the stats!") #lets see these stats!
    print(f"You played for {newtime} seconds!") #shows the user how many seconds they played for.
    print(f"you got the answer correct, {correct} times! ") # shows the user how many you got correct
    print(f"you got the answer wrong, {incorrect} times.") #shows the user how many you got incorrect
    new_value = correct+incorrect # creates a new value from the correct and incorrect variables
    try: #try this!
        calc_percentage = (correct/new_value) * 100 #calculating the percentage by dividing correct by the new value variable and multiplying by 100
    except ZeroDivisionError: # If we get a zero division error
        if correct == 0: # and correct is 0
            calc_percentage = 0 #we will make the percentage at 0
        elif incorrect == 0: # or incorrect is 0
            calc_percentage = 100 #we will set percentage at 100
    print(f"your percentage right is {calc_percentage}%") # print the percentage

def play_again(): #define the function play again
    print("play again?") # ask them if they want to play again
    play_again = pyip.inputYesNo() #using the pyinputplus yes or no function to get a yes or no from the user
    if play_again == "yes": # if they do get a yes back from input yes no
        main() # calling back to the main function
    else: #else
        print("ok bye bye") #a sweet goodbye for you
        sys.exit() #leave the program

tic = time.time() #first part of the program, starting a timer
main() #calling us to the main function right away.





