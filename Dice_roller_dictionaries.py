#Dice Rolling Project
#Russell Arlt
#CIT 112 David Hosler
from random import randint
import sys
min = 1 #the minimum number that the single die roll can be.
max = 6 #the maximum number that the single die roll can be.
rolls = 0 #A variable to be incremented.
def valid_number(): #function to ensure that a number is entered.
    while True: #starts a loop
        number = input("Dice rolling game! Rolls 2 die and adds them together. How many times do you want to roll the dice? : ") #getting an integer input from the user.
        if number <= "0":  # totally gets mad if they don't want to roll any
            print("Gotta roll something!")  # can't roll zero's or negatives!
            return valid_number() # go to function again
        try:  # beginning of exception handling
            return int(number)  # returning an int if possible.
        except ValueError:  # If we get a ValueError it will go here instead of shutting down the system.
            print('Ah ah ah! You did not enter an integer here. Try again.')  # Jurassic Park reference.
            return valid_number()  # throws you back to the top of the function.

number = valid_number() #gets the returned number if it is an integer.
numba_dict = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0} #dictionary 2-12 with its values set to 0.
while True: #while loop.
    if rolls < number: #if the rolls is less than the number entered then this loop will restart.
        print("rolling dice") #tells you its rolling the die.
        random1 = randint(min, max) #the first randomly rolled die.
        random2 = randint(min, max) #the second randomly rolled die.
        sum_value = random1 + random2 #the sum of the two randomly rolled die added together.
        key_find = numba_dict.items() #making variable key find equal to the named items, or keys, in the dictionary.
        for key, value in key_find: #for each key and value inside the variable of key find,
            if sum_value == key: #if that variable is equal to key,
                print(key) # print that variable out,
                value += 1 # add 1 to the value declared 0 in the dictionary
                numba_dict[key] = value # append the value that is the value of the key found above.
        rolls +=1 #increment rolls to continue through the loop
    elif rolls >= number: #if rolls is greater than or equal to the number asked for then it will continue here.
        print("Rolls completed. Data incoming....") #prints for the end of the code.
        break #breaks out of the while loop.
for k, v in numba_dict.items(): #for key and value in the dictionaries items,
    print(str(k) + " rolled " + str(v) + " times ") #print that key and associated value.