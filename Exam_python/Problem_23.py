# 24. Create a list of strings based on a list of numbers

# The rules:

# * If the number is a multiple of five and odd, the string should be `'five odd'`

# * If the number is a multiple of five and even, the string should be `'five even'`

# * If the number is odd, the string is `'odd'`

# * If the number is even, the string is `'even

def categorize_number(n: int) -> str:
    """Categorizes a number based on divisibility by 5 and parity."""
    is_multiple_of_five = (n % 5 == 0)
    is_even = (n % 2 == 0)

    if is_multiple_of_five:
        return 'five even' if is_even else 'five odd'
    else:
        return 'even' if is_even else 'odd'

# Input list
numbers = [1, 5, 10, 13, 25, 40, 42]

# Create the list of strings
result = [categorize_number(num) for num in numbers]

print(f"Numbers: {numbers}")
print(f"Strings: {result}")