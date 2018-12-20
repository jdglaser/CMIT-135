'''
CMIT - 135
Week 5 Assignment
Jarred Glaser
'''

def comma_code(join_method=False):
    '''
    Prints a user generated list. From previous Python knowledge I knew of a string method called
    'join()', which combines a list by a give string. I didn't feel this was quite in the spirit of
    the instructions of the assignment, so passing the 'join_method' argument of this function as
    'True' will use the 'join()' method, otherwise the function will use a for loop as instructed
    '''
    listToPrint = []
    while True:
        newWord = input("Enter a word to add to the list (press return to stop adding words) > ")
        if newWord == "":
            break
        else:
            listToPrint.append(newWord)
    
    # Print list
    if len(listToPrint) == 0:
        print("There are no items in your list.")
        return
    
    if len(listToPrint) == 1:
        print(listToPrint[0])
        return
    
    if len(listToPrint) == 2:
        print(listToPrint[0] + ' and ' + listToPrint[1])
        return

    if join_method == True:
        stringified_list = ', '.join(listToPrint[0:-1]) + ', and ' + listToPrint[-1]
        print(stringified_list)
        return
    else:
        stringified_list = ''
        for i in listToPrint[0:-1]:
            stringified_list += i + ', '
        stringified_list += 'and ' + listToPrint[-1]
        print(stringified_list)
        return

def backpack():
    import sys

    itemsInBackpack = ["book", "computer", "keys", "travel mug"]

    while True:
        print("Would you like to:")
        print("1. Add an item to the backpack?")
        print("2. Check if an item is in the backpack?")
        print("3. Quit")
        userChoice = input()
        
        if(userChoice == "1"):
            print("What item do you want to add to the backpack?")
            itemToAdd = input()
            
            ####### YOUR CODE HERE ######
            itemsInBackpack.append(itemToAdd)
            print(itemToAdd + " has been added to your backpack.")
            ####### YOUR CODE HERE ######
            
        if(userChoice == "2"):   
            print("What item do you want to check to see if it is in the backpack?")
            itemToCheck = input()
            
            ####### YOUR CODE HERE ######
            if itemToCheck in itemsInBackpack:
                print(itemToCheck + " is in your backpack.")
            else:
                print(itemToCheck + " is not in your backpack")
            ####### YOUR CODE HERE ######
        
        if(userChoice == "3"): 
            sys.exit()

def character_picture_grid():
    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]
    pivot_grid = []
    for y in range(0,6):
        row = []
        for x in range(0,9):
            row.append(grid[x][y])
        pivot_grid.append(row)
    
    for y in pivot_grid:
        print(''.join(y))

if __name__ == "__main__":
    print('''
    Please choose a program to run:
    1 = comma_code
    2 = back_pack
    3 = character_picture_grid
    ''')
    
    choice = input("Enter number 1-3: ")
    if choice == "1":
        comma_code(True)
    elif choice == "2":
        backpack()
    elif choice == "3":
        character_picture_grid()
    else:
        print("Please pick a valid option 1-3.")

    
