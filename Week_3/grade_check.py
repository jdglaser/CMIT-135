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

grade_check()