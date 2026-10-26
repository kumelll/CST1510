
def is_palindrome(text):
    """Check if the text reads the same backwards."""
    text = text.lower()
    return text == text[::-1]


word = input("Enter a word: ")

if is_palindrome(word):
    print("True")
else:
    print("False")
