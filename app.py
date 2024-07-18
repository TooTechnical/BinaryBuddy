def text_to_binary(text):
    binary_result = ''.join(format(ord(char), '08b') for char in text)
    return binary_result

def binary_to_text(binary):
    binary_values = [binary[i:i+8] for i in range(0, len(binary), 8)]
    ascii_characters = [chr(int(bv, 2)) for bv in binary_values]
    text_result = ''.join(ascii_characters)
    return text_result

def main():
    print("1. English to Binary")
    print("2. Binary to English")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        text = input("Enter English text: ")
        binary_result = text_to_binary(text)
        print("Binary result:", binary_result)
    elif choice == '2':
        binary = input("Enter binary string: ")
        if len(binary) % 8 != 0 or not all(char in '01' for char in binary):
            print("Invalid binary string. It should be multiple of 8 bits and contain only 0s and 1s.")
        else:
            text_result = binary_to_text(binary)
            print("English text:", text_result)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
