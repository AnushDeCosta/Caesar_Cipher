#
#  File     : deyay064_encryptor.py
# Author   : Anush De Costa
# Stud ID  : 110454712
# Email ID : deyay064@mymail.unisa.edu.au
# Description: Programming Assignment 2 – Caesar Cipher
# This is my own work as defined by the University's Academic Misconduct Policy.
#

# Implementing the Encrypt Command

def display_menu():
    print("\n*** Menu ***\n")
    print("1. Encrypt string")
    print("2. Decrypt string")
    print("3. Brute force decryption")
    print("4. Quit")


def get_menu_choice():
    return input("\nWhat would you like to do [1,2,3,4]? ")


def get_offset(min_offset, max_offset):
    offset = input(f"Please enter offset value ({
                   min_offset} to {max_offset}): ")
    while not offset.isdigit() or int(offset) < min_offset or int(offset) > max_offset:
        offset = input(f"Please enter offset value ({
                       min_offset} to {max_offset}): ")
    return int(offset)


def get_encryption_input(min_offset, max_offset):
    user_string = input("\nPlease enter string to encrypt: ")
    offset = get_offset(min_offset, max_offset)
    return user_string, offset


def encrypt_string(user_string, offset, min_ascii, max_ascii):
    encrypted_string = ""
    for char in user_string:
        ascii_value = ord(char)
        new_ascii_value = ascii_value + offset
        if new_ascii_value > max_ascii:
            new_ascii_value = min_ascii + (new_ascii_value - max_ascii - 1)
        encrypted_string += chr(new_ascii_value)
    return encrypted_string


def main():
    min_ascii = 32
    max_ascii = 126
    min_offset = 1
    max_offset = 94

    keep_running = True
    while keep_running:
        display_menu()
        choice = get_menu_choice()

        if choice == '1':
            user_string, offset = get_encryption_input(min_offset, max_offset)
            encrypted_string = encrypt_string(
                user_string, offset, min_ascii, max_ascii)
            print("\nEncrypted string:\n", encrypted_string)
        elif choice == '2':
            print("In command 2 - decrypt string")
        elif choice == '3':
            print("In command 3 - brute force decryption")
        elif choice == '4':
            print("\nGoodbye.")
            keep_running = False
        else:
            print("Invalid choice, please enter either 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
