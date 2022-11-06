import random
import re

# Variables and Attributes
plain_text = 'abcdefghijklmnopqrstuvwxyz'  # the 26 letters of the alphabet in order
key = ''  # same 26 letters that will be  randomly sorted to create a substituion key
user_message = ""
encrypted_message = ""


def Welcome():  # Welcome banner
    print(" ------------------------------------------------------------")
    print("|                 Substitution Cipher Program                |")
    print("|                   by Antonios F. Takos                     |")
    print(" -------------------------------------------------------------")


def Menu0():
    global key
    print("\n------------ Menu 0 ------------")
    print("(1): Generate key")
    print("(2): QUIT")
    option = int(input("What would you like to do?: "))
    if option == 1:
        generateKey(plain_text)
        Menu1()
    elif option == 2:
        exit()
    else:
        print("Invalid input. Please try again")
        Menu0()


def generateKey(alphabet):
    global key
    alphabet = list(alphabet)
    random.shuffle(alphabet)
    key = ''.join(alphabet)


# Menu for displayAlphKey() & inputMessage() functions
def Menu1():
    print("\n------------ Menu 1 ------------")
    print("(1): Print plaintext and key")
    print("(2): Input a message")
    print("(3): QUIT")
    option = int(input("What would you like to do?: "))
    if option == 1:
        displayAlphKey()
        Menu1()
    elif option == 2:
        inputMessage()
        Menu2()
    elif option == 3:
        quit()
    else:
        print("Invalid input. Please try again")
        Menu1()


# Prints out the plaintext alphabet and our substitution key
def displayAlphKey():
    alph_list = []
    for letter in plain_text:
        alph_list.append(letter)
    print("\np_t: " + str(alph_list))

    key_list = []
    for letter in key:
        key_list.append(letter)
    print("\nkey: " + str(key_list))


# Prompts the user to input a message to store in the user_message variable
def inputMessage():
    global user_message
    # print("\nPlease input a message that is all lowercase and with no spaces or special characters ;) ")
    # print("Yes: helloworld | No: Hello World")
    user_message = input("\nWhat is your message?: ")
    user_message = ReformatMessage(user_message)

    print("\nThe user message is now: " + user_message)


def ReformatMessage(message):
    message = message.lower()
    message = message.replace(" ", "")
    message = ''.join(item for item in message if item.isalnum())
    return message


# Menu encrypt() the user_message & re-assign said user_message if the user changes their mind
def Menu2():
    print("\n------------ Menu 2 ------------")
    print("(1): Reassign message")
    print("(2): Encrypt message")
    print("(3): QUIT")
    option = int(input("What would you like to do?: "))
    if option == 1:
        inputMessage()
        Menu2()
    elif option == 2:
        encrypted_message = encrypt(user_message)
        print("\nThis is the message encrypted: " + encrypted_message)
        Menu3()
    elif option == 3:
        quit()
    else:
        print("Invalid input. Please try again")
        Menu2()


def encrypt(message):  # takes the user_message and encrypts it according the to substitution key
    global plain_text
    encrypted = ""
    for char in user_message:
        index = plain_text.find(char)
        encrypted = user_message + key[index]

    return encrypted


def Menu3():  # Menu to allow the user to decrypt() the now encrypted user_message or re-assign said user_message
    print("\n------------ Menu 3 ------------")
    print("(1): Reassign message")
    print("(2): DECRYPT message [playing the role of the message RECIPIENT, Bob]")
    print("(3): Have a little fun by playing the role of the ATTACKER, Eve")
    print("(4): QUIT")
    option = int(input("What would you like to do?: "))
    if option == 1:
        inputMessage()
        Menu2()
    elif option == 2:
        decrypt()
        Menu3()
    elif option == 3:
        Eve()
    elif option == 4:
        quit()
    else:
        print("Invalid input. Please try again")
        Menu3()


def decrypt():  # takes the encrypted user_message and decrypts it according the to plaintext
    decrypted_message = ""
    for char in encrypted_message:
        index = key.find(char)
        decrypted_message = decrypted_message + plain_text[index]

    print("\nThis is the message decrypted!: " + decrypted_message)
    return decrypted_message


# --------------------- Cipher-text only attack [Eve] --------------------- #

def Eve():
    print("\n\n --------- You are now playing the role of Eve (the Attacker) ---------")
    option = input("Would you like to run the Letter Frequency Analyzer? [yes/y/Yes/yes or no/n/No/no]: ")
    if option == "yes" or "y" or "YES" or "Y":
        LetterFrequencyAnalyzer()
    elif option == "no" or "N" or "NO" or "quit" or "q" or "Q" or "QUIT":
        quit()
    else:
        print("Invalid input. Please try again")
        Eve()


def LetterFrequencyAnalyzer():
    print("\n------------------ Letter Frequency Analyzer ------------------")
    print("The Letter Frequency Analyzer will analyze text data from a text file of your choosing.")
    print("I VERY STRONGLY suggest that this text file be in the same directory as this program.")
    print("It is far easier to just input the name of your file (example.txt), rather than inputting a whole directory")

    fileName = input("Please CAREFULLY input the directory of your file: ")
    text_file = open(fileName)
    file_message = text_file.read()
    text_file.close()

    file_message = ReformatMessage(file_message)

    encrypted_text_file = encrypt(file_message)
    print("This is it encrypted: \n" + str(encrypted_text_file))

    frequency = list(range(26))
    letterByLetter = []
    for letter in range(26):
        frequency[letter] = 0

    for letter in range(len(encrypted_text_file)):
        for num in range(26):
            if encrypted_text_file[letter] == plain_text[num]:
                frequency[num] = frequency[num] + 1

    for count in frequency:
        rate = (count / len(encrypted_text_file))
        letterByLetter.append(rate)

    print("\nThe following is the frequency of each leter within the string")
    for i in range(26):
        print(plain_text[i] + "     " + str(letterByLetter[i]))


# LetterFrequencyAnalyzer() function ends here


# *** --------() 'Main Function' ()-------- ***#
Welcome()
Menu0()
key = generateKey(plain_text)