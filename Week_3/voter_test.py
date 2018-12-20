def voter_test():
    age = int(input("What is your age?"))
    if age >= 18:
        print("You are of voting age! Go exercise your right to vote!")
    else:
        years_left = 18 - age
        print("Sorry! You are not old enough to vote yet! You will be able to vote in {} years.".format(years_left))

voter_test()