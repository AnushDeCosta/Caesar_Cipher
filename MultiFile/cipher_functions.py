#
# File     : cipher_functions.py
# Author   : Anush De Costa
# Email ID : deyay064
# Description: Contains functions for encryption, decryption, and brute force decryption using the Caesar Cipher method.
# This is my own work as defined by the University's Academic Misconduct Policy.
#


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
