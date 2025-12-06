"""
PROBLEM:
Given a sequence of integers, filter out instances 
where the same value occurs successively, retaining 
only the initial occurrence. Return the refined sequence.

Given a sequence of integers, return a list that filters
out consecutive duplicates. 

[1, 1, 2, 2, 3, 1] -> [1, 2, 3, 1]

EXAMPLE:
original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True

# Non-consecutive duplicates are kept
original = [1, 2, 1, 3]
expected = [1, 2, 1, 3]
print(unique_sequence(original) == expected)      # True

DATA:
- Input: List
- Output: List

ALGORITHM
High-Level:
- Loop through the list
- If the last element of the result list doesn't match the
current element, add that element to the result list

- INITIALIZE empty RESULT list
- LOOP through the numbers
- COMPARE the number to the last element of result
- IF not same, add it
- RETURN RESULT

"""
def unique_sequence(values):
    if not values:
        return []
    
    result = [values[0]]

    for num in values[1:]:
        if result[-1] != num:
            result.append(num)
    return result

def unique_sequence2(values):
    return [value 
            for idx, value in enumerate(values)
            if idx == 0 or value != values[idx - 1]]


original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True

# Non-consecutive duplicates are kept
original = [1, 2, 1, 3]
expected = [1, 2, 1, 3]
print(unique_sequence(original) == expected)      # True

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence2(original) == expected)      # True

# Non-consecutive duplicates are kept
original = [1, 2, 1, 3]
expected = [1, 2, 1, 3]
print(unique_sequence2(original) == expected)      # True