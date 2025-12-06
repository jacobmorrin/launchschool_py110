"""
PROBLEM:
From two list arguments, determine the elements that are unique to the first list. 
The return value should be a set.

Given two lists, determine which elements of the first list are not in the second list.
Return those elements in a set.

EXAMPLE:
list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})

Secondary:
- We could use a for loop and check the intersection. If the number is in the intersection, don't
add that number to a clean list.

Tertiary:
- Actually we could use a comprehension

"""
def unique_from_first(list1, list2):
    return set(list1) - set(list2)

list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})