"""
PROBLEM:
Create a function that takes a list of numbers as an argument. 
For each number, determine how many numbers in the list are smaller than it, 
and place the answer in a list. Return the resulting list.

RULES:
When counting numbers, only count unique values. That is, if a number occurs multiple times in the list, it should only be counted once.

EXAMPLE:
print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])

DATA:
Input: List
Output: List
Set: Maybe? Getting unique numbers could be useful

ALGORITHM:
- Set a counter variable to zero
- Get a set of the numbers

"""
def smaller_numbers_than_current(lst):
    unique = set(lst)
    result = []
    count = 0

    for num in lst:
        for unique_num in unique:
            if num == unique_num:
                continue
            elif unique_num < num:
                count += 1
        result.append(count)
        count = 0

    return result 

print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)