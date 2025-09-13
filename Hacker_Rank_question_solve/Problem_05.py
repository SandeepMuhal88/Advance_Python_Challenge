def is_leap(year):
    """
    Determines if a given year is a leap year based on the Gregorian calendar rules.

    A year is a leap year if it is evenly divisible by 4, except for century years
    (years ending in 00), which must be evenly divisible by 400.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """

    # Then, check for the two exceptions:
    # 1. It is NOT divisible by 100.
    # 2. It is divisible by 400.

    # conditions are met).
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


if __name__ == '__main__':

    years_to_test = [1900, 2000, 2023, 2024, 2100, 2400]
    for y in years_to_test:
        print(f"Is {y} a leap year? {is_leap(y)}")

year = int(input())
print(is_leap(year))