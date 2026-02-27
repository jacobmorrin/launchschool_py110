"""
P:
Write a function that takes a list of ints as an argument.

Return the index N for which all numbers with an index less than N
sum to the same value as the numbers with an index greater than N.

R:
If there is no index that would make this happen return -1.
First run through is just first number [:1]
Index at N not included?

E:
print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)

A:
Loop through the list of numbers starting at 0
Left side = [:i]
Right side = [i + 1:]

"""
def equal_sum_index(lst):
    for idx in range(len(lst)):
        left = sum(lst[:idx])
        right = sum(lst[idx + 1:])
        if left == right:
            return idx
    return -1

print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)