"""
Given the following data structure, return a new list 
identical in structure to the original but, with each 
number incremented by 1. Do not modify the original data 
structure. Use a comprehension.

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

[{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]

"""
def value_incrementer(dictionary):
    return {key: value + 1 for key, value in dictionary.items()}

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

new_list = [value_incrementer(value) for value in lst]

print(new_list)