#
# File     : main.py
# Author   : Anush De Costa
# Email ID : deyay064
# Description: Main driver program for the Caesar Cipher assignment, coordinating all functionalities.
# This is my own work as defined by the University's Academic Misconduct Policy.
#

from display_details import display_details
from menu_functions import get_menu_choice, get_encryption_input, get_decryption_input, get_brute_force_input
from cipher_functions import encrypt_string, decrypt_string, brute_force_decrypt


def main():
    """
    Main function to drive the program.
    Displays the details, shows the menu, and handles user choices.
    """

    # ASCII range for printable characters and offset limits
    min_ascii = 32  # Minimum ASCII value for space
    max_ascii = 126  # Maximum ASCII value for tilde (~)
    min_offset = 1  # Minimum Caesar Cipher offset
    max_offset = 94  # Maximum Caesar Cipher offset

    # Display author details
    display_details()
    keep_running = True
    while keep_running:

        # Get the user's menu choice
        choice = get_menu_choice()

        # Encrypt a string
        if choice == '1':
            user_string, offset = get_encryption_input(min_offset, max_offset)
            encrypted_string = encrypt_string(
                user_string, offset, min_ascii, max_ascii)
            print(f"\nEncrypted string:\n{encrypted_string}")

        # Decrypt a string
        elif choice == '2':
            cipher_text, offset = get_decryption_input(min_offset, max_offset)
            decrypted_string = decrypt_string(
                cipher_text, offset, min_ascii, max_ascii)
            print(f"\nDecrypted string:\n{decrypted_string}")

        # Brute force decryption
        elif choice == '3':
            cipher_text = get_brute_force_input()
            brute_force_decrypt(cipher_text, min_offset,
                                max_offset, min_ascii, max_ascii)

        # Quit the program
        elif choice == '4':
            print("\nGoodbye.\n")
            keep_running = False


if __name__ == "__main__":
    main()
