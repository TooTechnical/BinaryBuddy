# app.py - Main application entry point
from interface import CLIInterface
from converter import TextConverter
import sys

def main():
    """Initialize and run the application"""
    try:
        converter = TextConverter()
        interface = CLIInterface(converter)
        interface.run()
    except KeyboardInterrupt:
        print("\n\nApplication terminated by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n{CLIInterface.ERROR_COLOR}Fatal Error: {e}{CLIInterface.RESET}")
        sys.exit(1)

if __name__ == "__main__":
    main()
