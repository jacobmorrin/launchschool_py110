"""
PROBLEM:
Given a dictionary and a list of keys, produce a new dictionary 
that only contains the key/value pairs for the specified keys.

EXAMPLE:
input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True

DATA:
Input: Dictionary
Output: Dictionary 

ALGORITHM:
This can be done with a dictionary comprehension and an if sattement.
Function should have two arguments, 
- Cycle through the input dict
- If a key is in the reference list to keep, add it to an empty dict

"""

def keep_keys(input_dict, keys):
    return {key: input_dict[key] for key in keys if key in input_dict}

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True