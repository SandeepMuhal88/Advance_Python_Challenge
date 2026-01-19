# 21. Identifying bugs in code

# The following `stripped_reversed_lowercase` function contains at least one bug. You can see this by 
# running the code in the cell below which tests the functionality of the `stripped_reversed_lowercase` function.



# Set trace at the beginning of `stripped_reversed_lowercase` and use debugger to solve the bug(s).
# Execute the code line by line and print variables used in the function to understand what's going wrong

import pdb

def stripped_reversed_lowercase(text):
    # Set trace to start debugging here
    # pdb.set_trace() 
    
    # Bug 1: Strings are immutable; .strip() and .lower() return NEW strings
    text.strip() 
    text.lower()
    
    # Bug 2: Incorrect slicing or logic for reversing
    reversed_text = text[::-1] 
    
    return reversed_text

# Test Case
# Expected: "olleh" | Actual: "  HeLLo  " (if bugs exist)
print(f"Result: '{stripped_reversed_lowercase('  HeLLo  ')}'")


def stripped_reversed_lowercase(text: str) -> str:
    """
    1. Removes leading/trailing whitespace.
    2. Converts to lowercase.
    3. Reverses the string.
    """
    # Fix: Re-assign the transformed string to a variable
    # Method chaining is efficient and readable
    cleaned_text = text.strip().lower()
    
    # Reverse using slicing
    reversed_text = cleaned_text[::-1]
    
    return reversed_text

# --- Verification ---
test_input = "  DataScience  "
result = stripped_reversed_lowercase(test_input)

print(f"Input:  '{test_input}'")
print(f"Output: '{result}'") 
# Output: 'ecneicsatad'