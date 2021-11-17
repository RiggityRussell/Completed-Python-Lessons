#########################
#Russell Arlt           #
#CIT 112 David Hosler   #
#Age Calculation        #
#########################

import datetime
import pyinputplus as pyip

def time_math(user_name): # function for getting the info
    while True: # while loop
        user_birth = input("Enter birth year, month, day, and minute in format as follows- 1987, December, 06, 42: ") # get the user input in this exact format
        try: # lets try to make it work!
            users_conv_birth = datetime.datetime.strptime(user_birth, '%Y, %B, %d, %M') # here we convert it into the datetime with strptime, asking for the full year, written month, numerical day, and numerical minute
            if users_conv_birth > datetime.datetime.now(): # We see if they entered a future date here
                print(f"{user_name}! Are you from the future!?") # we aint got time for future people!
                input("press enter to continue: ") # give em a break
                return time_math(user_name) # back to the loop!
            elif users_conv_birth < datetime.datetime.now(): # We are assured that they have entered a valid date
                print(f"{user_name}, you entered: {user_birth}.") # we show them their name and the entry they made.
                y_or_n = pyip.inputYesNo("Is this correct?:") # we check an input for if they entered it correctly.
                if y_or_n == 'yes': # if they did
                    print(f"We like it in this format {user_name}! {users_conv_birth}")  # show them the value we created with datetime.
                    input("Wonderful, please press enter to continue: ") # get them ready for more
                    return users_conv_birth #return the value that was created with datetime
                elif y_or_n == 'no': # if they entered something valid, but incorrect to them
                    input("Whoopsie do! Lets try again, press enter to continue: ") # we give them another chance
                    return time_math(user_name) # retrun to the loop!
            elif users_conv_birth == datetime.datetime.now(): # we see if they entered what time it is NOW
                print("Are you the chosen one? Neo?") # Matrix reference!
                input("press enter to continue: ") # always leave them wanting more
                return time_math(user_name) # to  the top again!
        except ValueError: # if they create a value error with their input at the top
            print(f"come on now {user_name} ya'll didn't read them instructions right") # we reprimand them. sternly.
            input("press enter to continue: ") # press enter!
            return time_math(user_name) # send em back!

user_name = input("What is your name dawg?: ") # well what is it?
birth_time = time_math(user_name) # send them to the function and get the return of that function!
user_time =  datetime.datetime.now() - birth_time # make a new variable where we subtract the users birthday from the time now.
time_str = str(user_time) # we make that a string
timelist = time_str.split() # we make that a list
print(f"{user_name}! you are {int(timelist[0]) / 365} years old!") # we do some math for years
print(f"That is {int(timelist[0]) / 12} months old!") # we do some math for months
print(f"The number of Hours: Minutes: and Seconds you've been alive is:\n{str(timelist[2])}") # we show them the hours, minutes and seconds they've been alive.
y_or_n = pyip.inputYesNo(f"Would you like to play again {user_name}?") # maybe you do?
if y_or_n == 'yes': # if so
    time_math(user_name) #start over
elif y_or_n == 'no': # if not
    print('OK. Bye bye.') # time to go.




