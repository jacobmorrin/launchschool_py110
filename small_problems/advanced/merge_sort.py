"""
P:
Write a function that takes a list argument.
Return a new list that contains the values of the original list in sorted order.
Sort the list using the merge sort algorithm.

R:
Every element of the list will be all nums or strings.

E:
[9, 2, 7, 6, 8, 5, 0, 1] -->              # initial list
[[9, 2, 7, 6], [8, 5, 0, 1]] -->          # divide into two lists
[[[9, 2], [7, 6]], [[8, 5], [0, 1]]] -->  # divide each sub-list in two
# repeat until each sub-list contains only 1 value
[[[[9], [2]], [[7], [6]]], [[[8], [5]], [[0], [1]]]]

A:
Get big list into series of small lists.



 Start with your list.
 Find the length of the list. 
 Divide the 

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

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    return merge(sorted_left, sorted_right)

# All of these examples should print True
print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
print(merge_sort([5, 3]) == [3, 5])
print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])

original = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
            'Kim', 'Bonnie']
expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel',
            'Sue', 'Tyler']
print(merge_sort(original) == expected)

original = [7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54,
            43, 5, 25, 35, 18, 46]
expected = [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25,
            35, 37, 43, 46, 51, 54]
print(merge_sort(original) == expected)