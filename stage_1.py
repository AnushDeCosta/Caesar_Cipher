#
#  File     : deyay064_encryptor.py
# Author   : Anush De Costa
# Stud ID  : 110454712
# Email ID : deyay064@mymail.unisa.edu.au
# Description: Programming Assignment 2 – Caesar Cipher
# This is my own work as defined by the University's Academic Misconduct Policy.
# 


def display_menu():
    print("\n*** Menu ***")
    print("1. Encrypt string")
    print("2. Decrypt string")
    print("3. Brute force decryption")
    print("4. Quit")

def get_menu_choice():
    return input("What would you like to do [1,2,3,4]? ")

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
            print("In command 3 - brute force decryption")
        elif choice == '4':
            print("Goodbye.")
            keep_running = False
        else:
            print("\nInvalid choice, please enter either 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
