import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def text_to_binary(text):
    try:
        binary_result = ''.join(format(ord(char), '08b') for char in text)
        return binary_result
    except Exception as e:
        print(Fore.RED + f"Error converting text to binary: {e}" + Style.RESET_ALL)
        return None

def binary_to_text(binary):
    try:
        if len(binary) % 8 != 0 or not all(char in '01' for char in binary):
            raise ValueError("Invalid binary string. It should be multiple of 8 bits and contain only 0s and 1s.")
        binary_values = [binary[i:i+8] for i in range(0, len(binary), 8)]
        ascii_characters = [chr(int(bv, 2)) for bv in binary_values]
        text_result = ''.join(ascii_characters)
        return text_result
    except ValueError as ve:
        print(Fore.YELLOW + f"Validation Error: {ve}" + Style.RESET_ALL)
        return None
    except Exception as e:
        print(Fore.RED + f"Error converting binary to text: {e}" + Style.RESET_ALL)
        return None

def get_user_choice():
    while True:
        print(Fore.CYAN + "1. English to Binary" + Style.RESET_ALL)
        print(Fore.CYAN + "2. Binary to English" + Style.RESET_ALL)
        print(Fore.CYAN + "3. Exit" + Style.RESET_ALL)
        choice = input(Fore.GREEN + "Enter your choice (1/2/3): " + Style.RESET_ALL)
        if choice in ['1', '2', '3']:
            return choice
        print(Fore.RED + "Invalid choice. Please enter 1, 2, or 3." + Style.RESET_ALL)

def english_to_binary():
    text = input(Fore.GREEN + "Enter English text: " + Style.RESET_ALL)
    binary_result = text_to_binary(text)
    if binary_result:
        print(Fore.BLUE + "Binary result: " + binary_result + Style.RESET_ALL)

def binary_to_english():
    binary = input(Fore.GREEN + "Enter binary string: " + Style.RESET_ALL)
    text_result = binary_to_text(binary)
    if text_result:
        print(Fore.BLUE + "English text: " + text_result + Style.RESET_ALL)

def main():
    while True:
        clear_screen()
        choice = get_user_choice()

        if choice == '1':
            english_to_binary()
        elif choice == '2':
            binary_to_english()
        elif choice == '3':
            print(Fore.YELLOW + "Thank you for using the converter. Goodbye!" + Style.RESET_ALL)
            break

        input(Fore.GREEN + "\nPress Enter to continue..." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
