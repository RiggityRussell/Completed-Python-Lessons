######################
#Russell Arlt        #
#CIT 112 David Hosler#
#sub Builder         #
######################
import re #importing regex
import pyinputplus as pyip #importing pyinputplus as pyip for easier access
import sys #importing sys to quit the application if needed

pro_list = [] # list for protiens
cheese_list = [] #list for cheeses
cond_list = [] #list for condiments
veg_list = [] #list for veggies
sand_dict = {"Bread" : '', "Protien(s)" : pro_list, "Cheese" : cheese_list, "Condiments" : cond_list, "Vegetables" : veg_list} #dictionary for lists and values.
def ya_or_nay(): # a quick function for yes or no
    y_or_n = pyip.inputYesNo("Yes or No: ") # pyip only takes input in the form of yes, Yes, y, no, No,n and returns a yes or no value.
    if y_or_n == "yes": # if its equal to a yes
        yupper = 1 #we set yupper to 1
        print("okie dokie artichokie!") # everyone loves artichokes
        return yupper #we return yupper as a 1 or "yes"
    elif y_or_n == "no": #if its equal to a no
        yupper = 2 #we set yupper to no
        print("no troubles bubbles") # it really is no troubles
        return yupper #we return yupper as a 2 or "no"

print("Sandwich time!") # beginning of the code
while True: # while true we begin the sandwich making.
    sand_pattern = re.compile(r'white|wheat|rye|sourdough|waffle|gluten free') # declare a new variable, sand pattern to search for the words we want to see.
    bread = input("White, Wheat, Sourdough, Waffle, Gluten Free, or Rye?: ").lower() #declare bread variable equal to input and tell the user what their options are, lower it.
    if re.search(sand_pattern, bread): #if regex searches the sand pattern and it is matched by the input in bread
        sand_dict["Bread"]= bread.capitalize() #set the dictionary value "Bread" as what was input in bread variable, capitalized.
        break #leave loop
    else: # if regex searches the sand pattern and it is NOT matched by the input in bread
        print("not valid, try again.") # get them to try again.
        continue #back to the top of the loop
while True: # New while loop
    sand_pattern = re.compile(r'chicken|turkey|ham|pastrami|hummus') #redeclare a sand pattern for protiens, compiled by regex.
    print("add as many protiens as you would like, seperated by space or comma from,") #what protien you want?
    protien = pyip.inputStr("Chicken, Turkey, Ham, Pastrami, and Hummus: ").lower() #variable protien from the user input is asked and lowered
    if protien == "": #if nothing is entered
        print("Did you mean to put nothing here?: ") #question that decision.

    found_protiens = re.findall(sand_pattern, protien) #found protiens is equal to the regex expression findall, where we search sandwich pattern for what variables were typed in protien
    for protien in found_protiens: #for all protiens in the variable found protiens
        found_protiens = protien.capitalize() #capitalize it! Make it pretty!
        pro_list.append(found_protiens) #append the list pro_list with the variable found protiens
    if pro_list == []:
        print("Nothing valid entered in protien. Would you like to continue with no protien?")
        yupper = ya_or_nay()  # go to the yupper function to get the yes or no
        if yupper == 1:  # if 1 or "yes"
            break  # leave loop
        elif yupper == 2:  # if 2 or "no"
            continue  # go back to the top of the loop
        else:  # else statement
            print("how did you get here?")  # I don't even know.
            continue  # restart this loop.
    break #break the loop
while True: #loopy!
    chee_pattern = re.compile(r"american|swiss|gouda|bleu") #variable is equal to the regex expression compile, says look for this OR this OR this
    print("psssst... Hey y'all want cheese?") #do you?
    yupper = ya_or_nay() #function for yes or no
    if yupper == 1: # if 1 or 'yes'
        print("Pick as many as you'd like from, American, Swiss, Gouda, or Bleu: ") #choices
        cheese = input().lower() #variable for cheese
        found_cheese = re.findall(chee_pattern, cheese) #found cheese variable, finds all the correct usages of what was input into cheese and looks in chee pattern for them.
        for cheese in found_cheese: #for every input in found cheese
            found_cheese = cheese.capitalize() #capitalize that cheese!
            cheese_list.append(found_cheese) #put the found cheese into a list!
        if cheese_list == []: #if the list has nothing in it.
            print("Nothing valid entered in cheese. Would you like to continue with no cheese?") #ask them if they want to go with nothing.
            yupper = ya_or_nay()  # go to the yupper function to get the yes or no
            if yupper == 1:  # if 1 or "yes"
                break  # leave loop
            elif yupper == 2:  # if 2 or "no"
                continue  # go back to the top of the loop
            else:  # else statement
                print("how did you get here?")  # I don't even know.
                continue  # restart this loop.
        break #break the loop
    elif yupper == 2: # this means no
        print("Yeah who needs stinky ol cheese anyways.") #guess we dont like cheese
        break #break this loop
    else: #I always add an else statement
        print("seriously how does someone get here?") #dont think you can see this/
        continue #continue the loop
