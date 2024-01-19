"""
Palindrome Checker problem
-solved by Dewan
"""

def is_palindrome(string):
    # Convert to lowercase and remove anything without characters
    clean_string = ''.join(char.lower() for char in string if char.isalnum())

    # Compare with reverse string
    return clean_string == clean_string[::-1]


print(is_palindrome("A man, a plan, a canal, Panama"))
print(is_palindrome("Hello"))
