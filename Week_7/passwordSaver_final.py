import csv
import sys

#The password file name to store the passwords to
passwordFileName = "PasswordFile.csv"

#The encryption key for the caesar cypher
encryptionKey=16

#Caesar Cypher Encryption
def passwordEncrypt (unencryptedMessage, key):

    #We will start with an empty string as our encryptedMessage
    encryptedMessage = ''

    #For each symbol in the unencryptedMessage we will add an encrypted symbol into the encryptedMessage
    for symbol in unencryptedMessage:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            encryptedMessage += chr(num)
        else:
            encryptedMessage += symbol
    return encryptedMessage

#Caesar Cypher decryption
def passwordDecrypt (encryptedMessage, key):

    #We will start with an empty string as our encryptedMessage
    decryptedMessage = ''

    #For each symbol in the unencryptedMessage we will add an encrypted symbol into the encryptedMessage
    for symbol in encryptedMessage:
        if symbol.isalpha():
            num = ord(symbol)
            num -= key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            decryptedMessage += chr(num)
        else:
            decryptedMessage += symbol
    return decryptedMessage

def loadPasswordFile(fileName):
    
    try:
        with open(fileName, 'r', newline='') as csvfile:
            passwordreader = csv.reader(csvfile)
            passwordList = list(passwordreader)
    except FileNotFoundError:
        open(fileName, 'w+')
        passwordList = []

    return passwordList

def savePasswordFile(passwordList, fileName):

    with open(fileName, 'w+', newline='') as csvfile:
        passwordwriter = csv.writer(csvfile)
        passwordwriter.writerows(passwordList)

passwords = loadPasswordFile(passwordFileName)
changes = False

while True:
    print("What would you like to do:")
    print(" 1. Lookup a password")
    print(" 2. Add a password")
    print(" 3. Delete a password")
    print(" 4. Save password file")
    print(" 5. Quit program")
    print("Please enter a number (1-5)")
    choice = input()

    if(choice == '1'): #Lookup a password
        if not passwords:
            print("No passwords created yet. Add a password first.")
            print()
            continue
        print("Which website do you want to lookup the password for?")
        for keyvalue in passwords:
            print('->',keyvalue[0])
        print("Select a choice from the list above")
        passwordToLookup = input()

        match = False
        for keyValue in passwords:
            if passwordToLookup == keyValue[0]:
                match = True
                decryptedPassword = passwordDecrypt(keyValue[1],encryptionKey)
                print("The password for {} is: {}".format(keyValue[0],decryptedPassword))

        
        if match == False:
            print("No match for password {}".format(passwordToLookup))

    if(choice == '2'):
        print("What website is this password for?")
        website = input()
        print("What is the password?")
        unencryptedPassword = input()

        encryptedPassword = passwordEncrypt(unencryptedPassword,encryptionKey)
        data = [website,encryptedPassword]
        passwords.append(data)
        changes = True
    
    if(choice == '3'): # Deletes password
        if not passwords:
            print("No passwords created yet. Add a password first.")
            print()
            continue
        print("What website password do you want to delete?")
        for keyvalue in passwords:
            print('->', keyvalue[0])
        print("Select a choice from the list above")
        passwordToDelete = input()

        match = False
        for keyValue in passwords:
            if passwordToDelete == keyValue[0]:
                match = True
                passwords.remove(keyValue)
                changes = True
        
        if match == False:
            print("No match for password {}".format(passwordToLookup))

    if(choice == '4'): #Save the passwords to a file
        savePasswordFile(passwords,passwordFileName)
        changes = False

    if(choice == '5'):  #quit our program
        if changes == True:
            print("You are about to exit with unsaved changes. Do you want to save first? (Answer with 'Yes' or 'No')")
            while True:
                choice = input()
                if choice == 'Yes':
                    savePasswordFile(passwords,passwordFileName)
                    sys.exit()
                elif choice == 'No':
                    sys.exit()
                else:
                    print("Please answer with 'Yes' or 'No'.")
        else:
            sys.exit()
    print()