while True: #new loop!
    cond_pattern = re.compile(r"mayonnaise|mayo|mustard|vinegar|oil|salt|pepper|oregano") #condiment pattern setting!
    print("Do you want condiments?: ") #do you want the condiments
    yupper = ya_or_nay() # lets go into the yes or no function
    if yupper == 1: #if yes or 1
        condiments = input("Choose as many as you'd like from: Mayonnaise, Mustard, Vinegar, Oil, Salt, Pepper, and Oregano: ").lower() # create and ask for condiments variable
        found_condiments = re.findall(cond_pattern, condiments) #found condiments variable is searching the pattern and the input
        for condiment in found_condiments: # for every condiment that is in found condiments
            found_condiments = condiment.capitalize() #capitalize IT WE LIKE IT
            cond_list.append(found_condiments) #append that list!
        if cond_list == []: # is that list empty?
            print("Nothing valid entered in condiments. Would you like to continue with no condiments?")#errybody like condiments
            yupper = ya_or_nay()  # go to the yupper function to get the yes or no
            if yupper == 1:  # if 1 or "yes"
                break  # leave loop
            elif yupper == 2:  # if 2 or "no"
                continue  # go back to the top of the loop
            else:  # else statement
                print("how did you get here?")  # I don't even know.
                continue  # restart this loop.
        break #leave the loop
    if yupper == 2: #if it is a no
        break #leave the loop
while True: #new while loop
    veg_pattern = re.compile(r"lettuce|spinach|tomato|jalapeno|cucumber|olives") #veg pattern variable is the compile of the strings here
    print("Do you want veggies?: ") #ask em if they want them
    yupper = ya_or_nay() #yes function!
    if yupper == 1: #if yes!
        vegetables = input("veggie time! Lettuce, Spinach, Tomato, Jalapeno, Cucumber, and Olives: ").lower() #vegetables variable input from the liiiist
        found_veggies = re.findall(veg_pattern, vegetables) # make the variable and find all the matching variables of vegetables in veg pattern
        for vegetable in found_veggies: # for every vegetable in the found veggies variable
            found_veggies = vegetable.capitalize() # capitalize!
            veg_list.append(found_veggies) #put it in a list!
        if veg_list == []: #if its an empty list, did you mean to do that?
            print("Nothing valid entered in vegetables. Would you like to continue with no vegetables?") # errybody love veggies
            yupper = ya_or_nay()  # go to the yupper function to get the yes or no
            if yupper == 1:  # if 1 or "yes"
                break  # leave loop
            elif yupper == 2:  # if 2 or "no"
                continue  # go back to the top of the loop
            else:  # else statement
                print("how did you get here?")  # I don't even know.
                continue  # restart this loop.
        break #break it out
    if yupper == 2: # no no no
        break #break it out
bread_price = 2.00 # the price of the bread
protien_price = 3.00 # the price of each protien
pro_int = 0 # counting the number of protiens
cheese_price = 2.00 # the price of each cheese
cheese_int = 0 # counting the number of cheeses
condiment_price = .25 # the price of each condiment
cond_int = 0 # counting the number of condiments
veggie_price = 1.00 # the price of each veggie
veg_int = 0 # counting the number of veggies
for i in pro_list: # for each in protien list
    pro_int +=1 # increase the number of protiens picked by 1
for i in cheese_list: #for each in cheese list
    cheese_int +=1 #increase the number of cheeses picked by 1
for i in cond_list: #for each in condiment list
    cond_int +=1 #increase the number of condiments picked by 1
for i in veg_list: #for each veg in veg list
    veg_int += 1 #increase the number of veggies by 1

pro_string = ', '.join(pro_list) #take that list and join it as a string.
string_chee = ', '.join(cheese_list) #take the cheese list and make it a string
cond_string = ', '.join(cond_list) #take the condiment list and make it a string
veg_string = ', '.join(veg_list) #take the veg list and make it a string
if pro_string == '': #if we have no values for the string
    pro_string="nothing" #they get NOTHING
if string_chee == '': #if we have no values for the string
    string_chee = "nothing" #they get NOTHING
if cond_string == '':#if we have no values for the string
    cond_string = "nothing" #they get NOTHING
if veg_string == '':#if we have no values for the string
    veg_string = "nothing" #they get NOTHING

print(f'It looks like you got a sandwich with {sand_dict["Bread"]} bread; {pro_string} as protien(s); ' #showing the sandwich bread, protiens
      f'{string_chee} as cheese(s); {cond_string} as condiment(s); and {veg_string} as veggie(s)!') #cheeses, condiments, and veggies

sandwich_cost = (bread_price) + (pro_int * protien_price) + (cheese_int * cheese_price) + (cond_int * condiment_price) + (veg_int * veggie_price) #make a variable that is the bread price, plus the number of protiens times price plus the number of cheeses times price plus the number of condiments times price plus the number of veggies times price.
print(f"Your sandwich is ${sandwich_cost}") #show them cost of the sandwich
print("Would you like to buy this sandwich?") #do you?
yupper = ya_or_nay() #lets find out!
if yupper == 1: #if yes
    print("Now you have a sandwich!") # you got the internet sammy
    sys.exit() # leave
if yupper == 2: #if no
    print("Who needs a sandwich anyways?") # we never needed that sammy anyways
    sys.exit() #exits

#EOF