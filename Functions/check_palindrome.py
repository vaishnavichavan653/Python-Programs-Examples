def is_palindrome(text):
    text = str(text).lower()
    return text == text[::-1]


print("Is madam a palindrome?", is_palindrome("madam"))
