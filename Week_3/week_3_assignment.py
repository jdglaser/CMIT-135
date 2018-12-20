'''
CMIT - 135 Week 3 Coding Assignments
Jarred Glaser
'''

from random import randint

def voter_test():
    age = int(input("What is your age?"))
    if age >= 18:
        print("You are of voting age! Go exercise your right to vote!")
    else:
        years_left = 18 - age
        print("Sorry! You are not old enough to vote yet! You will be able to vote in {} years.".format(years_left))

def grade_check():
    p = int(input("What is your grade percentage?"))
    if p > 93:
        print("Your grade is an A! Nice job!")
    elif p >= 90:
        print("Your grade is an A-! Nice job!")
    elif p >= 87:
        print("Your grade is a B+! Good job!")
    elif p >= 83:
        print("Your grade is an B! Good job!")
    elif p >= 80:
        print("Your grade is a B-! Good job!")
    elif p >= 77:
        print("Your grade is a C+! Not bad!")
    elif p >= 73:
        print("Your grade is a C! Not bad!")
    elif p >= 70:
        print("Your grade is a C-! Not bad!")
    elif p >= 67:
        print("Your grade is a D+! You're passing, but keep working!")
    elif p >= 63:
        print("Your grade is a D! You're passing, but keep working!")
    elif p >= 60:
        print("Your grade is a D-! You're passing, but keep working!")
    else:
        print("Sorry, you your grade is an F, try studying more!")

def big_small_number():
    num1 = input("Please enter the first number: ")
    num2 = input("Please enter the second number: ")
    total = int(num1) + int(num2)
    if total > 100:
        print("They add up to a big number!")
    else:
        print("They add up to {}".format(total))

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
    
if __name__ == "__main__":
    print("""
    Select Function to Run:\n
    1 = Voter Test\n
    2 = Grade Check\n
    3 = Big Number Check\n
    4 = Random Number Guessing\n
    Select a number 1-4:
    """)
    fun = int(input(""))
    if fun == 1:
        voter_test()
    elif fun == 2:
        grade_check()
    elif fun == 3:
        big_small_number()
    elif fun == 4:
        ran_num_guessing()
    else:
        print("Not a function...")
    


