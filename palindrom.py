import re

def is_palindrome(phrase):
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    backwards = forwards[::-1]
    return forwards == backwards

print(is_palindrome("This is python"))
print(is_palindrome("level"))
print(is_palindrome("Go hang a salami, I'm a lasagna hog."))
