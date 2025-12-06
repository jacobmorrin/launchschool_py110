"""
PROBLEM:
Write a function that takes a list of strings and returns a list 
of the same string values, but with all vowels (a, e, i, o, u) removed.

The function should take a list of string values, and return a list of the
same string values but the values should have their vowels removed.

RULES:
- Remove vowels of all cases

EXAMPLE:
# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True

DATA:
- Input is going to be a list
- Output will also be a list

ALGORITHM:
Method 1: For loops
- Loop through the list
- Loop through each list item
- If letter not a vowel, add letter to variable
- At end of word, append to list

"""
VOWELS = 'aeiouAEIOU'

def strip_vowels(s):
    no_vowels = [char for char in s if char not in VOWELS]
    return ''.join(no_vowels)

def remove_vowels(lst):
    return [strip_vowels(word) for word in lst]

# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True