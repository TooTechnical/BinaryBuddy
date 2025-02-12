

class ApplicationError(Exception):
    """Base class for application exceptions"""

    def __init__(self, message="An application error occurred"):
        self.message = message
        super().__init__(self.message)


class ConversionError(ApplicationError):
    """Raised when text/binary conversion fails"""

    def __init__(self, message="Conversion failed"):
        super().__init__(message)


class InputValidationError(ApplicationError):
    """Raised when user input fails validation checks"""

    def __init__(self, field_name, expected_format):
        message = (
            f"Invalid {field_name} input. Expected format: {expected_format}"
        )
        super().__init__(message)


class BinaryValidationError(InputValidationError):
    """Raised for specific binary input validation failures"""

    def __init__(self, issue_type):
        issues = {
            'length': "Binary length must be divisible by 8",
            'chars': "Only 0 and 1 characters allowed",
            'empty': "Binary input cannot be empty"
        }
        super().__init__("binary", issues[issue_type])


class TextValidationError(InputValidationError):
    """Raised for specific text input validation failures"""

    def __init__(self, issue_type):
        issues = {
            'empty': "Text input cannot be empty",
            'invalid_chars': "Contains non-UTF8 characters"
        }
        super().__init__("text", issues[issue_type])
