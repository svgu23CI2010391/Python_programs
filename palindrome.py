#20.Develop a function to check whether a string is a palindrome.

def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]

print(is_palindrome("ABA"))