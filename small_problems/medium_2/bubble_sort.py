"""
P: 
Write a function that takes a list as an argument.
Use the bubble swap method to sort the list.

RULES:
Sorting should be done in place. THe original list should be mutated.
List will contain at least two elements
Sorting can be done on ints and chars

E:

D:
Input: List
Output: List

A:
We need to use a while loop because we need to continue looping
through the list until there are no swaps.

So...



Use indexing and a range object to iterate through a list.
Store the objects being compared in variable.
Compare the two list elements.
If the comparison is true, swap the elements.
Count the swap.
Continue with the loop


swaps = None

"""

def bubble_sort(lst):
    while True:
        swaps = 0
        
        for idx in range(len(lst) - 1):
            if lst[idx] > lst[idx + 1]:
                lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]
                swaps += 1
        
        if swaps == 0:
            break

lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True