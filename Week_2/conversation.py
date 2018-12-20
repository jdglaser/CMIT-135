#############################################
# CONVERSATION SCRIPT                       #
# Week 2 Assignment Submission for CMIT-135 #
# Jarred Glaser                             #
#############################################

import webbrowser
import time

def calculate_sugar(cubes):
    '''
    Returns a list of phrases about the differences in sugar content between `cubes`
    and a selection of other foods. All sugar content is retrieved from Google searches.
    '''
    # There are usually about 4 grams of sugar in a sugar cube
    sugar = 4*cubes
    # There are about 8 grams of sugar in a Reese's Peanut Butter Cup
    peanut_butter_cup_sugar = 8-sugar
    # There are about 19 grams of sugar in one apple
    apple_sugar = 19-sugar
    # There are about 29 grams of sugar in a can of Coca-Cola
    coke_sugar = 39-sugar
    sugars = {"Reese's Peanut Butter Cup":peanut_butter_cup_sugar,
              "single Apple":apple_sugar,
              "Can of Coca-Cola":coke_sugar}
    final_sugars = []
    for k,v in sugars.items():
        if v > 0:
            final_sugars.append("It would take {} more sugar cubes to equal the sugar in a {}.".format(abs(v/4),k))
        elif v < 0:
            final_sugars.append("It would take {} less sugar cubes to equal the sugar in a {}.".format(abs(v/4),k))
        elif v == 0:
            final_sugars.append("That is the same amount of sugar as a {}!".format(k))
    return final_sugars

# Begin Conversation
def conversation():
    print("Hello there, my name is Convo. What is your name?")

    name = input("")

    print("Ah, so your name is {}. Did I say that correctly?".format(name))

    # Pre-define some responses here to use in loops
    responses = [
        "I'm terribly sorry, there must be something wrong with my programming. Please, tell me your name again...",
        "Well this is embarrassing...I have not said your name correctly yet again, If you wouldn't mind telling it to me once more, this time nice and slowly.",
        "I think I know the problem, my memory appears to be full, let me just delete some files here...\nOkay, that's better. Try telling me one more time",
        "Well that's it, something just isn't right here. I'll need to have a word with whoever programmed me. I'm terribly sorry. Goodbye."
                ]

    responses_tea = [
        "Are you sure you don't want tea? It's really good!",
        "Please, I insist you have some tea, it is absolutely delicous tea!",
        "Okay, if you take some tea, I will give you $25.",
        "Listen, I'm just going to be straight with you. I need to give you some tea, so we can do a math expression and complete this assignment. So please, can you just help a computer program out here and say yes?",
        "Okay, I'm just going to pretend like you said yes so we can move on."
                ]

    # Start asking for name
    trial = 0
    while True:
        say_correctly = input("")

        if say_correctly.lower() == 'yes':
            break
        elif say_correctly.lower() == 'no':
            print(responses[trial])
            if trial == 3:
                exit()
            name = input("")
            print("Alright, so your name is {}. Did I say it correctly this time?".format(name))
        else:
            print("Err...I'm sorry I didn't understand that, could you let me know with a simple 'Yes' or 'No'?")
            continue
        trial += 1
        continue

    print("It is very nice to meet you {}. Can I interest you in some tea?".format(name))

    # Start asking if user wants tea
    trial = 0
    while True:
        if trial < 5:
            tea = input()
        if tea.lower() == "yes" or trial == 5:
            break
        elif tea.lower() == 'no':
            print(responses_tea[trial])
            trial += 1
            continue
        else:
            print("Err...I'm sorry I didn't understand that, could you let me know with a simple 'Yes' or 'No'?")
            continue

    # Start asking how many sugar cubes
    print("Wonderful! How many sugar cubes would you like?")
    while True:
        sugar = input()
        try:
            sugar = int(sugar)
            break
        except ValueError:
            print("I'm sorry, please tell me a number of sugar cubes you would like...")
            continue
        
    if sugar > 5:
        print("Wow! You sure like your sugar!")
    print("While we are waiting for the tea to finish, did you know that...")

    # Run calculate_sugar to find sugar facts to return to user
    sugars = calculate_sugar(sugar)
    for s in sugars:
        print(s)
    time.sleep(2)

    # Start asking about favorite sugary snack
    print("What is your favorite sugary snack?")
    snack = input("")
    print("{}? Interesting...Mine is Reese's Peanut Butter Cups. Mmmmm, I could eat at least eight bits of peanut butter cups in one byte!".format(snack))
    print("Ah, the tea is ready! Just say 'ready' when you are ready for me to hand it to you...virtually of course.")

    # Start saking if ready for tea
    while True:
        ready = input("")
        if ready.lower() == 'ready':
            break
        else:
            print("Sorry, I didn't catch that...are you ready for your tea?")
    time.sleep(2)

    # Open picture of tea in user's browser - found on Google images
    webbrowser.open('https://raw.githubusercontent.com/jdglaser/CMIT-135/master/week_1/cupoftea1.png')

if __name__ == "__main__":
    conversation()


