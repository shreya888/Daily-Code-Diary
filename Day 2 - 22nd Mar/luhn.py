def verify_card_number(card_number):
    """
    Verifies the validity of a credit card number using the Luhn algorithm.

    Args:
        card_number (str): The credit card number to be verified.

    Returns:
        bool: True if the card number is valid, False otherwise.
    """
    # Initialize variables to store sums of odd and even digits
    sum_of_odd_digits = 0
    sum_of_even_digits = 0

    # Reverse the card number for easier processing
    card_number_reversed = card_number[::-1]

    # Extract odd digits from the reversed card number
    odd_digits = card_number_reversed[::2]

    # Calculate sum of odd digits
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    # Extract even digits from the reversed card number
    even_digits = card_number_reversed[1::2]

    # Calculate sum of even digits
    for digit in even_digits:
        # Multiply even digits by 2
        number = int(digit) * 2
        # If the result is two-digit, sum the digits
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number

    # Calculate total sum of digits
    total = sum_of_odd_digits + sum_of_even_digits

    # Check if total sum is divisible by 10
    return total % 10 == 0

def main():
    """
    Main function to verify a credit card number and print the result.
    """
    card_number = '4111-1111-4555-1142'

    # Remove hyphens and spaces from the card number
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    # Verify the card number and print the result
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')
