#Computer Input
#Russell Arlt
#CIT 112

CPU_list = [] #list for CPU's
Monitor_list = [] #list for Monitors
comp_question = {'CPU- ' : CPU_list, 'Motherboard- ' : '', 'RAM- ' : '', 'Disk- ' : '', 'Monitors- ' : Monitor_list} #Dictionary to hold keys and values, including the lists above.
print("\nGive me your computer information! I want it!") #give me the information!
print("Please enter as many CPU's as you have. When you are done enter 'done'.") #Instructing the user to enter multiple CPU's if needed.
while True: #while loop to get as many inputs as needed
    cpu_get = input() #variable for the input
    if cpu_get.lower() == 'done': #if they type done, in any way, breaks from the while loop.
        break #gets put of loop
    elif cpu_get == '' or cpu_get == ' ': #if they don't put anything in there it kicks them back to the top.
        print("WHOOPSIE DO! You didn't enter anything. Try again.") #a perfect print line.
        continue #kicking them to the top of the while loop
    else: #this will enter anything that they put into the input above.
        CPU_list.append(cpu_get) #appends the CPU list with the input asked above.
        continue #goes to the top of the while loop.
get_mothers_board = input("Whats that motherboard ya got?") #stores the motherboard variable
comp_question['Motherboard- '] = get_mothers_board #modifies the value of the motherboard.
get_ram = input("What kinda Ram y'all got?") #stores the ram variable.
comp_question['RAM- '] = get_ram #modifies the value of the ram
get_disk = input("What about the Disk?") #stores the disk variable.
comp_question['Disk- '] = get_disk #modifies the valuie of the disk
print("Some people have lots of monitors! Enter as many as you have, when you are done enter 'done'.") #asks for monitors
while True: #repeating loop
    mon_get = input() #getting monitors
    if mon_get.lower() == 'done': #if they type done it leaves the loop
        break #quits the loop
    elif mon_get == '' or mon_get == ' ': #if they don't type anything
        print("WHOOPSIE DO! You didn't enter anything. Try again.") #try again!
        continue #kicks them to the top of the while loop
    else: #If the if's dont trigger, this does.
        Monitor_list.append(mon_get) #appends the list above
        continue #goes back to the top of the while loop
print("Thank you for entering your information. We will NOT use it for evil.") #I plomise.
for k, v in comp_question.items(): #a for loop that is looking at the keys(k) and the values(v) in the dictionary
    print(str(k) + str(v)) #printing those keys and values next to each other.

