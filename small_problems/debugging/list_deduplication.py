"""
PROBLEM:
A developer is trying to remove duplicates from a list. 
They use a set for deduplication, but the order of elements 
is lost. How can we preserve the order?

data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = list(set(data))
print(unique_data == [4, 2, 1, 3]) # order not guaranteed

SOLUTION:
Sets preserve unique values but not order. If order is important,
better to use a list.

"""
data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = []

for item in data:
    if item not in unique_data:
        unique_data.append(item)

print(unique_data == [4, 2, 1, 3]) # order not guaranteed
