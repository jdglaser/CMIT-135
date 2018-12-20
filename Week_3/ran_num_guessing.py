from random import randint

def ran_num_guessing():
    print("I'm thinking of a number between 0 and 9, what is it?")
    randomNum = randint(0,9)
    while True:
        guess = int(input("Enter your guess: "))
        if guess < 0:
            print("Please enter a number from 0 to 9")
            continue
        elif guess > 9:
            print("Please enter a number from 0 to 9")
            continue
        else:
            break
    if randomNum == guess:
        print("You got it correct!")
    else:
        print("You got it wrong, the answer was {}. Sorry, try again.".format(randomNum))

ran_num_guessing()