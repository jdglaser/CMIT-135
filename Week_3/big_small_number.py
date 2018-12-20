def big_small_number():
    num1 = input("Please enter the first number: ")
    num2 = input("Please enter the second number: ")
    total = int(num1) + int(num2)
    if total > 100:
        print("They add up to a big number!")
    else:
        print("They add up to {}".format(total))

big_small_number()