"""
Docstring for set_mods
PROBLEM:
We want to remove certain items from a set while iterating over it, 
but the code below throws an error. Why is that and how can we fix it?

data_set = {1, 2, 3, 4, 5}

for item in data_set:
    if item % 2 == 0:
        data_set.remove(item)

The problem is that we are removing elements from an iterable as we iterate. 
So Python thinks we are going to be iterating over 5 elements. If that 
changes during iteration, Python will throw a RunTime error.

One solution would be to create and return a new set or to use a comprehension
to create a new set.
"""
data_set = {1, 2, 3, 4, 5}
new_set = set()

for item in data_set:
    if item % 2 != 0:
        new_set.add(item)

print(new_set)

#Or with a comprehension

new_set2 = {item for item in data_set if item % 2 != 0}
print(new_set2)