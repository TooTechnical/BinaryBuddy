# converter.py - Handles conversion logic and validation
import re

class ConversionError(Exception):
    """Base class for conversion errors"""
    pass

class TextConverter:
    """Handles text-binary conversions with validation"""
    
    BINARY_PATTERN = re.compile(r'^[01]{8}+$')  # Matches groups of 8 binary digits
    
    @staticmethod
    def text_to_binary(text: str) -> str:
        """
        Convert UTF-8 text to binary string
        Args:
            text: Input string to convert
        Returns:
            Binary string representation
        Raises:
            ConversionError: On empty input or conversion failure
        """
        if not text:
            raise ConversionError("Input text cannot be empty")
            
        try:
            return ''.join(f"{ord(char):08b}" for char in text)
        except Exception as e:
            raise ConversionError(f"Conversion failed: {str(e)}") from e

    @staticmethod
    def binary_to_text(binary: str) -> str:
        """
        Convert binary string to UTF-8 text
        Args:
            binary: Binary string (must be multiples of 8 bits)
        Returns:
            Decoded text string
        Raises:
            ConversionError: On invalid binary format
        """
        binary = binary.strip().replace(" ", "")
        
        if not TextConverter.BINARY_PATTERN.match(binary):
            raise ConversionError("Invalid binary format - must contain only 0s and 1s in groups of 8")
            
        try:
            return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))
        except Exception as e:
            raise ConversionError(f"Decoding failed: {str(e)}") from e
