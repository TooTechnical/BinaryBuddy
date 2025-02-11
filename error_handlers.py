# error_handlers.py - Custom exceptions and error handling utilities
from colorama import Fore, Style
import datetime

class ApplicationError(Exception):
    """Base class for application exceptions"""
    def __init__(self, message="An application error occurred"):
        self.message = message
        self.timestamp = datetime.datetime.now().isoformat()
        super().__init__(self.message)

class ConversionError(ApplicationError):
    """Raised when text/binary conversion fails"""
    def __init__(self, original_error=None):
        message = "Failed to complete conversion: Invalid input format"
        super().__init__(message)
        self.original_error = original_error

class InputValidationError(ApplicationError):
    """Raised when user input fails validation checks"""
    def __init__(self, field_name, expected_format):
        message = (f"Invalid {field_name} input. "
                   f"Expected format: {expected_format}")
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

def handle_errors(func):
    """Decorator for consistent error handling across the application"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ApplicationError as e:
            print(f"\n{Fore.RED}ERROR: {e.message}{Style.RESET_ALL}")
            log_error(e)
        except Exception as e:
            print(f"\n{Fore.RED}CRITICAL: Unexpected error - {str(e)}{Style.RESET_ALL}")
            log_error(e)
    return wrapper

def log_error(error: Exception):
    """Log errors with timestamp and context"""
    error_log = (
        f"\n--- ERROR LOG ---\n"
        f"Timestamp: {datetime.datetime.now().isoformat()}\n"
        f"Error Type: {type(error).__name__}\n"
        f"Message: {str(error)}\n"
    )
    if hasattr(error, 'original_error'):
        error_log += f"Original Error: {str(error.original_error)}\n"
    print(f"{Fore.YELLOW}{error_log}{Style.RESET_ALL}")
