"""
P:
Write a function that takes a list of ints as input
Count the number of non-touching pairs.
NTP = two equal ints separated by some other integer

E:
non_touching_pairs([1, 2, 5, 6, 5, 2]) # 1
non_touching_pairs([1, 2, 2, 20, 6, 20, 2, 6, 2]) # 3

D:
Input: List
Output: Int

length = 9
last index = 
[1, 2, 2, 20, 6, 20, 2, 6, 2]
 0. 1. 2. 3.  4.  5.  6 7.  8

A:
Initialize empty set
Start with index.
Scan rest of numbers starting with index + 1.
If there is another number, add it to a set


"""
def non_touching_pairs(lst):
    pairs = set()

    for i in range(len(lst) - 2):
        for j in range(i + 2, len(lst)):
            if lst[i] == lst[j]:
                pairs.add(lst[i])
    print(pairs)
    return len(pairs)

print(non_touching_pairs([1, 2, 5, 6, 5, 2]) == 1) # 1
# print(non_touching_pairs([1, 2, 2, 20, 6, 20, 2, 6, 2]) == 3) # 3