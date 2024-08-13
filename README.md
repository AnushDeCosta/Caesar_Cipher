# Caesar Cipher Program

![caesar-cipher](https://upload.wikimedia.org/wikipedia/commons/4/4a/Caesar_cipher_left_shift_of_3.svg)

## Summary
The Caesar Cipher Program provides tools for encryption and decryption using the Caesar Cipher technique. This project includes functionalities to encrypt strings, decrypt strings, and perform brute force decryption. The program is written in Python and adheres to the PEP 8 style guide.

## Introduction
The Caesar Cipher Program aims to offer a comprehensive solution for encrypting and decrypting text using the Caesar Cipher method. This project covers the following functionalities:
- Encrypting a string
- Decrypting a string
- Brute force decryption

Each functionality is implemented in separate modules to maintain a clear and organized code structure. The project adheres to Python best practices and the PEP 8 style guide.

## Encryption and Decryption
The program allows users to:
- **Encrypt a string**: Enter a string and an offset value to encrypt the string using the Caesar Cipher method.
- **Decrypt a string**: Enter a cipher text and an offset value to decrypt the string using the Caesar Cipher method.
- **Brute force decryption**: Enter a cipher text and attempt to decrypt it using all possible offsets within the range.

### Encryption
The encryption process involves shifting each character in the input string by a specified offset within the ASCII range. The encrypted string is then returned.

### Decryption
The decryption process involves shifting each character in the cipher text by the negative of the specified offset within the ASCII range. The decrypted string is then returned.

### Brute Force Decryption
Brute force decryption attempts to decrypt the cipher text using all possible offsets within the specified range, displaying the results for each offset.

## Tools
* Python 3.x
* VSCode or any other Python IDE

## Files
* `deyay064_encryptor.py` - The main driver program for the Caesar Cipher assignment, coordinating all functionalities.
* `display_details.py` - Contains the function to display author details.
* `menu_functions.py` - Contains functions for displaying the menu and handling user input.
* `cipher_functions.py` - Contains functions for encryption, decryption, and brute force decryption using the Caesar Cipher method.


## Usage
To run the program, execute the `deyay064_encryptor.py` file:

\```sh
python deyay064_encryptor.py
\```


## Acknowledgements
Thanks to the instructor and course materials for the guidance and recommendations on best practices and PEP 8 compliance.

