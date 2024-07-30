#
# File     : deyay064_encryptor.py
# Author   : Anush De Costa
# Email ID : deyay064
# Description: Programming Assignment 2 – A Caesar Cipher program for encryption, decryption, and brute force decryption.
# This is my own work as defined by the University's
# Academic Misconduct Policy.
#

def display_details():
    """
    Displays the author's details.
    """
    print("\nFile     : deyay064_encryptor.py")
    print("Author   : Anush De Costa")
    print("Stud ID  : 110454712")
    print("Email ID : deyay064")
    print("Description: Programming Assignment 2 - Caesar Cipher")
    print("This is my own work as defined by the University's Academic Misconduct Policy.")


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
    Prompts the user to enter a string to encrypt and and also prompts for an offset value.
    """
    user_string = input("\nPlease enter string to encrypt: ")
    offset = get_offset(min_offset, max_offset)
    return user_string, offset


def get_decryption_input(min_offset, max_offset):
    """
    Prompts the user to enter a string to decrypt and and also prompts for an offset value.
    """
    cipher_text = input("\nPlease enter the string to decrypt: ")
    offset = get_offset(min_offset, max_offset)
    return cipher_text, offset


def get_brute_force_input():
    """
    Prompts the user to enter a string for brute force decryption.
    """
    return input("\nPlease enter string to decrypt: ")


def encrypt_string(user_string, offset, min_ascii, max_ascii):
    """
    Encrypts a string using the Caesar Cipher method with the given offset.
    """
    encrypted_string = ""
    for char in user_string:
        ascii_value = ord(char)
        new_ascii_value = ascii_value + offset

        # Wrap around if the new ASCII value exceeds the maximum ASCII value
        if new_ascii_value > max_ascii:
            new_ascii_value = min_ascii + (new_ascii_value - max_ascii - 1)
        encrypted_string += chr(new_ascii_value)
    return encrypted_string


def decrypt_string(cipher_text, offset, min_ascii, max_ascii):
    """
    Decrypts a string using the Caesar Cipher method with the given offset.
    """
    decrypted_string = ""
    for char in cipher_text:
        ascii_value = ord(char)
        new_ascii_value = ascii_value - offset

        # Wrap around if the new ASCII value is less than the minimum ASCII value
        if new_ascii_value < min_ascii:
            new_ascii_value = max_ascii - (min_ascii - new_ascii_value - 1)
        decrypted_string += chr(new_ascii_value)
    return decrypted_string


def brute_force_decrypt(cipher_text, min_offset, max_offset, min_ascii, max_ascii):
    """
    Attempts to decrypt the cipher text using all possible offsets within the range.
    """
    for offset in range(min_offset, max_offset + 1):
        decrypted_string = decrypt_string(
            cipher_text, offset, min_ascii, max_ascii)
        print(f"Offset {offset}: {decrypted_string}")


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
            encrypted_string, offset = get_decryption_input(
                min_offset, max_offset)
            decrypted_string = decrypt_string(
                encrypted_string, offset, min_ascii, max_ascii)
            print(f"\nDecrypted string:\n{decrypted_string}"),

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
