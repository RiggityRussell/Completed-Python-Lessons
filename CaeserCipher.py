##############################
#Russell Arlt                #
#CIT 112                     #
#David Hosler                #
#Caesar Cipher               #
##############################

import sys

"""
The second task will be to create a script that creates a standard shifting cipher.
This cipher, also known as a Caesar Cipher, will accept input from a user to determine
if they want to encrypt or decrypt a message.

You will then need to prompt the user for the shift they want to use.
For example, if the user chooses a shift of 20, the letter ‘a’ should be turned into the letter ‘t’.
You will need to account for both upper and lowercase letters, so lowercase letters can
become uppercase if the shift extends beyond the end of lowercase letters.
One way to think about this is as a large string containing all
uppercase letters followed by all lowercase letters with no spaces
(‘ABC...xyz’). The script must accept user input of the message, and depending on the selection to encrypt or decrypt,
it will change the text of the message based on the shift. Once the script has encrypted or decrypted the message it
will display the new message to the user.
You will use string manipulation, functions with multiple parameters,
exception handling, and significant comments for the processes that are being performed.

"""
def get_sentence_only():
    while True:
        print("\nPlease enter a sentence: ", end='')
        user_sentence = input()
        user_list = user_sentence.split()
        new_stuff = ''.join(user_list)
        if new_stuff.isalpha() == True:
            print("dope!")
            return new_stuff, user_sentence
        else:
            print("Please enter only words. Thank you.")
            return get_sentence_only()

def encrypt_or_decrypt():
    while True:
        print("would you like to encrypt or decrypt the sentence? (type help for explanation): ")
        decison = input().lower()
        if decison == 'encrypt':
            print("okie dokie artichokie! We will encrypt the sentence!")
            cipher_list.clear()
            encrypt_time = decison
            decrypt_time = "no!"
            return decison, encrypt_time, decrypt_time
        elif decison == 'decrypt':
            print("okie dokie artichokie! We will decrypt the sentence!")
            decrypt_time = decison
            encrypt_time = "no!"
            return decison, decrypt_time, encrypt_time
        elif decison == "help":
            print("Typing encrypt will allow you to move the letters in the sentence you type along the alphabet.")
            print("Typing decrypt will allow you to move the letters in the sentence you already typed backwards along the alphabet.")
            return encrypt_or_decrypt()
        else:
            print("Looks like you might need help. Please try again.")
            return encrypt_or_decrypt()
def get_shift_num():
    while True:
        print("Please enter the shift you wish to see for your cipher: ", end='')
        shift_choice = input()
        if shift_choice.isdecimal() == True:
            print(f"{shift_choice} times! Ok!")
            try:
                return int(shift_choice)
            except:
                print("looks like that isn't a valid integer!")
                return get_shift_num()
        else:
            print("Only integers here dawg.")
            return get_shift_num()

def encrypt_func():
    space_list = ' '.join(new_stuff)
    print(user_sentence)
    print(new_stuff)
    print(space_list)
    for element in space_list:
        if element in letters_list:
            beautiful_tyler = letters_list.index(element) + shift_choice
            cipher_list.append(
                letters_list[beautiful_tyler % 52])  # giving me the remainder and starting that at 1 in the list.
    bigBoiString = ''.join(cipher_list)
    return bigBoiString

def decrypt_func():
    space_list = ' '.join(new_stuff)
    for element in space_list:
        if element in letters_list:
            such_beautiful_tyler = letters_list.index(element) + (-abs(shift_choice))
            decrypt_list.append(letters_list[such_beautiful_tyler % 52]) #giving me the remainder and starting that at 1 in the list.
    newString = ''.join(decrypt_list)
    print(newString)
    return newString
print("\nRussells Caeser Cipher! You will type a sentence, tell me how many times you want it shifted, \nand I'll take care of the rest!")

all_letters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z "
letters_list = all_letters.split()
decrypt_list = []
cipher_list = []


while True:
    new_stuff, user_sentence = get_sentence_only()
    decrypt_time, encrypt_time, decision = encrypt_or_decrypt()
    shift_choice = get_shift_num()
    if decision == encrypt_time:
        bigBoiString = encrypt_func()
        print(bigBoiString)
        while True:
            print("\nWe did it! To decrypt the message\n press a)")
            print("To encrypt a new message\n press b)")
            print("To pack up your stuff and go home\n press c)")
            user_choice = input().lower()
            if user_choice == "a":
                decrypt_func()
                print("\nWasn't that great?")
            elif user_choice == "b":
                encrypt_func()
            elif user_choice == "c":
                print("\nok bye I love you")
                sys.exit()  # exits the application
            else:
                print("not valid!")
                continue
    elif decision == decrypt_time:
        newString = decrypt_func()
        print(newString)
        while True:
            print("To encrypt a new message\n press a)")
            print("To pack up your stuff and go home\n press b)")
            user_choice = input().lower()
            if user_choice == "a":
                encrypt_func()
            elif user_choice == "b":
                print("\nok bye I love you")
                sys.exit()  # exits the application
            else:
                print("not valid!")
                continue







            
