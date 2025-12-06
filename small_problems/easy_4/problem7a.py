"""
PROBLEM:
- Given a string, return a list of all of the substrings in that list.
The substrings should be ordered by index, and from longest to shortest.

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
- We are looping through the string twice. We're looping through the string
twice. One loop focused on the starting position. And then another loop to 
create the substrings from that starting position. 


"""


def leading_substrings(s):
    return [s[:idx + 1] for idx in range(len(s))]

def substrings(s):
    results = []

    # This loop generates increasingly shorter strings based on the starting 
    # position (start_idx) that goes up
    for start_idx in range(len(s)):
        string_at_idx = s[start_idx:]

        # This loop sends the substrings to leading_subsstrings
        # which generates all of the sub-substrings
        for substring in leading_substrings(string_at_idx):
            results.append(substring)

    return results

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True