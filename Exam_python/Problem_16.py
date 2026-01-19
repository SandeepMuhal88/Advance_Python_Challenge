#17. Explain the two methods used to delete a file from os using python, with example code.
# 1. The Methods: os.remove() and os.unlink()
# Both functions delete a file path. If the path points to a directory instead of a file, both will 
# raise an IsADirectoryError (on Linux/macOS) or an OSError.

# Method A: os.remove()
# This is the most common and "Pythonic" name for the operation. It is generally the go-to choice for readability.

# Method B: os.unlink()
# This is the Unix-style name for deleting a file. In Unix-like systems, deleting a file is technically "unlinking" 
# the file name from the data on the storage disk.

# 2. Implementation with Error Handling
# When deleting files, it is a best practice to use a try-except block or check for the file's 
# existence using os.path.exists() to prevent the program from crashing if the file is missing.

import os

file_path = "example_data.csv"

# --- Method 1: Using os.remove() ---
try:
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Successfully deleted {file_path} using os.remove()")
    else:
        print("The file does not exist.")
except PermissionError:
    print("Error: You do not have permission to delete this file.")
except Exception as e:
    print(f"An error occurred: {e}")

# --- Method 2: Using os.unlink() ---
# (Logic is identical; often used by developers coming from C/Unix backgrounds)
try:
    # Creating a dummy file to demonstrate
    with open("temp_log.txt", "w") as f:
        f.write("Temporary data")
        
    os.unlink("temp_log.txt")
    print("Successfully deleted temp_log.txt using os.unlink()")
except OSError as e:
    print(f"Error: {e.strerror}")


from pathlib import Path

file_to_delete = Path("results.json")

# Missing_ok=True prevents an error if the file is already gone
file_to_delete.unlink(missing_ok=True)