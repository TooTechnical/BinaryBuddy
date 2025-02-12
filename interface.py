from colorama import Fore, Style, init


class CLIInterface:
    """Handles user interaction through the command-line interface"""

    def __init__(self, converter):
        init(autoreset=True)
        self.converter = converter

    def display_menu(self):
        """Display the main menu"""
        print(Fore.CYAN + "\n=== BinaryBuddy ===")
        print(Fore.YELLOW + "1. Convert Text to Binary")
        print("2. Convert Binary to Text")
        print("3. Exit" + Style.RESET_ALL)

    def get_sub_choice(self):
        """Get user choice after conversion"""
        print(Fore.CYAN + "\nChoose an action:")
        print(Fore.YELLOW + "1. Convert again")
        print("2. Return to main menu")
        print("3. Exit" + Style.RESET_ALL)
        while True:
            choice = input(Fore.GREEN + "Enter choice (1/2/3): " + Style.RESET_ALL).strip()
            if choice in {"1", "2", "3"}:
                return choice
            print(Fore.RED + "Invalid choice! Please enter 1, 2, or 3." + Style.RESET_ALL)

    def handle_conversion(self, direction: str):
        """Handle conversion flow with post-conversion menu"""
        while True:
            try:
                if direction == "text_to_binary":
                    text = input(Fore.GREEN + "Enter text: " + Style.RESET_ALL).strip()
                    result = self.converter.text_to_binary(text)
                    print(Fore.BLUE + f"Binary: {result}" + Style.RESET_ALL)
                elif direction == "binary_to_text":
                    binary = input(Fore.GREEN + "Enter binary: " + Style.RESET_ALL).strip()
                    result = self.converter.binary_to_text(binary)
                    print(Fore.BLUE + f"Text: {result}" + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

            # Post-conversion menu
            choice = self.get_sub_choice()
            if choice == "2":
                break  # Return to main menu
            elif choice == "3":
                print(Fore.YELLOW + "Goodbye!" + Style.RESET_ALL)
                exit()

    def run(self):
        """Main application loop"""
        while True:
            self.display_menu()
            main_choice = self.get_choice()

            if main_choice == "1":
                self.handle_conversion("text_to_binary")
            elif main_choice == "2":
                self.handle_conversion("binary_to_text")
            elif main_choice == "3":
                print(Fore.YELLOW + "Goodbye!" + Style.RESET_ALL)
                break
