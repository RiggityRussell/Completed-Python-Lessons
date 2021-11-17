#########################
#Russell Arlt           #
#CIT 112 David Hosler   #
#PC Specs & Data Storage#
#########################
import pyinputplus as pyip
import pathlib
import re
import sys
import shelve #import many modules

def main(): # the main function that will be referenced to start the program
    while True: # while loop to stop any SHENANIGANS
        user_name = pyip.inputStr("Enter your name please:") # getting a string input for the user name (mostly to stop entering nothing.)
        pattern = re.compile(fr'{user_name}') # formatting the raw string to be the input from the user.
        user_file = open(pathlib.Path.cwd()/ 'UserName.txt', 'r', encoding='utf-8') # creating a variable that is equal to the reading value of UserName.txt. so we can look through it.
        name_there = user_file.read() # creating a variable that is reading the file.
        user_file.close() # closing the file.
        found_word = re.findall(pattern, name_there)  # we are setting found word to findall the pattern in every word.
        if user_name in found_word:  # for every word that we are looking for in found word
            user_exists(user_name) # if the user name is in the text document send them to this function
        elif user_name not in found_word:  # if the user name is not in the text document
            doesnt_exist(user_name) # send them to this function
        else: # HOW?
            print("Easter Egg!") # errybody like eggs!
            continue # restart loop

def doesnt_exist(user_name): # This function is for adding the user name to the .txt file.
    user_file = open(pathlib.Path.cwd()/ 'UserName.txt', 'r', encoding='utf-8') # reopening the file
    filetime = user_file.read() # reading the file
    print("current names in file are:") #telling us that current names in the file are
    print(filetime) # print the names
    user_file.close() # close the file.
    input("Press enter to continue: ") # a nice pause. Sometimes its good to slow down.

    user_file = open(pathlib.Path.cwd()/ 'UserName.txt', 'a', encoding='utf-8') # opening the file to APPEND new values to it.
    user_file.write(user_name + "\n") # adding the username with the write action. The \n is to stop the names from running together.
    user_file.close() # close the file.

    user_file = open(pathlib.Path.cwd() / 'UserName.txt', 'r', encoding='utf-8') # opening the file as a READ option
    print("updated names in file are:") # show them things changed
    filetime = user_file.read() # read that file!
    print(filetime) # print the names!
    user_file.close() # close the file
    yarp_or_narp = pyip.inputYesNo("\nWould you like to add your computer specs to the database?") # would you?
    if yarp_or_narp == "yes": # if they have entered an equivalent yes value
        adding_comp_info(user_name) # take them to the function! Bring user name with you!
    elif yarp_or_narp == "no": # if they have entered an equivalent no value
        print('Ok thats fine!\n') # and it really is fine
        main() #go back to the main function!


