#
# File     : menu_functions.py
# Author   : Anush De Costa
# Email ID : deyay064
# Description: Contains functions for displaying the menu and handling user input for the Caesar Cipher program.
# This is my own work as defined by the University's Academic Misconduct Policy.
#

def get_menu_choice():
    """
    Displays the menu and prompts the user to make a choice.
    Validates the user input to ensure it is one of the valid options (1, 2, 3, or 4).
    """
    print("\n*** Menu ***\n")
    print("1. Encrypt string")
    print("2. Decrypt string")
    print("3. Brute force decryption")
    print("4. Quit")
    choice = input("\nWhat would you like to do [1,2,3,4]? ")
    while choice not in ['1', '2', '3', '4']:
        print("Invalid choice, please enter either 1, 2, 3, or 4.")
        choice = input("\nWhat would you like to do [1,2,3,4]? ")
    return choice


def get_offset(min_offset, max_offset):
    """
    Prompts the user to enter an offset value within the specified range.
    Validates the user input to ensure it is a number within the range.
    """
    offset = input(f"Please enter offset value ({min_offset} to {max_offset}): ")
    while not offset.isdigit() or int(offset) < min_offset or int(offset) > max_offset:
        offset = input(f"Please enter offset value ({min_offset} to {max_offset}): ")
    return int(offset)


def get_encryption_input(min_offset, max_offset):
    """
    Prompts the user to enter a string to encrypt and an offset value.
    """
    user_string = input("\nPlease enter string to encrypt: ")
    offset = get_offset(min_offset, max_offset)
    return user_string, offset


def get_decryption_input(min_offset, max_offset):
    """
    Prompts the user to enter a string to decrypt and an offset value.
    """
    cipher_text = input("\nPlease enter the string to decrypt: ")
    offset = get_offset(min_offset, max_offset)
    return cipher_text, offset


def get_brute_force_input():
    """
    Prompts the user to enter a string for brute force decryption.
    """
    return input("\nPlease enter string to decrypt: ")
