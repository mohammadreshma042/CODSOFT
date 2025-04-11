import random
import string

def generate_password(length, use_digits, use_symbols, use_upper, use_lower):
    characters = ''
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase

    if not characters:
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_choice(prompt):
    while True:
        choice = input(prompt + " (y/n): ").strip().lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        else:
            print("Please type 'y' or 'n'.")

def main():
    print("\n********** PASSWORD GENERATOR **********\n")
    
    # Get password length
    while True:
        try:
            length = int(input("Enter desired password length (min 4): "))
            if length < 4:
                print("Please enter at least 4 characters.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("\nSelect character types to include:")
    use_digits = get_choice("Include Numbers (0-9)?")
    use_symbols = get_choice("Include Symbols (!@#$...) ?")
    use_upper = get_choice("Include Uppercase Letters (A-Z)?")
    use_lower = get_choice("Include Lowercase Letters (a-z)?")

    print("\nGenerating your password...")

    password = generate_password(length, use_digits, use_symbols, use_upper, use_lower)

    if password:
        print(f"\nYour Secure Password: {password}\n")
    else:
        print("Error: You must select at least one character type.")

    print("\n")

if __name__ == "__main__":
    main()
