import re  # Regular expression module
import secrets  # For generating secure random numbers
import string

def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    """
    Function to generate a random password with specified constraints as args.
    
    Args:
        length (int): Length of the password (default is 16).
        nums (int): Number of digits in the password (default is 1).
        special_chars (int): Number of special characters in the password (default is 1).
        uppercase (int): Number of uppercase letters in the password (default is 1).
        lowercase (int): Number of lowercase letters in the password (default is 1).
        
    Returns:
        str: Generated password that satisfies the given constraints.
    """

    # Define the possible characters for the password
    letters = string.ascii_letters  # All ASCII letters (both lowercase and uppercase)
    digits = string.digits  # All digits
    symbols = string.punctuation  # All punctuation symbols

    # Combine all possible characters to choose from
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)  # Adding random character to password string from the pool of all_characters
        
        # List of constraints with their corresponding regular expressions
        # (Number of _, Regular expression for _)
        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints
        if all(
            constraint <= len(re.findall(pattern, password))  # Counting and checking if occurrences of the pattern in the password to be acceptable
            for constraint, pattern in constraints  # Iterating through each constraint and pattern
        ):
            break  # If all constraints are satisfied, break out of the loop, else make new password via while loop
    
    return password

# Example test
if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)
