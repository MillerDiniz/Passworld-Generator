import random
import string

def generate_password(length=12, include_numbers=True, alphanumeric=False):
    """
    Generates a random password.

    Parameters:
    - length (int): Length of the password (default: 12).
    - include_numbers (bool): Include numbers in the password (default: True).
    - alphanumeric (bool): Generate an alphanumeric password (default: False).

    Returns:
    - str: Generated password.
    """
    if alphanumeric:
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

    # Exclude numbers if include_numbers is False
    if not include_numbers:
        characters = ''.join(c for c in characters if c not in string.digits)

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    """
    Main function for user interaction.
    """
    print("Welcome to the Password Generator!")

    # User input
    length = int(input("Enter the desired number of characters: "))
    include_numbers = input("Include numbers in the password? (y/n): ").lower() == 'y'
    alphanumeric = input("Generate an alphanumeric password? (y/n): ").lower() == 'y'

    # Generate and display the password
    new_password = generate_password(length, include_numbers, alphanumeric)
    print("New password:", new_password)

if __name__ == "__main__":
    main()
