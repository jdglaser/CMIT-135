print("It is very nice to meet you {}. Can I interest you in some tea?".format("Jarred"))
responses_tea = ["Are you sure you don't want tea? It's really good!",
             "Please, I insist you have some tea, it is absolutely delicous tea!",
             "Okay, if you take some tea, I will give you $25.",
             "Listen, I'm just going to be straight with you. I need to give you some tea, so we can do a math expression and complete this assignment. So please, can you just help a computer program out here and say yes?",
             "Okay, I'm just going to pretend like you said yes so we can move on."
             ]
trial = 0
while True:
    if trial < 5:
        tea = input()
    if tea == "yes" or trial == 5:
        break
    elif tea.lower() == 'no':
        print(responses_tea[trial])
        trial += 1
        continue
    else:
        print("Err...I'm sorry I didn't understand that, could you let me know with a simple 'Yes' or 'No'?")
        continue

print("Wonderful! How many sugar cubes would you like?")
while True:
    sugar = input()
    try:
        sugar = int(sugar)
        break
    except ValueError:
        print("I'm sorry, please tell me a number of sugar cubes you would like...")
        continue