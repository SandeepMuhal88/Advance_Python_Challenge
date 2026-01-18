#5. What are parameters in Python?

# 1. Parameters vs. Arguments
# While often used interchangeably, there is a technical distinction:

# Parameter s: Defined in the function signature (the "blueprint").

# Arguments: The actual values passed to the function during execution.

def greet(name):  # 'name' is a parameter
    print(f"Hello, {name}!")

greet("Alice")    # "Alice" is an argument


# Types of Parameters
# Python provides several ways to define parameters, offering flexibility in how functions handle input.

# A. Positional Parameters

def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet("Hamster", "Harry")

def complex_func(pos_only, /, standard, *, kw_only):
    print(pos_only, standard, kw_only)

# Valid call:
complex_func(1, 2, kw_only=3) 
# OR
complex_func(1, standard=2, kw_only=3)

# Invalid call:
# complex_func(pos_only=1, ...) -> Raises TypeError