def adding_comp_info(user_name): # function for getting and appending the information to the text file.
    disk_list = [] # a list for disk!
    mon_list = [] # a list for monitors!
    user_shelf = shelve.open(user_name) # ok create a variable named user_shelf which opens a shelf, as the users name.
    CPU = pyip.inputStr("Enter your CPU here please: ") # variable for getting the CPU info
    user_shelf['CPU Name'] = CPU # much like a dictionary, we set the shelf name CPU NAME, then give it the info of CPU variable
    get_mothers_board = pyip.inputStr("Enter Motherboard: ") # variable for motherboard info
    user_shelf['Motherboard'] = get_mothers_board # set shelf value motherboard, give it the info
    get_ram = pyip.inputStr("Enter RAM: ") # Get ram info
    user_shelf['RAM'] = get_ram # set ram info in shelf
    disk_int = pyip.inputInt("How many disk drives do you have?: ", min=1 ) # get the number of disk drives, must be at least 1.
    disk_up = 1 # variable int for the number of disks to be displayed correctly.
    while True: # while this is true
        if disk_up < disk_int: # if disk up int is less than disk int
            print(f'Enter disk drive {disk_up}: ') # ask them to enter disk drive number x
            get_disk = pyip.inputStr() # variable equal to the input
            disk_list.append(get_disk) # put it in a list!
            disk_up +=1 # add 1 to disk up
            continue # go back to top
        elif disk_up >= disk_int: # if disk up in is greater than or equal to disk int
            print(f'Enter disk drive {disk_up}: ') # ask them to enter disk drive number x
            get_disk = pyip.inputStr() # get the final disk
            disk_list.append(get_disk) # append it
            break # leave the while loop!
    user_shelf['Disk'] = disk_list # set the shelf name Disk, give it that list.
    mon_int = pyip.inputInt("How many monitors do you have?", min=1) # give me a number that is more than 1!
    mon_up = 1 # setting the variable for counting
    while True: # while looooooop
        if mon_up < mon_int : # if mon up int is less than mon int
            print(f'Enter monitor {mon_up}: ') # enter monitor x
            get_mon = pyip.inputStr() # get the monitor name
            mon_list.append(get_mon) # append it to a list
            mon_up += 1 # increment 1
            continue # go again!
        elif mon_up >= mon_int: # if mon up int is less than mon int
            print(f'Enter monitor {mon_up}: ') # enter monitor x
            get_mon = pyip.inputStr() # get monitor name
            mon_list.append(get_mon) # append it to a list
            break # leave the loop
    user_shelf['Monitor'] = mon_list # Set the shelf name Monitor, give it that list.
    user_shelf.close() # close the shelf
    print("All values saved.") # did it!
    bye_bye_time = pyip.inputYesNo("Would you like to leave the application?: ") # if they are done
    if bye_bye_time == "yes": # thats fine
        print("It really is bye bye time.") # kick em out
        sys.exit() # leaves program.
    elif bye_bye_time == "no": # must be too much fun
        print("OK lets start again.") # and we will
        main() #start the program over
    else: # if somehow they can get poast the yes or no
        print("impossibru!") # They see this and the system shatters

def user_exists(user_name): # function for if the user is already in the database
    print("It looks as though you are in the database already.")  # we tell them that
    while True:
        user_menu = input('Enter A to see stored information.\nEnter B to update information\nEnter Q to quit Application\n\t') # we give them some options
        if user_menu.lower() == "a": # If they enter a
            try: # we start a try except!
                user_shelf = shelve.open(user_name) # we open the shelf
                print(f"OK {user_name}") # we print their name
                print(f"CPU is: {user_shelf['CPU Name']}") # we print the CPU entered
                print(f"Motherboard is: {user_shelf['Motherboard']}") # motherboard entered
                print(f"RAM is: {user_shelf['RAM']}") # RAM entered
                var = 1 # variable set at 1
                for disk in user_shelf['Disk']: # for each disk in the shelf key Disk
                    print(f"Disk {var}: {disk}") # print disk (1 or 2 or 3) Disk name
                    var += 1 # increment that number
                var = 1 # variable set at 1
                for monitor in user_shelf['Monitor']: # for each monitor in the shelf monitor
                    print(f"Monitor {var}: {monitor}") # print the number and name
                    var += 1 #increment variable
                user_shelf.close() #close the shelf
                input("Press enter to continue: \n") # a nice break
                main() # back to the main method
            except (ValueError, KeyError): # this is to stop people from entering data, forcing the system closed and not finishing it, then restarting and entering a name with no values.
                print("It looks as though you are in the database, but never entered information. Lets do that now.") # stops the error and forces putting new info in.
                adding_comp_info(user_name) #takes them to the relevant function

        elif user_menu.lower() == "b": # If they enter b
            user_shelf = shelve.open(user_name) # we open the shelf in their name
            del user_shelf['CPU Name'] # delete!
            del user_shelf['Motherboard'] # delete!
            del user_shelf['RAM'] # delete!
            del user_shelf['Disk'] # delete!
            del user_shelf['Monitor'] # delete!
            user_shelf.close() # close that shelf
            adding_comp_info(user_name) # take em to the function for adding info.

        elif user_menu.lower() == "q": # if they enter q they wanna go home
            print("It really is bye bye time.") # it is
            sys.exit() # EXIT

        else: # if they try anything FUNNY
            print("Not a valid option.") # they cant!
            continue # back to the top

main() # here is where the magic happens

