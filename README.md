
# PRODIGY_CS_01 - Caesar Cipher Program

Description: This repository contains a Python script that implements the Caesar Cipher algorithm, which is a basic encryption technique used to encode and decode messages. This script is part of Task 1 for the Prodigy InfoTech Cybersecurity Internship.

The Caesar Cipher works by shifting each letter in the plaintext by a fixed number of positions down or up the alphabet. This script allows users to perform encryption and decryption operations based on user input.


## Features

- Encrypt Text: Convert plaintext to ciphertext using a specified shift value.
- Decrypt Text: Convert ciphertext back to plaintext using the same shift value.
- User-Friendly Interface: Provides an interactive menu for easy operation.


## Getting Started

Follow these steps to get the Caesar Cipher program up and running on your local machine.
## Prerequisites
- Python 3.x: Ensure Python 3 is installed on your system. You can download it from https://www.python.org/.
## Installation

1. Clone the Repository:

```bash
  https://github.com/Anish-Bhaumik/PRODIGY_CS_01.git
```
2. Navigate to the Project Directory:

```bash
cd PRODIGY_CY_01

```
    
## Running the Program
1. Execute the Script:
```bash
python3 caesar_cipher.py
```
2. Interactive Menu:
- You will see three options:
   1. Encrypt text: Enter the message and shift value to get the encrypted text.
   2. Decrypt text: Enter the message and shift value to get the decrypted text.
   3. Exit: Exit the program.
## Usage/Examples
1. Encrypting a message:

```plaintext
   _____                                  _____  _         _                 
  / ____|                                / ____|(_)       | |                
 | |      __ _   ___  ___   __ _  _ __  | |      _  _ __  | |__    ___  _ __ 
 | |     / _` | / _ \/ __| / _` || '__| | |     | || '_ \ | '_ \  / _ \| '__|
 | |____| (_| ||  __/\__ \| (_| || |    | |____ | || |_) || | | ||  __/| |   
  \_____|\__,_| \___||___/ \__,_||_|     \_____||_|| .__/ |_| |_| \___||_|   
                                                   | |                       
                                                   |_|                       
    
================================================================================

Choose an option:
1. Encrypt text
2. Decrypt text
3. Exit
Enter your choice (1, 2, or 3): 1
Enter the message: Hello everyone
Enter the shift value: 3

================================================================================
                               Encrypted Message                                
--------------------------------------------------------------------------------
                                 Khoor hyhubrqh                                 
================================================================================

```

2. Decrypting a Message:
```plaintext
Choose an option:
1. Encrypt text
2. Decrypt text
3. Exit
Enter your choice (1, 2, or 3): 2
Enter the message: Khoor hyhubrqh
Enter the shift value: 3

================================================================================
                               Decrypted Message                                
--------------------------------------------------------------------------------
                                Hello everyone                                  
================================================================================
```
## Code Overview
- caesar_encrypt(text, shift): Encrypts the given text by shifting characters by the shift value.
- caesar_decrypt(text, shift): Decrypts the given text by shifting characters in the opposite direction.
- print_header(): Displays the header and program title in a stylized ASCII art format.
- print_message(label, message): Prints the encrypted or decrypted message with a label.
- main(): Runs the interactive menu allowing users to choose between encryption, decryption, or exit.