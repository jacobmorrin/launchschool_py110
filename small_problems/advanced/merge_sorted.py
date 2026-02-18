"""
P:
Write a function that takes two sorted lists.
Return a new list that contains all the elements from both input lists in 
ascending sorted order.

RULES:
Lists contain either all ints or strings
You cannot sort the final result list.
You must build the result list one elements at at time.
You cannot mutate the input lists.

E:
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])

D:
Input: Two Lists
Output: One list

Boolean: Got to find a way to compare all of the elements to find the first
String: If the list is populated with strings then yes. 
Array:
Set:
Dict:
Int:

Algorithm:

Option 1:
- Combine both lists. Find the max of the list. Insert it at position 0 of a new list.
Pop that element from the list.

Option 2:
- Create a dictionary with each element

"""
def merge_lists(list1, list2):
    return list1 + list2

def merge(list1, list2):
    merged = merge_lists(list1, list2)
    sorted = []

    while len(merged) > 0:
        sorted.insert(0, max(merged))
        merged.pop(merged.index(max(merged)))

    return sorted

print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)