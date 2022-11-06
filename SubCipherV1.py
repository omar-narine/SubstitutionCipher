import random
from collections import defaultdict, OrderedDict

plainText = "abcdefghijklmnopqrstuvwxyz"
plainTextList = []
plainTextList2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
keySpace = ""
keySpaceList = []
userMessage = ""
encryptedMessage = ""


def main_menu():
    global keySpace
    print("\nMain Menu - Options Below: ")
    print("(1) - Generate Key")
    print("(2) - Quit")
    user_input = int(input("Choose an option: "))
    if user_input == 1:
        keySpace = generate_key(plainText)
        print("\nKey has been generated!")
        menu2()
    elif user_input == 2:
        print("\nGoodbye!")
        exit()
    else:
        print("Invalid input!")
        main_menu()


def menu2():
    global keySpace
    global keySpaceList
    global plainText
    global plainTextList
    global userMessage
    global encryptedMessage
    keySpaceList = list(keySpace)
    plainTextList = list(plainText)

    print("Plain Text", end=": ")
    print(plainTextList)
    print("Encrypted", end=": ")
    print(keySpaceList)

    print("\nMenu - Options Below: ")
    print("(1) - Enter a string to be encrypted")
    print("(2) - Quit")
    user_input = int(input("Choose an option: "))

    if user_input == 1:
        userMessage = input("Enter message to encrypt: ")
        encryptedMessage = encryption_algorithm(userMessage)
        print("Encrypted message: " + encryptedMessage)
        menu3()
    elif user_input == 2:
        print("Goodbye!")
        exit()
    else:
        print("Invalid Input!")
        menu2()


def menu3():
    global userMessage
    print("\nMenu - Options Below: ")
    print("(1) - Decrypt Message ")
    print("(2) - Quit")
    user_input = int(input("Choose an option: "))

    if user_input == 1:
        userMessage = input("Enter message to encrypt: ")
        decrypted_message = decryption_algorithm(encryptedMessage)
        print("Decrypted message: " + decrypted_message)
        menu4()
    elif user_input == 2:
        print("Goodbye!")
        exit()
    else:
        print("Invalid Input!")
        menu3()


def menu4():
    print("\nMenu - Options Below: ")
    print("(1) - Encrypt a Text File ")
    print("(2) - Quit")
    user_input = int(input("Choose an option: "))

    if user_input == 1:
        encrypt_text_file()
    elif user_input == 2:
        print("Goodbye!")
        exit()
    else:
        print("Invalid Input!")
        menu4()


def menu5():
    print("\nMenu - Options Below: ")
    print("(1) - Decrypt a Text File ")
    print("(2) - Perform Letter Frequency Analysis on Encrypted Text File")
    print("(3) - Quit")
    user_input = int(input("Choose an option: "))

    if user_input == 1:
        decrypt_text_file()
    elif user_input == 2:
        letter_frequency_analysis()
    elif user_input == 3:
        print("Goodbye!")
        exit()
    else:
        print("Invalid Input!")
        menu5()


def generate_key(plain_text_string):
    plain_text = list(plain_text_string)
    random.shuffle(plain_text)
    key = "".join(plain_text)
    return key


def encryption_algorithm(text):
    encrypted_text = ""
    for character in text:
        if character == " ":
            encrypted_text = encrypted_text + " "
        else:
            for x in range(26):
                if character == plainTextList[x]:
                    print(plainTextList[x] + " ==> " + keySpaceList[x])
                    encrypted_text = encrypted_text + keySpaceList[x]
    return encrypted_text


def decryption_algorithm(text):
    decrypted_text = ""
    for character in text:
        if character == " ":
            decrypted_text = decrypted_text + " "
        else:
            for x in range(26):
                if character == keySpaceList[x]:
                    decrypted_text = decrypted_text + plainTextList[x]
    return decrypted_text


def encrypt_text_file():
    print("If file is located in same directory as python file, file name can just be entered. "
          "Otherwise entire the file address!")
    file_name = input(r"Enter file name/address: ")
    unencrypted_text_file = open(file_name, "r", encoding="utf8")
    encrypted_text_file = open("EncryptedText.txt", "w+", encoding="utf8")

    line = unencrypted_text_file.readline().lower()
    while line != "":
        encrypted_text = ""
        for character in line:
            if character not in plainTextList:
                if character != "\n":
                    encrypted_text = encrypted_text + character
            else:
                for x in range(26):
                    if character == plainTextList[x]:
                        encrypted_text = encrypted_text + keySpaceList[x]
        encrypted_text_file.write(encrypted_text)
        encrypted_text_file.write("\n")
        line = unencrypted_text_file.readline().lower()
    unencrypted_text_file.close()
    encrypted_text_file.close()
    print("\nText Encrypted and saved to 'EncryptedText.txt'!")
    menu5()


def decrypt_text_file():
    print("If file is located in same directory as python file, file name can just be entered. "
          "Otherwise entire the file address!")
    file_name = input(r"Enter file name/address: ")
    encrypted_text_file = open(file_name, "r", encoding="utf8")
    decrypted_text_file = open("DecryptedText.txt", "w+", encoding="utf8")

    line = encrypted_text_file.readline().lower()
    while line != "":
        decrypted_text = ""
        for character in line:
            if character not in keySpaceList:
                if character != "\n":
                    decrypted_text = decrypted_text + character
            else:
                for x in range(26):
                    if character == keySpaceList[x]:
                        decrypted_text = decrypted_text + plainTextList[x]
        decrypted_text_file.write(decrypted_text)
        decrypted_text_file.write("\n")
        line = encrypted_text_file.readline().lower()
    encrypted_text_file.close()
    decrypted_text_file.close()
    print("\nText Decrypted and saved to 'DecryptedText.txt'!")
    menu5()


def letter_frequency_analysis():
    print("If file is located in same directory as python file, file name can just be entered. "
          "Otherwise entire the file address!")
    file_name = input(r"Enter file name/address: ")
    encrypted_text_file = open(file_name, "r", encoding="utf8")

    line = encrypted_text_file.readline().lower()
    letter_frequency = {}
    total_counter = 0
    while line != "":
        for character in line:
            if character in plainTextList2:
                if character not in letter_frequency:
                    letter_frequency[character] = 1
                    total_counter += 1
                else:
                    letter_frequency[character] += 1
                    total_counter += 1
        line = encrypted_text_file.readline().lower()

    letter_frequency_copy = {k: v for k, v in sorted(letter_frequency.items(), key= lambda v: v[1])}

    print("Letter Frequency Table (In %): ")
    for x in letter_frequency_copy:
        print(x, end=": ")
        print((letter_frequency_copy[x] / total_counter) * 100)
    print(letter_frequency_copy)
    print(total_counter)
    encrypted_text_file.close()
# PlainTextFile.txt


main_menu()


# letter_frequency_analysis()