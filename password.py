######################
#Russell Arlt        #
#CIT 112 David Hosler#
#Pass Eval           #
######################
import re
import pyinputplus as pyip

pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
# Above statement says, if from the beginning of the string there is one occurence of a lowercase letter,
# then one occurence of a capital letter, one of a number, one of the symbols, or any of the aforementioned,
# at least 8 times.
pass_input = pyip.inputPassword("please enter a password. Eight letters, including uppercase, lowercase, symbols and a number required.") #getting a Password
if re.search(pattern, pass_input): # if regex.search finds the patterns requirements in pass input
    print("valid password") # password is valid
else: # otherwise
    print("invalid password") #password is invalid.
