import re


class ConversionError(Exception):
    """Custom exception for conversion errors"""

    def __init__(self, message="Conversion error occurred"):
        super().__init__(message)


class TextConverter:
    """Handles core conversion logic with validation"""

    # Regex to validate binary strings (only 0s and 1s)
    BINARY_PATTERN = re.compile(r'^[01]+$')

    @staticmethod
    def text_to_binary(text: str) -> str:
        """
        Convert text to binary string
        Args:
            text: Input string to convert
        Returns:
            Binary string representation
        Raises:
            ConversionError: If input is invalid
        """
        if not text:
            raise ConversionError("Input text cannot be empty")
        return ''.join(f"{ord(char):08b}" for char in text)

    @staticmethod
    def binary_to_text(binary: str) -> str:
        """
        Convert binary string to text
        Args:
            binary: Binary string (must be multiples of 8 bits)
        Returns:
            Decoded text string
        Raises:
            ConversionError: If input is invalid
        """
        binary = binary.strip().replace(" ", "")

        # Validate that the string contains only 0s and 1s
        if not TextConverter.BINARY_PATTERN.match(binary):
            raise ConversionError(
                "Invalid binary format - must contain only 0s and 1s"
            )

        # Validate that the length is a multiple of 8
        if len(binary) % 8 != 0:
            raise ConversionError("Binary length must be a multiple of 8")

        # Convert binary to text
        return ''.join(
            chr(int(binary[i:i + 8], 2)) for i in range(0, len(binary), 8)
        )
