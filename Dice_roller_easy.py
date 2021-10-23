#Dice Rolling Project
#Russell Arlt
#CIT 112 David Hosler
from random import randint
import sys
min = 1
max = 6
number = int(input("Dice rolling game! Rolls 2 die and adds them together. How many times do you want to roll the dice? : "))
rolls = 0
numba_list = []
while True:
    if rolls < number:
        print("rolling dice")
        random1 = randint(min, max)
        random2 = randint(min, max)
        sum_value = random1 + random2
        print(sum_value)
        numba_list.append(sum_value)
        rolls += 1
    elif rolls >= number:
        print("Rolls completed. Data incoming....")
        break
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0
ten = 0
eleven = 0
twelve = 0
while True:
    for i in numba_list:
        if i == 2:
            two += 1
    for i in numba_list:
        if i == 3:
            three += 1
    for i in numba_list:
        if i == 4:
            four += 1
    for i in numba_list:
        if i == 5:
            five += 1
    for i in numba_list:
        if i == 6:
            six += 1
    for i in numba_list:
        if i == 7:
            seven += 1
    for i in numba_list:
        if i == 8:
            eight += 1
    for i in numba_list:
        if i == 9:
            nine += 1
    for i in numba_list:
        if i == 10:
            ten += 1
    for i in numba_list:
        if i == 11:
            eleven += 1
    for i in numba_list:
        if i == 12:
            twelve += 1
    print("2 rolled", two, "times")
    print("3 rolled", three, "times")
    print("4 rolled", four, "times")
    print("5 rolled", five, "times")
    print("6 rolled", six, "times")
    print("7 rolled", seven, "times")
    print("8 rolled", eight, "times")
    print("9 rolled", nine, "times")
    print("10 rolled", ten, "times")
    print("11 rolled", eleven, "times")
    print("12 rolled", twelve, "times")
    for i in numba_list:
        if i == 13:
            print("How in the hell did you get 13?")
    break

