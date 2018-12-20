'''
CMIT - 135
Week 4 Assignment
Jarred Glaser
'''

# Part 1.
def count_down():
    # While loop
    print("Counting down using 'while loop':")
    count = 10
    while count > 0:
        print(count)
        count -= 1
    
    # For Loop
    print("Counting down using 'for loop':")
    for i in range(10,0,-1):
        print(i)

# Part 2
def two_to_the_n():
    for i in range(1,101):
        print("n is: ", i)
        print("2^n is: ", 2**i)

# Part 3
def guessing_game_part_two():
    from random import randint
    randomNum = randint(1,100)

    while True:
        guess = input("Guess a number from 1 to 100: ")
        try:
            guess_int = int(guess)
        except ValueError:
            print("Please guess numbers only.")
            continue
        if guess_int > 100 or guess_int < 1:
            print("Please guess a number from 1 to 100 only.")
            continue
        if guess_int == randomNum:
            print("You win!")
            break
        else:
            print("Sorry that's not it, guess again!")
            continue

# Part 4
def multiplication_table():
    for i in range(1,10):
        row = ''
        for y in range(1,10):
            multiplication = str(i*y)
            if len(multiplication) > 1:
                row += ' ' + multiplication
            else:
                row += '  ' + multiplication
        print(row)

if __name__ == "__main__":
    print('''
    Please choose a program to run:
    1 = count_down
    2 = two_to_the_n
    3 = guessing_game_part_2
    4 = multiplication_table
    ''')
    choice = input("Enter number 1-4: ")
    if choice == "1":
        count_down()
    elif choice == "2":
        two_to_the_n()
    elif choice == "3":
        guessing_game_part_two()
    elif choice == "4":
        multiplication_table()
    else:
        print("Please pick a valid option 1-4.")
