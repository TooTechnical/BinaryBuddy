import sys
import select
from colorama import Fore, Style, init

class CLIInterface:
    def __init__(self, converter):
        init(autoreset=True)
        self.converter = converter

    def display_menu(self):
        print(Fore.CYAN + "\n=== BinaryBuddy ===")
        print(Fore.YELLOW + "1. Convert Text to Binary")
        print("2. Convert Binary to Text")
        print("3. Exit" + Style.RESET_ALL)

    def get_input(self, prompt, timeout=5):
        print(prompt, end='', flush=True)
        rlist, _, _ = select.select([sys.stdin], [], [], timeout)
        if rlist:
            return sys.stdin.readline().strip()
        return None

    def get_sub_choice(self):
        print(Fore.CYAN + "\nChoose an action:")
        print(Fore.YELLOW + "1. Convert again")
        print("2. Return to main menu")
        print("3. Exit" + Style.RESET_ALL)
        
        choice = self.get_input(Fore.GREEN + "Enter choice (1/2/3): " + Style.RESET_ALL)
        if choice in {"1", "2", "3"}:
            return choice
        return None

    def handle_conversion(self, direction: str):
        while True:
            try:
                if direction == "text_to_binary":
                    text = self.get_input(Fore.GREEN + "Enter text: " + Style.RESET_ALL)
                    if text is None:
                        print("\nNo input received. Returning to main menu...")
                        return
                    result = self.converter.text_to_binary(text)
                    print(Fore.BLUE + f"Binary: {result}" + Style.RESET_ALL)
                elif direction == "binary_to_text":
                    binary = self.get_input(Fore.GREEN + "Enter binary: " + Style.RESET_ALL)
                    if binary is None:
                        print("\nNo input received. Returning to main menu...")
                        return
                    result = self.converter.binary_to_text(binary)
                    print(Fore.BLUE + f"Text: {result}" + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

            choice = self.get_sub_choice()
            if choice == "2" or choice is None:
                break
            elif choice == "3":
                print(Fore.YELLOW + "Goodbye!" + Style.RESET_ALL)
                sys.exit(0)

    def run(self):
        if not sys.stdin.isatty():
            print("Non-interactive session detected. Exiting...")
            sys.exit(0)

        while True:
            self.display_menu()
            main_choice = self.get_sub_choice()

            if main_choice == "1":
                self.handle_conversion("text_to_binary")
            elif main_choice == "2":
                self.handle_conversion("binary_to_text")
            elif main_choice == "3" or main_choice is None:
                print(Fore.YELLOW + "Goodbye!" + Style.RESET_ALL)
                break
