#Computer Input
#Russell Arlt
#CIT 112
ask_for_specs = 0 #start with a variable at zero that will be incremented up to 5.
computer_spec_ask = ['CPU- ', 'Motherboard- ', 'RAM- ', 'Disk- ', 'Nic- '] #The information that will be asked for in a list.
print("This script will ask about your system information on your computer.") #telling the user whats happening
print("It will ask for your CPU, Motherboard, RAM, Disk, and Nic information.") #Still telling them things
entering_list = True #what will keep us in the loop
user_list = [] #List that will be created by the users input.
while entering_list is True: #beginning of the loop
    if ask_for_specs < 5: #If the ask for specs variable is less than 5 it will reiterate the loop
        print(computer_spec_ask[ask_for_specs]) #THIS IM PROUD OF. This will print out my list, one at a time based on what the ask for specs variable is currently at.
        user_spec = input() #The input for the list.
        if user_spec == '': # If the user doesn't put anything in then it will break out of the loop.
            break #breaks loop
        user_list.append(user_spec)  # how we add the users input into the list. user_list is now getting the input of user_spec sent to it.
        ask_for_specs += 1  # this will increment 1 up to 5 and then break. It will also change which list  data is given to the user.
    elif ask_for_specs >= 5: #If the variable hits 5, or more somehow, then the loop will break
        break #breaks loop
for i in range(0, ask_for_specs): # i in the range from 0 and ask for specs. This will allow us to go from 0, or CPU, until Nic, or if the user puts nothing, then it does nothing.
    print(computer_spec_ask[i] + user_list[i])# adding both lists together in another list.

