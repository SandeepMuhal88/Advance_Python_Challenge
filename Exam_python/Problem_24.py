#25. Write a Python program to count the number of strings where the string length is
# 2 or more and the first and last character are same from a given list of strings.

def count_matching_strings(strings: list[str]) -> int:
    """
    Counts strings where length >= 2 and the first and last characters are identical.
    """
    count = 0
    
    for s in strings:
        # Check if length is at least 2 AND first char matches last char
        # Index 0 is the first, index -1 is the last
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1
            
    return count

# --- Example Usage ---
sample_list = ['abc', 'xyz', 'aba', '1221', 'bh', 'a']
result = count_matching_strings(sample_list)

print(f"List: {sample_list}")
print(f"Count: {result}") 
# Matches: 'aba' (len 3, a==a) and '1221' (len 4, 1==1)