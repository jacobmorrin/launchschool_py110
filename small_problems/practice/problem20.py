"""
PROBLEM:
Write a function that takes a list of numbers.
All of the numbers are the same except for one.
Find the different number and return that

EXAMPLES:
print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)

DATA:
input: List
Ouput: Going to be an int
Dictionary and return the key associated with a value of 1.

ALGORITHM:
Intialize empty dictionary
Populate dictionary with number counts using .get + 1
return key that has a value of 1

"""
def what_is_different(lst):
    nums = {}
    for num in lst:
        nums[num] = nums.get(num, 0) + 1

    for key, value in nums.items():
        if value == 1:
            return key
    return None

print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)