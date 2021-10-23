import random

# All the lower case letters of the alphabet, will use this for checking input
LETTERS = 'abcdefghijklmnopqrstuvwxyz'
# Characters that might be in the text file, but we don't want them to have to guess
FILL_INS = ' ,\'"!@#$%^&*()-=+'

# This defines all the steps of the hangman sequence, quick ASCII images of the hanging
HANGMAN_STEPS = [ '''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  o   |
      |
      |
     ===''', '''
  +---+
  o   |
  |   |
      |
     ===''', '''
  +---+
  o   |
 /|   |
      |
     ===''', '''
  +---+
  o   |
 /|\  |
      |
     ===''', '''
  +---+
  o   |
 /|\  |
 /    |
     ===''', '''
  +---+
  o   |
 /|\  |
 / \  |
     ===''', '''
  ___
 /   \\
| x x |
|  _  |
 \___/
''']


# Will accept a list and pick a random item from it and return the item
def getRandomWord( wordList ):
    index = random.randint( 0, len( wordList ) )
    return wordList[index].rstrip().lower()

# Shows the game board based
def hangDisplay( wrongLetters, rightLetters, secret ):
# The step of hanging is based on how many wrong letters they have
# When the game first starts it will have no wrong letters and picks the first image
    print(HANGMAN_STEPS[len(wrongLetters)])
    print()
# Display a list of the letters that they've gotten wrong under the gallows
    print('Incorrect guesses: ', end=' ')
    for l in wrongLetters:
        print(l, end=' ')
    print()
# Create blanks for each letter in the secret word
    blanks = '_' * (int(len( secretWord )))
# If they've picked the correct letter replace the blank with the letter
    for i in range( len( secretWord )):
        if secret[i] in FILL_INS: # Handles non-letters in the word file
            blanks = blanks[:i] + secret[i] + blanks[i+1:]
        if secret[i] in rightLetters:
            blanks = blanks[:i] + secret[i] + blanks[i+1:]

# Print out the string of underscores and correct letters
    for l in blanks:
        print( l, end=' ' )
    print()
    return wrongLetters, rightLetters, secret

# Accept user input and ensure that it is a single letter in the alphabet
def userGuess():
    while True:
        guess = input( 'Choose a letter: ' ).lower()
        if len( guess ) != 1:
            print( 'Please pick a single letter to guess' )
        elif guess not in LETTERS:
            print( 'Please enter a letter.' )
        else:
            return guess

# Take user input to see if they want to play again
def playAgain():
    print( 'Do you want to play again? (yes or no): ', end='' )
    return input().lower().startswith('y')

# Sets the variables for the script as well as opening the file to read
# the list of items we want to pick at random.
def setupGame():
    global wrongLetters
    global rightLetters
    global secretWord
    gameFinished = False

    try:
        file1 = open( 'animals.txt', 'r' )
        words = file1.readlines()
        file1.close()
    except IOError:
        print( 'Unable to open animals.txt file. Resorting to using the word "broken".' )
        words = [ 'broken' ]
    secretWord = getRandomWord( words )
    wrongLetters = ''
    rightLetters = ''
    return gameFinished == False

gamesWon = 0
gamesLost = 0
totalGames = 0

setupGame()
while True:
    gameFinished = False
# Each iteration give the game board, based on the function to determine the stage of the gallows
    wrongLetters, rightLetters, secretWord = hangDisplay(wrongLetters, rightLetters, secretWord)
# Accept input, should provide all the letters that the user has guessed to this point
    guess = userGuess()
    if guess in secretWord: # Check if the letter is in the secret word
        rightLetters += guess # Add the right letter to ones they've done correctly
        wordSolved = True # Set the variable to true before checking
        for i in range( len( secretWord ) ):
            if secretWord[i] in FILL_INS:
                continue
            if secretWord[i] not in rightLetters: # If they have even a single letter wrong, they aren't done
                wordSolved = False
                break
        if wordSolved: # If they solved the word it will do this part
            print(f"You figured out the word {secretWord}! I'm very proud of you") # Repeat the word they solved
            gamesWon += 1
            gameFinished = True
    else: # The letter wasn't in the word
        wrongLetters += guess  # Different string of bad characters
        if len( wrongLetters ) == len( HANGMAN_STEPS ) - 1: # This means the gallows are complete
            hangDisplay( wrongLetters, rightLetters, secretWord ) # Show the last stage
            print( f'You have run out of guesses!')
            print(f'You tried {len( wrongLetters )} wrong letters and {len( rightLetters )} right letters.')
            print(f'The word you were looking for was "{secretWord}".') # Tell them number of right/wrong guesses, and what the secret was
            gamesLost += 1
            gameFinished = True

    if gameFinished == True:
        if playAgain():
            setupGame() # Will run if the user enters y or yes to play again and reset variables for another play
        else:
            totalGames = gamesWon + gamesLost
            print( f'You played {totalGames} games. You won {gamesWon} and lost {gamesLost}.' ) #Give them stats before closing
            break

#EOF

