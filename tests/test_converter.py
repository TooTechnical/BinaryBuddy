import pytest
from converter import TextConverter, ConversionError


class TestTextConverter:
    """Unit tests for TextConverter"""

    def test_text_to_binary_valid(self):
        assert TextConverter.text_to_binary("A") == "01000001"
        assert TextConverter.text_to_binary("Hi") == "0100100001101001"

    def test_binary_to_text_valid(self):
        assert TextConverter.binary_to_text("01000001") == "A"
        assert TextConverter.binary_to_text("0100100001101001") == "Hi"

    def test_invalid_binary_length(self):
        with pytest.raises(ConversionError) as e:
            TextConverter.binary_to_text("0100000")
        assert "multiple of 8" in str(e.value)

    def test_invalid_binary_chars(self):
        with pytest.raises(ConversionError) as e:
            TextConverter.binary_to_text("0100000a")
        assert "must contain only 0s and 1s" in str(e.value)

    def test_empty_text_input(self):
        with pytest.raises(ConversionError) as e:
            TextConverter.text_to_binary("")
        # Assert that the exception message matches
        assert "Input text cannot be empty" in str(e.value)
