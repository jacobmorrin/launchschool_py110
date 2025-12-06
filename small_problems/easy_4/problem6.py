"""
PROBLEM:
Write a function that takes a string argument and returns a list of 
substrings of that string. Each substring should begin with the first 
letter of the word, and the list should be ordered from shortest to longest.

Write a function that takes a string argument, and returns a list of substrings
of that string beginning with the first character and subsequently adding
each character.

RULES:
- No spaces
- Single word string
- All letter

EXAMPLE:
# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])

ALGORITHM:
Primary:
- Create an empty string
- Loop through each character of the string adding to the empty string and appending
the string of characters to a list
- Each time we go through the loop we would have to increase the number of characters
- Return the list

Secondary:
- Since our return value is a list object, we can use a comprehension.
- We can loop through the indices and use slicing to create the strings.

"""
# Solution 1
# def leading_substrings(s):
#     result = []
#     chars = 1
    
#     while chars <= len(s):
#         result.append(s[:chars])
#         chars += 1

#     return result

# Solution 2
def leading_substrings(s):
    return [s[:idx] for idx in range(1, len(s) +1)]


print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])
