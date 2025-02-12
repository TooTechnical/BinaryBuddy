from interface import CLIInterface
from converter import TextConverter


def main():
    """Main entry point for the application"""
    converter = TextConverter()
    interface = CLIInterface(converter)
    interface.run()


if __name__ == "__main__":
    main()
