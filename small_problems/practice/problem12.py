"""
P:
Write a function that takes a string as an argument.
The function should return true if the string is a pangram
False if it is not.

R:
Pangram is a sentence that contains every letter of the alphabet once.

Create a function that takes a string as an argument and returns True if the 
string is a pangram, False if it is not.

For example, the sentence "Five quacking zephyrs jolt my wax bed." 
is a pangram since it uses every letter at least once. Note that case is irrelevant.

E:
print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)

D:
Input: String
Output: Boolean
Set: Get all letters, if 26 its a pangram!
Dictionary: add all letters to dictionary with counts, if no zeroes, pangram!

A:
Get a set of all the lowercase alphabetic characters
If the length of the set is 26,
"""
ALPHABET_LENGTH = 26
def is_pangram(s):
    chars = {ch for ch in s.lower() if ch.isalpha()}
    return ALPHABET_LENGTH == len(chars)

print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)
