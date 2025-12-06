"""
Create a function that takes a list of integers as an argument. 
Determine and return the index N for which all numbers with an index 
less than N sum to the same value as the numbers with an index 
greater than N. If there is no index that would make this happen, 
return -1.

If you are given a list with multiple answers, return the index 
with the smallest value.

The sum of the numbers to the left of index 0 is 0. Likewise, 
the sum of the numbers to the right of the last element is 0.

PROBLEM:
Write a function that takes a list of integers
Determine the index at which point the numbers before it and the 
numbers after it sum to the same value. Return that "middle" index

RULES:
- If this can't happen return -1 
- All lists are just composed of numbers

EXAMPLE:
# The following tests should each print True.
print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)

DATA:
- Input: List of numbers
- Int
Intermediary: Variables for sum_left and sum_right?

ALGORITHM:
SET *sum_left* and *sum_right* to None
results []

LOOP through the index slots of the list
    SUM indexes [0:idx] and SET to sum_right
    SUM indexes [idx:-1] and SET to sum_right
        IF sum_right == sum_left:
            RETURN the current index


RETURN -1
"""
def equal_sum_index(lst: list) -> int:
    sum_left = ''
    sum_right = ''

    for idx in range(len(lst)):
        sum_left = sum(lst[0:idx])
        sum_right = sum(lst[idx + 1:])

        if sum_left == sum_right:
            return idx
        
    return -1

print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)