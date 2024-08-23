import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('''\nWelcome to a deductive logic game. I am thiking a {}-digit positive integer with no repeated digits. Now, You give it a try to guess the number .Here are some gules.
    When I say :    That mean:
    Pico            One digit is correct but in the wrong position.
    Fermi           One digit is correct and in the right position.
    Bagels          No digit is correct.'''.format(NUM_DIGITS))

    while True:
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))
        
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            """keep looping till user does not give a valid input"""
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess No {} : '.format(numGuesses))
                guess = input('> ')
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))

        print('Do you want to play again? (yes or no) : ')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing.')

def getSecretNum():
    number = list('1920384756')
    random.shuffle(number)

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(number[i])
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi ')
        elif guess[i] in secretNum:
            clues.append('Pico ')
    
    if len(clues) == 0:
        return 'Bagels '
    else:
        clues.sort()
        return ''.join(clues)
        
# if __name__ == '__main__':
main()