#18. What is the difference between a shallow copy and a deep copy? Explain with example?

# The difference between shallow and deep copies lies in how Python handles nested objects (like a list inside another list). 
# When you copy a compound object, the distinction determines whether changes to the "inner" objects affect both the original and the copy.

# 1. Shallow Copy
# A shallow copy creates a new object, but instead of copying the items inside, it simply inserts references to the objects found in the original.

# Behavior: The top-level container is new, but nested elements point to the exact same memory addresses as the original.

# Result: Modifying a nested object in the copy will reflect in the original.

# 2. Deep Copy
# A deep copy creates a new object and recursively copies every object found in the original.

# Behavior: It creates a completely independent clone of the original object and all its children.

# Result: Modifying any part of the copy (even nested elements) will not affect the original.

import copy

# Original list with a nested list
original = [[1, 2, 3], [4, 5, 6]]

# --- Shallow Copy ---
shallow_copy = copy.copy(original)

# --- Deep Copy ---
deep_copy = copy.deepcopy(original)

# Modify a nested element in the shallow copy
shallow_copy[0][0] = 'X'

# Modify a nested element in the deep copy
deep_copy[1][0] = 'Z'

print(f"Original:     {original}")
# Output: [['X', 2, 3], [4, 5, 6]] -> Impacted by shallow copy!

print(f"Shallow Copy: {shallow_copy}")
# Output: [['X', 2, 3], [4, 5, 6]]

print(f"Deep Copy:    {deep_copy}")
# Output: [[1, 2, 3], ['Z', 5, 6]] -> Totally independent