# Problem 3: Palindrome Checker
# Description:
# Write a function is_palindrome(s) that takes a string s and checks if it is a palindrome. 
# A palindrome is a word or phrase that reads the same forward and backward
# The check should be case-insensitive and ignore spaces.
# Examples:
# •	is_palindrome("Radar") should return True.
# •	is_palindrome("A man a plan a canal Panama") should return True.
# •	is_palindrome("hello") should return False.


def is_palindrome(s):
    s=s.lower().replace(" ","")
    k=s[::-1]
    if s==k:
        return True
    else:
        return False


print(is_palindrome("Radar"))
print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("hello"))