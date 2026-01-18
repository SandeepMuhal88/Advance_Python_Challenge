#8. What are the basic data types in Python?
# Float and integers, string, Boolean

#9. How do you convert a string to an integer in Python?
# Typescripting
name='10'
x=int(10)
print(type(x))

#10. How do you check if a string contains a specific substring in Python?
# In Python, there are several ways to check for a substring, depending on whether you need a simple boolean check, 
# the position of the substring, or complex pattern matching.

# 1. The in Operator (Recommended)
# The most "Pythonic" and readable way. It returns a boolean (True or False).
text = "Deep learning is a subset of machine learning."
substring = "machine"

if substring in text:
    print("Substring found!")

# 2. The str.find() Method
# Returns the lowest index of the substring if found, otherwise -1.
index = text.find(substring)
if index != -1:
    print(f"Substring found at index {index}.")
# 3. The str.index() Method
# Similar to find(), but raises a ValueError if the substring is not found.
try:
    index = text.index(substring)
    print(f"Substring found at index {index}.")
except ValueError:
    print("Substring not found.")

# 4. The re Module for Regular Expressions
# For complex pattern matching, use the re module.
import re
pattern = r"machine"
if re.search(pattern, text):
    print("Substring found using regex!")
# Example Outputs:
# Substring found!
# Substring found at index 27.
# Substring found using regex!