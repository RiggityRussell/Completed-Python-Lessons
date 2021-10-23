##########################
#Inventory Management    #
#CIT 112 Russell Arlt    #
#David Hosler            #
##########################

import sys # importing that system to exit.

name_dict = ['chips', 'teddy bears', 'albacore tuna', 'double sided tape'] #lists for storing our values.
quantity_dict = ['10', '5', '43', '50']
price_dict = ['$3.89', '$8.65', '$0.89', '$2.49']
desc_dict = ['salty and crunchy!', 'soft and cuddly', 'canned fish', 'its sticky on both sides!']
inventory = {
    'name'        : name_dict,
    'quantity'    : quantity_dict,
    'price'       : price_dict,
    'description' : desc_dict
            } # Dictionary that holds 4 keys, and 4 values, which are our lists above.

def get_valid_int(): #function for error checking a number
    valid_quant = input("How many do we have on hand? :") #getting the user input to verify what they put is a number.
    if valid_quant <= "0": #totally gets mad if theres no inventory
        print("Well I don't think we can have no inventory. Maybe try counting again.") #gotta find those glasses!
        return get_valid_int() #returns to the to of the function.
    try: #beginning of exception handling
        return int(valid_quant) #returning an int if possible.
    except ValueError: # If we get a ValueError it will go here instead of shutting down the system.
        print('Ah ah ah! You did not enter a number here. Try again.') #Jurassic Park reference.
        return get_valid_int() #throws you back to the top of the function.

def get_valid_float(): #function of error checking a float.
    valid_price = input("How much does this cost? (please use a decimal place where approprite.) : ") #asks for a price and decimal place.
    try: #beginning of the exception handling.
        return float(valid_price) #returns a float if what is input is a float.
    except ValueError: # Where we go if theres an issue.
        print("Hmmmmm. Doesn't look right to me... Try again please.") #prompting user to try again.
        return get_valid_float() #returns them to the top of the function.

def main_program():#created a main to use to throw people back to the top of the program.
    while True:  # bool time!
        print("\nIf you want to see what we have please press a: ")  # shows inventory
        print("\nIf you want to add your own stuff to the inventory please press b: ")  # adds to inventory.
        print("\nTo see a specific product and its relevant attributes press c: ")  # shows a specific product, quantity, price, and description.
        print("\nType quit to quit: \n")  # lets you leave IF YOU WANT
        valid_input = input("\t")  # getting a valid input from the user.
        while True:  # bool time again!
            if valid_input == "a":  # if user input is a
                for k, v in inventory.items():  # for key and value in the dictionary called inventory showing items
                    print(k, v)  # prints the key and all the values from the list associated with the key.
                break  # breaking out of this loop

            elif valid_input == "b":  # if user input is b
                while True: #loop time!
                    valid_name = input("what is the name of the product? : ")  # takes a name to enter into the list.
                    if valid_name.lower() == 'quit': #just in case you're testing me
                        print("Well now you're just trying to break the code! Let's try again.") #gotcha!
                        continue #back to the top!
                    name_dict.append(valid_name)  # appends the new name to the list
                    print(valid_name + " eh? Perfect.")  # repeats the name back to the user.
                    valid_quant = get_valid_int()  # takes us to the function defined above.
                    quantity_dict.append(valid_quant)  # appends the quantity to the list.
                    print(str(valid_quant) + "! Well that's more than I thought we had.")  # repeats the quantity back to the user.
                    valid_price = get_valid_float()  # takes us to the function defined above.
                    price_dict.append("$" + str(valid_price))  # appends the price list and adds a $ to the front of it.
                    valid_descrip = input("What is this product?")  # asks for a description
                    desc_dict.append(valid_descrip)  # appends the appropriate list.
                    print("ok so we are adding, " + valid_name + ", and the quantity we have is, " + str(valid_quant))
                    print("and the price is $" + str(valid_price) + " and its description is, " + valid_descrip + ".")  # prints it all out for the user.
                    break  # breaks out fo the while loop.
                break #breaks out of the elif

            elif valid_input == "c":  # if user input is c
                while True: #loopy time
                    print("Enter a valid item and we will show you its values! Please enter done to stop.") #key word here is valid! It will restart if its not valid.
                    ask_for_name = input("what item and associated values did you want to see? : ")  # asks what item they want to see.
                    if ask_for_name.lower() == 'done': #lets the user leave this section
                        main_program() #back to the top!
                    for name in name_dict:  # runs through the names in the names list.
                        if ask_for_name == name:  # if the input name above is the same as a name in the list then it will continue.
                            hammer_time = name_dict.index(name)  # This took me too long. variable to store the index value of the name declared above.
                            print(ask_for_name)  #prints what the user entered
                            print(quantity_dict[hammer_time])  # finds the same index value as the declared one and returns the quantity.
                            print(price_dict[hammer_time])  # same as above but price
                            print(desc_dict[hammer_time])  # same as above but description
                            break #breaks out

            elif valid_input == "quit":  # you wanna leave?
                print("\nok bye I love you")  # go right ahead
                sys.exit()  # exits the application

            else:  # if all else fails we come to this.
                print("\nI am unable to understand this request. I am but a humble machine." +
                      "\nPlease carefully read the instructions and try again.")  # gets the user to try again.
                if input(
                        "\nPress enter to continue") == "":  # this'll stick you in a never ending loop if you dont just hit enter
                    break  # break time! sound the whistle!


print("Welcome to Russell's Inventory system! We have many wonderful things.") #beginning of the code.
main_program() #references the function above. Technically the second line of code.

