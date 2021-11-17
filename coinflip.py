#########################
#Russell Arlt           #
#CIT 112 David Hosler   #
#Coinflip debug         #
#########################



import random
import logging

logging.disable()
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')# RA This allows us to set the level of debugging we want to see,with the level of error, and the message generated.
logging.debug('Program start')
numRight = 0 # Used to record total amount of correct answers
tries = 0 # Used to record total number of attempts

while True: # Loop to keep the guessing going
    guess = ''

    while guess not in ( 'heads', 'tails', 'q', 'quit' ): # Checks the user input
        print( 'Guess the coin toss--heads or tails (q to exit).' )
        guess = input().lower() # RA added lower to make sure that it will match heads or tails lowercase.
    if guess in ( 'q', 'quit' ): # Handle them deciding to quit
        break
    flip = random.randint( 0, 1 ) # 0 for tails, 1 for heads
    if flip == 0:
        flip = "tails"
    elif flip == 1:
        flip = 'heads'
    else:
        print("wild.")
    logging.debug(f'computers choice is {flip}, users choice is {guess}')
    tries += 1 # RA changed to increment instead of set value at 1
    # assert flip == guess ### I Used this to discover that flip is always either 0 or 1
    if flip == guess: # If the guess was right tell them and record it
        print( 'That\'s right!' )
        numRight += 1 # RA changed to increment instead of set value at 1
    else: # Otherwise they aren't right
        print( 'That\'s not right.' )
        # RA removed the numRight variable setting it back to zero if they failed.

logging.debug(f'There was {tries} tries, and {numRight} were correct.') # used to ensure that the incrementing is working correctly.
print( f'Game over.\nYou got {numRight} out of {tries} attempts.' )

#EOL