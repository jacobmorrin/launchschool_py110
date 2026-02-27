"""
PROBLEM:
Create a function that takes a list of integers as an argument and returns 
a tuple of two numbers that are closest together in value. 

RULES:
If there are multiple pairs that are equally close, return the pair 
that occurs first in the list.

EXAMPLE:
print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))

DATA:
input: list
output: tuple

ALGORITHM:
want to use a variable for the different and the tuple and update that based on our conditions.


Loop through the numbers

"""
def closest_numbers(lst):
    min_difference = abs(lst[0] - lst[1])
    result = (lst[0] - lst[1])

    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            diff = abs(lst[i] - lst[j])
            if diff < min_difference:
                min_difference = diff
                result = (lst[i], lst[j])
                
    return result

print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))