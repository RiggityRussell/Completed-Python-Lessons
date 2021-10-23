"""
Lesson 1
New Python Script of my own choosing.
Russell Arlt
9/1/2021
"""
#print outputs what is located in the parentheses onto the screen.
print('Hello, what is your name?')
#Below I am having the user input the variable for a string in with their name.
name = input()
#Here I call the variable "name" into the print output.
print('Nice to meet you ' + name + '!')
#Below I used string to ask length to show us the number of letters in name.
print('Did you know your name is ' + str(len(name)) + ' letters long?')
print('What is your favorite number?')
#Number is being made a variable int with the user input.
number = input()
print('Well golly gee! ' + number + ' is my favorite number as well!')
print('If you had to put a decimal point on ' + number + ' what would the decimal be?')
#decimal is being used as a float variable.
decimal = input()
#Below I call all the variables together inside a print output.
print('Ok ' + name + ' your favorite number is ' + number + ' and the decimal point you would add is ' + decimal)
print('lets add your favorite number and the decimal together ' + name)
#Now I add the variables number and decimal.
print(number + decimal)
print('Well look at that! The power of math does it again!')
print('best to make sure we can multiply as well!')
#Multiplying the variables!
print(int(number) * float(decimal))
print("Now we're just having fun but lets divide these crazy numbers!")
#Dividing both ways!
print(float(decimal) / int(number))
print("Let's divide them the other way as well!")
print(int(number) / float(decimal))
print("I'm really proud of you " + name + ' for going through all this with me.')
