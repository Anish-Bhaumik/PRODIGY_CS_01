def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def print_header():
    header = """
   _____                                  _____  _         _                 
  / ____|                                / ____|(_)       | |                
 | |      __ _   ___  ___   __ _  _ __  | |      _  _ __  | |__    ___  _ __ 
 | |     / _` | / _ \/ __| / _` || '__| | |     | || '_ \ | '_ \  / _ \| '__|
 | |____| (_| ||  __/\__ \| (_| || |    | |____ | || |_) || | | ||  __/| |   
  \_____|\__,_| \___||___/ \__,_||_|     \_____||_|| .__/ |_| |_| \___||_|   
                                                   | |                       
                                                   |_|                       
    """
    print(header)
    print("="*80)

def print_message(label, message):
    print("\n" + "="*80)
    print(f"{label}".center(80))
    print("-" * 80)
    print(message.center(80))
    print("="*80)

def main():
    print_header()

    while True:
        print("Choose an option:")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. Exit")
        
        choice = input("Enter your choice (1, 2, or 3): ")
        
        if choice == '3':
            print("Exiting the program. Goodbye!")
            break
        
        if choice not in ['1', '2']:
            print("Invalid choice! Please choose 1, 2, or 3.")
            continue

        message = input("Enter the message: ")
        
        try:
            shift_value = int(input("Enter the shift value: "))
        except ValueError:
            print("Invalid shift value! Please enter an integer.")
            continue

        if choice == '1':
            encrypted_message = caesar_encrypt(message, shift_value)
            print_message("Encrypted Message", encrypted_message)
        elif choice == '2':
            decrypted_message = caesar_decrypt(message, shift_value)
            print_message("Decrypted Message", decrypted_message)

if __name__ == "__main__":
    main()
