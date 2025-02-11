# interface.py - Handles CLI presentation layer
from colorama import Fore, Style, init

class CLIInterface:
    """Manages command-line interface and user interaction"""
    
    # Color constants
    PROMPT_COLOR = Fore.GREEN
    RESULT_COLOR = Fore.BLUE
    ERROR_COLOR = Fore.RED
    WARNING_COLOR = Fore.YELLOW
    RESET = Style.RESET_ALL
    
    def __init__(self, converter):
        init(autoreset=True)
        self.converter = converter

    def display_header(self):
        """Show application header"""
        print(f"\n{Fore.CYAN}=== Binary Text Converter ===")
        print(f"{Fore.YELLOW}     (Secure UTF-8 Version)     {self.RESET}")

    def get_menu_choice(self):
        """Get validated menu choice from user"""
        while True:
            try:
                self.display_menu_options()
                choice = input(f"{self.PROMPT_COLOR}Enter choice (1-3): {self.RESET}").strip()
                if choice in {'1', '2', '3'}:
                    return choice
                raise ValueError("Invalid menu selection")
            except ValueError as ve:
                print(f"{self.WARNING_COLOR}{ve}{self.RESET}")

    def display_menu_options(self):
        """Show main menu options"""
        print(f"\n{Fore.CYAN}1. English → Binary")
        print(f"2. Binary → English")
        print(f"3. Exit{self.RESET}")

    def handle_conversion(self, direction: str):
        """Handle conversion flow based on direction"""
        try:
            if direction == "text_to_binary":
                input_text = input(f"{self.PROMPT_COLOR}Enter English text: {self.RESET}").strip()
                result = self.converter.text_to_binary(input_text)
                print(f"\n{self.RESULT_COLOR}Binary result: {result}{self.RESET}")
            else:
                input_text = input(f"{self.PROMPT_COLOR}Enter binary string: {self.RESET}").strip()
                result = self.converter.binary_to_text(input_text)
                print(f"\n{self.RESULT_COLOR}English text: {result}{self.RESET}")
        except Exception as e:
            print(f"\n{self.ERROR_COLOR}Error: {e}{self.RESET}")

    def run(self):
        """Main application loop"""
        while True:
            self.display_header()
            choice = self.get_menu_choice()
            
            if choice == '1':
                self.handle_conversion("text_to_binary")
            elif choice == '2':
                self.handle_conversion("binary_to_text")
            elif choice == '3':
                print(f"\n{self.WARNING_COLOR}Exiting... Thank you!{self.RESET}")
                return
                
            input(f"\n{self.PROMPT_COLOR}Press Enter to continue...{self.RESET}")
