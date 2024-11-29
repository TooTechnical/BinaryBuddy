# Text to Binary Converter

A simple Python application to convert English text to binary and vice versa.

## View the App

[Click here to use the BinaryBuddy Tool
](https://binarybuddy-469f6feb46e7.herokuapp.com)

## Binary Buddy

**Binary Buddy** is a simple Python program that converts English text to Binary and Binary to English. It's designed for anyone who wants to understand binary encoding or quickly convert between text and binary representations.

## 📋 Features

- **English to Binary Conversion:** Converts any English text into its binary equivalent using ASCII encoding.
- **Binary to English Conversion:** Converts a valid binary string back into readable English text.

## ⚙️ How It Works

### English to Binary
1. Each character of the input text is converted to its ASCII value.
2. The ASCII value is then converted into an 8-bit binary format.

### Binary to English
1. The binary input is divided into chunks of 8 bits.
2. Each 8-bit chunk is converted into its corresponding ASCII character.

## 🧑‍💻 Program Code

```python
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
            print("Invalid binary string. It should be a multiple of 8 bits and contain only 0s and 1s.")
        else:
            text_result = binary_to_text(binary)
            print("English text:", text_result)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
```
## 🛠️ How to Run

- Prerequisites
-Python 3.x must be installed on your system.
-Steps

1. Save the code to a file named binary_buddy.py.
2. Open a terminal or command prompt.
3. Navigate to the folder where the file is saved.
4. Run the program with the command: python binary_buddy.py
   
- Follow the prompts to choose between English-to-Binary or Binary-to-English conversion.

## 🔍 Usage Examples

- Example 1: English to Binary text

- 1. English to Binary
- 2. Binary to English
     
- Enter your choice (1/2): 1
- Enter English text: Hello
- Binary result: 0100100001100101011011000110110001101111
- Example 2: Binary to English text

1. English to Binary
2. Binary to English
- Enter your choice (1/2): 2
- Enter binary string: 0100100001100101011011000110110001101111
- English text: Hello

## 🔒 Input Validation
- English to Binary:
- Accepts any string of English text.
- Binary to English:
- Validates that the input:
- Contains only 0s and 1s.

  
-- Has a length that is a multiple of 8 (since each ASCII character is represented by 8 bits).
-- Invalid inputs will display an appropriate error message.

## 🚧 Limitations

-- Only supports ASCII encoding, which means some extended Unicode characters may not be converted correctly.
-- The binary input must be in multiples of 8 bits to be valid.


## 🚀 Future Enhancements
-- Add Unicode support to handle more characters.
-- Create a Graphical User Interface (GUI) for a better user experience.
-- Add functionality to save the output to a file.
## 📄 License
-- This project is licensed under the MIT License. You are free to use, modify, and distribute it.

## 🤝 Contributing
-- Contributions are welcome! If you have ideas for improvements or find any bugs, feel free to fork the repository and submit a pull request.

## 📧 Contact
For any questions, feedback, or suggestions, feel free to reach out!

Enjoy using Binary Buddy! 🎉



