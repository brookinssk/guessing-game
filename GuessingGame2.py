from random import randint
randomNum = randint(1, 100)  # Creates a random number from 1-100

# print(randomNum)        # delete hashtag for quick guess checking
print('Let\'s play a game! Guess the number I picked between 1 - 100.')
userGuess = int(input())

while userGuess != randomNum:       # while the user's guess is not equal to the correct number it keeps asking for another input
    print('Nope! Wrong guess!')
    userGuess = int(input())

if userGuess == randomNum:          # just to make sure, this is only printed IF the guess is equal to the random number, not if the loop is exited or anything else
    print('Wow you got it!')
