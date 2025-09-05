# Task
# The provided code stub reads an integer, , from STDIN. For all non-negative integers , print .

# Example
# a=3

# The list of non-negative integers that are less than n-=3  is(0,1,2) . Print the square of each number on a separate line.


def solution(n):
    for i in range(n):
        print(i**2)


if __name__ == '__main__':

    n = int(input())
    solution(n)
    