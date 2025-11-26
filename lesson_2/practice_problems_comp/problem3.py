"""
PROBLEM:
Given the following data structure, return a new list with the same 
structure, but with the values in each sublist ordered in ascending 
order as strings (that is, the numbers should be treated as strings). 
Use a comprehension if you can. (Try using a for loop first.)

EXAMPLE:
lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
[['a', 'b', 'c'], [-3, 11, 2], ['black', 'blue', 'green']]

ALGORITHM:
- Use key of str in sort or sorted
"""
lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# # Traditional for loop
for sublst in lst:
    sublst.sort(key=str)

print(lst)

# Comprehension
sorted_str_lst = [sorted(sublst, key=str) for sublst in lst]

print(sorted_str_lst)