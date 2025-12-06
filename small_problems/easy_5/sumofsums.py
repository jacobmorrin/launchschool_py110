"""
Write a function that takes a list of numbers and returns the sum 
of the sums of each leading subsequence in that list. Examine the 
examples to see what we mean. You may assume that the list always
 contains at least one number.

PROBLEM:
Write a function that takes a list of numbers, and returns
the sum of sums for each leading sequnce in the list.

For example, if you had a list [3, 5, 3] the result would be 
(3 + (3+5) + (3+5+8))

EXAMPLE:
print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

Conceptually:
0 index
0-1 indidces
0-2 indices
0-3 indices

print(sum_of_sums([4]) == 4)   

Data:
Input: List of ints
Output: Ints
Intermediary: need a variable to capture consecutive sums

ALGORITHM:
- DEFINE the function sum_of_sums(lst: list) -> int:
- SET result to 0
- LOOP through the list by index 
- Use sum and slicing to take the sum of the indexes from 0 -> current index
- ADD that number to result
- RETURN result

"""
# Solution 1: Inefficient
def sum_of_sums(lst: list) -> int:
    result = 0
    for idx in range(len(lst) + 1):
        result += sum(lst[0:idx])
    return result

#Solution 2: More Efficien
def sum_of_sums2(lst: list) -> int:
    result = 0
    running_total = 0
    for num in lst:
        running_total += num
        result += running_total
    return result

print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums2([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums2([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums2([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35