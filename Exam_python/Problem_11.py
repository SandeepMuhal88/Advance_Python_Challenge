# 12. Counting average length of words in a sentence

# Create a function `average_length_of_words` which takes a string as an argument and returns the average length of the words
# in the string. You can assume that there is a single space between each word and that the input does not have punctuation.
def average_length_of_words(sentence: str) -> float:
    """
    Calculates the average length of words in a string.
    Assumes single spaces and no punctuation.
    """
    # 1. Split the sentence into a list of words
    words = sentence.split()
    
    # Handle empty string case to avoid DivisionByZero
    if not words:
        return 0.0
    
    # 2. Sum the lengths of all words
    total_chars = sum(len(word) for word in words)
    
    # 3. Calculate average
    average = total_chars / len(words)
    
    return average

# --- Testing ---
example_sentence = "Deep Learning is fascinating"
result = average_length_of_words(example_sentence)

print(f"Sentence: '{example_sentence}'")
print(f"Average word length: {result:.2f}") 
# (4 + 8 + 2 + 11) / 4 = 25 / 4 = 6.25