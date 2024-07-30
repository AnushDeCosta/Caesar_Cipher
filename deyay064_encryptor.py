#
# File     : deyay064_encryptor.py
# Author   : Anush De Costa
# Stud ID  : 110454712
# Email ID : deyay064@mymail.unisa.edu.au
# Description: Programming Assignment 2 – Caesar Cipher
# This is my own work as defined by the University's Academic Misconduct Policy.
#


# def main():

# Display Author Details
# def display_details():

# Get validate menu choice
# def get_menu_choice():
# Display menu (optional)
# def display_menu()

# Define offset value
# def get_offset():

# Loop Structure
# if command 1, display the encrypted string to screen
# if command 2, display the decrypted string to screen
# if command 3, display all 94 possible decrypted strings to screen
# if command 4, quit the program

# # existing functions to be used
# ord()
# chr()
# int()
# input()
# print()
# range()
# pow()
# len()
# str()aa
# string_name[index]
# isdigit()
# append()


# if __name__ == '__main__':
#     main()

# Creating a controlled loop
keep_running = True
while keep_running:
    # Print Menu options
    print("\n*** Menu ***")
    print("1. Encrypt string")
    print("2. Decrypt string")
    print("3. Brute force decryption")
    print("4. Quit")

    # Prompt user for input and process user input
    choice = input("What would you like to do [1,2,3,4]? ")

    if choice == '1':
        print("In command 1 - encrypt string")
    elif choice == '2':
        print("In command 2 - decrypt string")
    elif choice == '3':
        print("In command 3 - brute force")
    elif choice == '4':
        print("Goodbye.")
        keep_running = False
    else:
        print("Invalid choice, please enter either 1, 2, 3, or 4.")
