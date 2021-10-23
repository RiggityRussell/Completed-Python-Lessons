#Dictionary Dice Rolling Project
#Russell Arlt
#CIT 112 David Hosler
from random import randint
min = 1 #the minimum number that the single die roll can be.
max = 6 #the maximum number that the single die roll can be.
number = int(input("Dice rolling game! Rolls 2 die and adds them together. How many times do you want to roll the dice? : ")) #getting an integer input from the user.
rolls = 0 #A variable to be incremented.
dice_dictionary = {}
numba_list = []
while True: #while loop.
    if rolls < number: #if the rolls is less than the number entered then this loop will restart.
        print("rolling dice") #tells you its rolling the die.
        random1 = randint(min, max) #the first randomly rolled die.
        random2 = randint(min, max) #the second randomly rolled die.
        sum_value = random1 + random2 #the sum of the two randomly rolled die added together.
        print(sum_value) #printing that sum for the user.
        numba_list = sum_value
        dice_dictionary.setdefault( 'numb of roll' , numba_list )
        rolls += 1  # incrementing the roll value +1.
    elif rolls >= number:  # if rolls is greater than or equal to the number asked for then it will continue here.
        print("Rolls completed. Data incoming....")  # prints for the end of the code.
        break  # breaks out of the while loop.
for i in range(2,13): #this finds every value in the range 2-12 (it is exclusionary so not 13)
    count_up = 0 #a value to be incremented.
    for j in range(0,number): #counts from the first roll up to the number declared.
        if i == numba_list[j]: #if value is equal to value from the number list, repeat for each time this is true.
            count_up +=1 #increments up the value.
    print(str(i) + " rolled " + str(count_up) + " time(s)") #will print starting at 2, and incrementing up until 12,
                                                            #then prints the number of times count_up value was incremented.