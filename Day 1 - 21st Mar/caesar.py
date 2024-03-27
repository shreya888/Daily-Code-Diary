text = 'Hello Zaira'  # Original text to be encrypted using Caesar cipher
shift = 3  # Shift value for encryption

# Function to perform Caesar encryption
def caesar(message: str, offset: int) -> str:
    """
    Encrypts a message using the Caesar cipher.

    Args:
        message (str): The message to be encrypted.
        offset (int): The shift value for encryption.

    Returns:
        str: The encrypted message.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  # Define the alphabet
    encrypted_text = ''  # Initialize the encrypted text
    
    for char in message.lower():
        if char == ' ':  # Preserve spaces in the message
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    
    return encrypted_text

# Example usage
print(f'Original text: {text}, Shift: {shift}')
encryption = caesar(text, shift)
print(f'Encrypted text: {encryption}')

# Decrypting using Caesar cipher with a shift of 3 in opposite direction
decryption = caesar(encryption, -1*shift)
print(f'Decrypted text: {decryption}')
