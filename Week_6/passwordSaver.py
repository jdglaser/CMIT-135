import csv
import sys

#The password list - We start with it populated for testing purposes
#passwords = [["yahoo","XqffoZeo"],["google","CoIushujSetu"]]


#The password file name to store the passwords to
passwordFileName = "samplePasswordFile.csv"

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

    with open(fileName, newline='') as csvfile:
        passwordreader = csv.reader(csvfile)
        passwordList = list(passwordreader)

    return passwordList

def savePasswordFile(passwordList, fileName):

    with open(fileName, 'w+', newline='') as csvfile:
        passwordwriter = csv.writer(csvfile)
        passwordwriter.writerows(passwordList)

passwords = loadPasswordFile(passwordFileName)

while True:
    print("What would you like to do:")
    print(" 1. Open password file")
    print(" 2. Lookup a password")
    print(" 3. Add a password")
    print(" 4. Delete a password")
    print(" 5. Save password file")
    print(" 6. Print the encrypted password list (for testing)")
    print(" 7. Quit program")
    print("Please enter a number (1-4)")
    choice = input()

    if(choice == '1'): #Load the password list from a file
        passwords = loadPasswordFile(passwordFileName)

    if(choice == '2'): #Lookup at password
        print("Which website do you want to lookup the password for?")
        for keyvalue in passwords:
            print(keyvalue[0])
        print("Select a choice from the list: ")
        passwordToLookup = input()

        match = False
        for keyValue in passwords:
            if passwordToLookup == keyValue[0]:
                match = True
                decryptedPassword = passwordDecrypt(keyValue[1],encryptionKey)
                print("The password for {} is: {}".format(keyValue[0],decryptedPassword))

        
        if match == False:
            print("No match for password {}".format(passwordToLookup))

    if(choice == '3'):
        print("What website is this password for?")
        website = input()
        print("What is the password?")
        unencryptedPassword = input()

        encryptedPassword = passwordEncrypt(unencryptedPassword,encryptionKey)
        data = [website,encryptedPassword]
        passwords.append(data)
    
    if(choice == '4'): # Deletes password
        print("What website password do you want to delete?")
        for keyvalue in passwords:
            print(keyvalue[0])
        print("Select a choice from the list: ")
        passwordToDelete = input()

        match = False
        for keyValue in passwords:
            if passwordToDelete == keyValue[0]:
                match = True
                passwords.remove(keyValue)
        
        if match == False:
            print("No match for password {}".format(passwordToLookup))

    if(choice == '5'): #Save the passwords to a file
        savePasswordFile(passwords,passwordFileName)


    if(choice == '6'): #print out the password list
        for keyvalue in passwords:
            print(', '.join(keyvalue))

    if(choice == '7'):  #quit our program
        sys.exit()

    print()
    print()