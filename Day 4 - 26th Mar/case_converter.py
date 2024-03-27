def convert_to_snake_case(pascal_or_camel_cased_string):
    """
    Converts a PascalCase or camelCase string to snake_case.

    Args:
        pascal_or_camel_cased_string (str): The input string in PascalCase or camelCase.

    Returns:
        str: The input string converted to snake_case.
    """
    # Create a list of characters where uppercase letters are prefixed with an underscore and converted to lowercase
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]
    
    # Join the list of characters into a single string and strip leading/trailing underscores
    return ''.join(snake_cased_char_list).strip('_')

def main():
    """
    Main function to demonstrate conversion of camelCase and PascalCase strings to snake_case.
    """
    # Test conversions and print results
    print(convert_to_snake_case('iAmACamelCasedString'))
    print(convert_to_snake_case('IAmAPascalCasedString'))

if __name__ == '__main__':
    main()
