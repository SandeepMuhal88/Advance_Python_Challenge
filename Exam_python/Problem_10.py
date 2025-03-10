# 11. Fill the missing pieces of the `count_even_numbers` function

# Fill `____` pieces of the `count_even_numbers` implemention in order to pass the assertions. You can assume that `numbers` argument is a list of integers.

 

# ____ count_even_numbers(numbers):

#     count = 0

#     for num in ____:

#         if ____ % 2 == ____:

#             count += ____

#     _____ _____

def count_even_numbers(numbers):
    count=0
    for num in numbers:
        if num%2==0:
            count+=1
    return count


def something(number):
    if number%2==0:
        if number==0:
            return False
        return True
    else:
        return False
    
# Example usage
# print(count_even_numbers([12,63,8,5,12,10])) # should print 3

print(something(0)) # should print True

# Shorthing the code
def sort_numbers(l1):
    l1.sort()
    return l1

print(sort_numbers([12,63,8,5,12,10])) # should print 3