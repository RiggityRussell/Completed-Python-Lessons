######################
#Russell Arlt        #
#CIT 112 David Hosler#
#Word Counting       #
######################

import re #importing regex
import pyinputplus as pyip #importing pyinputplus as pyip for ease
import pathlib #importing pathlib to find and read files.
import sys #importing system to be able to quit the application

while True: #loop
    word_list = [] #list to hold the words found.
    user_word = pyip.inputStr("Enter a word to find in Augustus: ") #variable is equal to a pyinputplus string
    pattern = re.compile(fr'\b{user_word}\b') # variable = the compile of the user word
    file_Augustus = open(pathlib.Path.cwd()/ 'Augustus.txt', encoding='utf-8') #set a variable to open the text Augustus within the path of the current working directory
    every_word = file_Augustus.read() #we make a variable that is the entire text of Augustus
    file_Augustus.close() #close the file! Can't forget that
    while True: #loop
        num = 0 #nmber variable inside the 2nd loop
        found_word = re.findall(pattern, every_word) #we are setting found word to findall the pattern in every word.
        for i in found_word: #for every word that we are looking for in Augustus
            word_list.append(i) #put it in that list
            num += 1 #increment number by 1
        print(f"{user_word} is in the book Augustus {num} times.") #after we find the number, print the word and the number
        print(word_list) #Show the list DELETE?
        input("Press enter to continue!") #let the user look at everything before continuing.
        break #break the loop
    play_again = pyip.inputYesNo("do you want to search for a word again?: ") #take a yes or no from the user.
    if play_again == "yes": #if its yes
        continue #restart the loop
    elif play_again == "no": #if its no
        print("bye bye!") #goodbye!
        sys.exit() #exits application.





