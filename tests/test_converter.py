# tests/test_converter.py
import pytest

# To (project root relative import):
from ..converter import TextConverter  # Relative import from parent directory
class TestTextConverter:
    """Unit tests for text-binary conversion functionality"""
    
    def test_text_to_binary_valid(self):
        """Test valid text to binary conversion (LO5.1)"""
        assert TextConverter.text_to_binary("A") == "01000001"
        assert TextConverter.text_to_binary("Hi") == "0100100001101001"
        
    def test_binary_to_text_valid(self):
        """Test valid binary to text conversion (LO5.1)"""
        assert TextConverter.binary_to_text("01000001") == "A"
        assert TextConverter.binary_to_text("0100100001101001") == "Hi"
        
    def test_invalid_binary_length(self):
        """Test binary length validation (LO7.1)"""
        with pytest.raises(ValueError) as e:
            TextConverter.binary_to_text("0100000")
        assert "multiple of 8" in str(e.value)
        
    def test_invalid_binary_chars(self):
        """Test binary character validation (LO2.1)"""
        with pytest.raises(ValueError) as e:
            TextConverter.binary_to_text("0100000a")
        assert "0s and 1s" in str(e.value)
        
    def test_empty_text_input(self):
        """Test empty text input handling (LO2.1)"""
        with pytest.raises(ValueError) as e:
            TextConverter.text_to_binary("")
        assert "cannot be empty" in str(e.value)

if __name__ == "__main__":
    pytest.main()
