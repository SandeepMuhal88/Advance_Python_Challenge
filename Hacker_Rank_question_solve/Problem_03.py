# Task
# The provided code stub reads two integers,  and , from STDIN.

# Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .

# No rounding or formatting is necessary.

# Example


# The result of the integer division .
# The result of the float division is .

def solution(a,b):
    print(a//b)
    print(a/b)
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    solution(a,b)