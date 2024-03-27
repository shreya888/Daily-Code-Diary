text = 'mrttaqrhknsw ih puggrur'  # Original text to be encrypted and decrypted
custom_key = 'happycoding'  # Custom key used for encryption and decryption

# Function to perform Vigenere encryption or decryption
def vigenere(message: str, key: str, direction: int = 1) -> str:
    """
    Encrypts or decrypts a message using the Vigenere cipher.

    Args:
        message (str): The message to be encrypted or decrypted.
        key (str): The key used for encryption or decryption.
        direction (int, optional): The direction of encryption/decryption. Defaults to 1 (encryption).

    Returns:
        str: The encrypted or decrypted message.

    Raises:
        ValueError: If the message or key is empty.
    """
    if not message or not key:
        raise ValueError("Message and key cannot be empty.")
    
    key_index = 0  # Initialize index to track position in the key
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  # Define the alphabet
    final_message = ''  # Initialize the final message
    
    # Iterate through each character in the message
    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

# Function to encrypt a message using Vigenere cipher
def encrypt(message: str, key: str) -> str:
    """
    Encrypts a message using the Vigenere cipher.

    Args:
        message (str): The message to be encrypted.
        key (str): The key used for encryption.

    Returns:
        str: The encrypted message.
    """
    return vigenere(message, key)

# Function to decrypt a message using Vigenere cipher
def decrypt(message: str, key: str) -> str:
    """
    Decrypts a message using the Vigenere cipher.

    Args:
        message (str): The message to be decrypted.
        key (str): The key used for decryption.

    Returns:
        str: The decrypted message.
    """
    return vigenere(message, key, -1)

# Example usage
print(f'\nOriginal text: {text}')
print(f'Key: {custom_key}')
encryption = encrypt(text, custom_key)
print(f'\nEncrypted text: {encryption}')
decryption = decrypt(encryption, custom_key)
print(f'Decrypted text: {decryption}\n')
