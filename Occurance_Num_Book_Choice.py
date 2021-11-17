import re #importing regex
import pyinputplus as pyip #importing pyinputplus as pyip for ease
import pathlib #importing pathlib to find and read files.
import sys #importing system to be able to quit the application
from collections import Counter #doing a counting import

def specificword(choice): #function for the specific word
    while True: #while loop
        word_list = []  # list to hold the words found.
        user_word = pyip.inputStr(f"Enter a word to find in {choice}: ")  # variable is equal to a pyinputplus string
        if choice == 'The Last Plunge':  # if they choose the last plunge
            choice = "The_Last_Plunge"  # change their choice to the exact .txt name
        elif choice == 'Practical Agitation':  # if they choose practical agitation
            choice = "Practical_Agitation"  # change their choice to the exact .txt. name
        pattern = re.compile(fr'\b{user_word}\b')  # variable = the compile of the user word
        file = open(pathlib.Path.cwd() / f'{choice}.txt', encoding='utf-8')  # set a variable to open the text that they choose within the path of the current working directory
        every_word = file.read()  # we make a variable that is the entire text of Augustus
        file.close()  # close the file! Can't forget that
        while True:  # loop
            num = 0  # number variable inside the 2nd loop
            found_word = re.findall(pattern, every_word)  # we are setting found word to findall the pattern in every word.
            for i in found_word:  # for every word that we are looking for in Augustus
                word_list.append(i)  # put it in that list
                num += 1  # increment number by 1
            if choice == 'The_Last_Plunge':  # if we changed their choice to the literal .txt
                choice = "The Last Plunge"  # we change it back to normal so it doesn't look weird
            elif choice == 'Practical_Agitation':  # if we changed it to the literal .txt
                choice = "Practical Agitation"  # chachacha changes! Like David Bowie.
            print(f"{user_word} is in the book {choice} {num} times.")  # after we find the number, print the word and the number
            print(word_list)  # Show the list DELETE?
            input("Press enter to continue!")  # let the user look at everything before continuing.
            break  # break the loop
        play_again = pyip.inputYesNo("do you want to search for a word again?: ")  # take a yes or no from the user.
        if play_again == "yes":  # if its yes
            print()#line break
            main() #back to main function.
        elif play_again == "no":  # if its no
            print("bye bye!")  # goodbye!
            sys.exit()  # exits application.

def commonword(choice): #function for finding the most common words
    while True: #while loop
        file = open(pathlib.Path.cwd() / f'{choice}.txt', encoding='utf-8')  # set a variable to open the text that they choose within the path of the current working directory
        every_word = file.read()  # we make a variable that is the entire text of Augustus
        file.close()  # close the file! Can't forget that
        split_list = every_word.split() #creating a list and putting all the words into it as a list.
        Counters = Counter(split_list) #new variable is equal to counting the split list
        most_occur = Counters.most_common(3) #new variable that is set to the top 3 most common words in the counted split list.
        print(most_occur) #print the top 3 most common words
        input("Fun eh? Press enter to continue\n")#go ahead
        main()#go back to main

def main(): #main function to call back to if needed.
    while True: #loop
        print("Please choose from the following books to search for a word in.")#ask the user to choose which book they want to search in
        choice = pyip.inputMenu(['Augustus', 'The Last Plunge', 'Bacon', 'Practical Agitation']) #get the choice variable displayed in a menu from the choice of 4 books.
        print("Would you like to see the most common word in each book, or search a specific word?") #ask them if they want to see the most common word or search for a specific word.
        either = pyip.inputMenu(['Common', 'Specific']) #give them a choice in a menu
        if either == 'Specific': #if they want to search a word
            specificword(choice) #SEND THEM TO THE FUNCTION, passing choice into it.
        elif either == 'Common': #If they want to see the most common word
            commonword(choice) #send them to this function, passing choice into it

main() #The start of the program



