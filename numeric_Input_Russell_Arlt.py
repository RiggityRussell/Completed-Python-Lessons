#Mathematical Program
#Russell Arlt
#CIT 112
import math #imports the math library
def input_int_number(): # the function that will handle exceptions for the input of a number
    number = input("\nEnter a number pal: ") #where number is defined by the user input
    if number != "0": #Makes sure that the number isn't a zero, even though it is in a string form at the moment.
        try: #beginning of the try, except for handling exceptions.
            return int(number) #returns a valid int for the variable number
        except ValueError: #what will trigger if an integer is not entered
            print(f"\n{number} ain't no number I ever heard of! try that again.")# what prints out if someone enters something other than a number
            return input_int_number() #throws the user back to the top of the function to try again
    elif number == "0": #checks to see if they input 0
        print("NO! Not zero!")  #Yells at the user for putting in a zero.
        return input_int_number() #throws them back to the top of the function

def even_number(number): #the function that is called if the number can be divided by 2 until zero. returns a new number defined in the local scope.
    number = number//2 #uses floor division to half the even number, will continue to do so until it hits an odd number.
    return number #returns number out of the function to the global scope.

def odd_number(number): #the funtion that is called if the number CANNOT be divided by 2 until zero. returns a new number defined in the local scope.
    number = 3*number+1 #multiplies the number by 3 and adds 1
    return number #returns number out of the function to the global scope

number = input_int_number() #number variable that is defined and returned from the function input_int_number
print(f"{number} is your number") #prints out what the number is
divisible = True #defines divisible is True
while divisible == True: #will run this code beneath it forever while it is true
    if number // 2 == 0:  # checks to see if the number is floor divided by 2 and equals zero. number could also == 1 and have the same parameters.
        print(number) #if it can be divided by zero it prints the number
        print("thats all!") #Last statement of the program
        divisible = False #when divisible stops being true it exits the main code block and ends the program.
    elif number % 2 == 0: #this checks to see if the number is even by using modulo
        print(number) #prints the number
        number = even_number(number) #takes the variable number defined within the even_number function
    elif number % 2 != 0: #this checks to see if the number is odd by using modulo
        print(number) #prints the number
        number = odd_number(number) #takes the variable number defined within the odd_number function.

#EOF