#
#  File     : deyay064_encryptor.py
# Author   : Anush De Costa
# Stud ID  : 110454712
# Email ID : deyay064@mymail.unisa.edu.au
# Description: Programming Assignment 2 – Caesar Cipher
# This is my own work as defined by the University's Academic Misconduct Policy.
#

# Validating User Input

def display_menu():
    print("\n*** Menu ***\n")
    print("1. Encrypt string")
    print("2. Decrypt string")
    print("3. Brute force decryption")
    print("4. Quit")


def get_menu_choice():
    choice = input("\nWhat would you like to do [1,2,3,4]? ")
    while choice not in ['1', '2', '3', '4']:
        print("Invalid choice, please enter either 1, 2, 3, or 4.")
        choice = input("\nWhat would you like to do [1,2,3,4]? ")
    return choice


def get_offset(min_offset, max_offset):
    offset = input(f"Please enter offset value ({min_offset} to {max_offset}): ")
    while not offset.isdigit() or int(offset) < min_offset or int(offset) > max_offset:
        offset = input(f"Please enter offset value ({min_offset} to {max_offset}): ")
    return int(offset)


def get_encryption_input(min_offset, max_offset):
    user_string = input("\nPlease enter string to encrypt: ")
    offset = get_offset(min_offset, max_offset)
    return user_string, offset


def get_decryption_input(min_offset, max_offset):
    cipher_text = input("\nPlease enter the string to decrypt: ")
    offset = get_offset(min_offset, max_offset)
    return cipher_text, offset


def get_brute_force_input():
    return input("\nPlease enter string to decrypt: ")


def brute_force_decrypt(cipher_text, min_offset, max_offset, min_ascii, max_ascii):
    for offset in range(min_offset, max_offset + 1):
        decrypted_string = decrypt_string(
            cipher_text, offset, min_ascii, max_ascii)
        print(f"Offset {offset}: {decrypted_string}")


def encrypt_string(user_string, offset, min_ascii, max_ascii):
    encrypted_string = ""
    for char in user_string:
        ascii_value = ord(char)
        new_ascii_value = ascii_value + offset
        if new_ascii_value > max_ascii:
            new_ascii_value = min_ascii + (new_ascii_value - max_ascii - 1)
        encrypted_string += chr(new_ascii_value)
    return encrypted_string


def decrypt_string(cipher_text, offset, min_ascii, max_ascii):
    decrypted_string = ""
    for char in cipher_text:
        ascii_value = ord(char)
        new_ascii_value = ascii_value - offset
        if new_ascii_value < min_ascii:
            new_ascii_value = max_ascii - (min_ascii - new_ascii_value - 1)
        decrypted_string += chr(new_ascii_value)
    return decrypted_string


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
            print(f"\nEncrypted string:\n{encrypted_string}")
        elif choice == '2':
            encrypted_string, offset = get_decryption_input(
                min_offset, max_offset)
            decrypted_string = decrypt_string(
                encrypted_string, offset, min_ascii, max_ascii)
            print(f"\nDecrypted string:\n{decrypted_string}"),
        elif choice == '3':
            cipher_text = get_brute_force_input()
            brute_force_decrypt(cipher_text, min_offset,
                                max_offset, min_ascii, max_ascii)
        elif choice == '4':
            print("\nGoodbye.\n")
            keep_running = False


if __name__ == "__main__":
    main()
