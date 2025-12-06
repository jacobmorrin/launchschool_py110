"""
PROBLEM:
Write a function that returns a list of all substrings of a string. 
Order the returned list by where in the string the substring begins. 
This means that all substrings that start at index position 0 should 
come first, then all substrings that start at index position 1, and 
so on. Since multiple substrings will occur at each position, return 
the substrings at a given index from shortest to longest.

Write a function that returns a list of all the substrings of a string.
All substrings means all, so in abc you would have a, ab, b, bc, c.
Order the substrings based on where the first letter starts in the original string.
And sort them from shortest to longest.

EXAMPLE:
expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True

ALGORITHM:
- Two tracker variables, start of string, and the index we start from
- For sorting we would want a tuple of the starting letter's index, 
the length of the substring.

Helper function
- Needs to send back the index position of the character
- And the length of the substring

append a 

"""
def substrings(s):
    return [s[start_idx:end_idx] for start_idx in range(len(s))
                             for end_idx in range(start_idx + 1, len(s) + 1)
    ]