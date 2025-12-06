"""
PROBLEM:
You want to multiply all elements of a list by 2. However, the function 
is not returning the expected result. Explain the bug, and provide a solution.

SOLUTION:
The problem is that during the iteration we are multiplying the integer by 
two but not capturing it anywhere. Since integers are immutable, item *=2
creates a new object in memory, and does not modify the item directly in the
list object. We are also returning the original list.

To fix this we should create a new list object, and append item *=2 to it, and
then return that new list.

Another solution would be to use a comprehension

"""
#SOLUTION 1: Modified for loop
def multiply_list(lst):
    result = [] # New list object
    for item in lst:
        result.append(item * 2) #Append new int to list

    return result #Return new list

#SOLUTION 2: Comprehension
def multiply_list2(lst):
    return [item * 2 for item in lst]

print(multiply_list2([1, 2, 3]) == [2, 4, 6])