#
# File     : deyay064_encryptor.py
# Author   : Anush De Costa
# Email ID : deyay064@mymail.unisa.edu.au
# Description: Programming Assignment 2 – Caesar Cipher
# This is my own work as defined by the University's Academic Misconduct Policy.
#

# Setting Up the Interactive Menu

def display_menu():
    print("\n*** Menu ***\n")
    print("1. Encrypt string")
    print("2. Decrypt string")
    print("3. Brute force decryption")
    print("4. Quit")


def get_menu_choice():
    return input("\nWhat would you like to do [1,2,3,4]? ")


def main():
    keep_running = True
    while keep_running:
        display_menu()
        choice = get_menu_choice()

        if choice == '1':
            print("In command 1 - encrypt string")
        elif choice == '2':
            print("In command 2 - decrypt string")
        elif choice == '3':
            print("In command 3 - brute force")
        elif choice == '4':
            print("\nGoodbye.")
            keep_running = False
        else:
            print("Invalid choice, please enter either 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
