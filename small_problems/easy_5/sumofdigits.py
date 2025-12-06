"""
PROBLEM:
Write a function that takes one argument, a positive integer, 
and returns the sum of its digits.

EXAMPLE:
print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True

DATA:
- Input: int
- Output: int
- intermediary: string for iterating

ALGORITHM:
- Get the digits into a list
    - Strategy 1:
        - INITIALIZE empty list
        - INITIALIZE empty result variable
        - LOOP through str(num):
            append each character to the empty list
        - LOOP through the list
            - Add int(element) to a result variable
        - RETURN result variable
    - Strategy 2:
        return sum([int(digit) for digit in str(num)])

"""
def sum_digits(num):
    return sum([int(digit) for digit in str(num)])

print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True