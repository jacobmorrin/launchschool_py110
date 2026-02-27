"""
PROBLEM:
Create a function that takes a list of integers as an argument. 
The function should return the minimum sum of 5 consecutive numbers in the list. 
If the list contains fewer than 5 elements, the function should return None.

EXAMPLE:
print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)

DATA:
Input: List
Output: Int

ALGORITHM:
Get length of the list -- store.
Set end_idx to 6
Check length. If < 5 return None
Use a for loop and a range object with the length (start_idx)
sum = lst[start_idx:end_idx]
if sum 
"""
def minimum_sum(lst):
    if len(lst) < 5:
        return None
    
    sums = []
    for idx in range(len(lst) - 4):
        sums.append(sum(lst[idx:idx + 5]))

    return min(sums)

print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)