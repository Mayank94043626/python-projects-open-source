import random
import string
import os

def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def generate_password(length):
    clear_screen()
    
    # Define character sets for different complexity levels
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    while True:
        complexity = input("Choose complexity (low, medium, high): ").lower()

        if complexity not in ["low", "medium", "high"]:
            print("Invalid choice. Please choose 'low', 'medium', or 'high'.")
            continue

        if complexity == "low":
            character_set = lowercase_chars + digits
        elif complexity == "medium":
            character_set = lowercase_chars + uppercase_chars + digits
        elif complexity == "high":
            character_set = lowercase_chars + uppercase_chars + digits + special_chars

        # Generate the password
        password = ''.join(random.choice(character_set) for _ in range(length))
        
        # Center-align the output
        term_width = os.get_terminal_size().columns
        padding = (term_width - len(password)) // 2
        print(" " * padding + password)
        break

if __name__ == "__main__":
    while True:
        clear_screen()
        length_str = input("Enter the desired length of the password: ")

        if not length_str.isdigit():
            input("Invalid input. Press Enter to continue...")
            continue

        length = int(length_str)

        if length <= 0:
            input("Invalid input. Press Enter to continue...")
            continue

        generate_password(length)

        choice = input("Do you want to generate another password? (yes/no): ").lower()
        if choice != "yes":
            break