"""
P:
Write a function that takes a list of strings
And returns of list of ints that correspond to the number of characters in each string 
that occupy their place in the alphabet.

E:
# The below tests should each print True.
print(count_letters_in_position(["abode", "ABc", "xyzD"]) == [4, 3, 1])
print(count_letters_in_position(["abide", "ABc","xyz"]) == [4, 3, 0])
print(count_letters_in_position(["IAM", "CODING", "HELP"]) == [0, 0, 0])
print(count_letters_in_position(["", "a", "b", "c"]) == [0, 1, 0, 0])

D:
Input: List
Output: List

A:
Initalize count = 0
intialize result []
Create constant alphabet
loop through each word
loop through each character of each word
compare the letter of the alphabet from constant to the character
if the same add 1 to count
at end add count to result and reset count
reutnr result

"""
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def count_letters_in_position(lst):
    result = []

    for word in lst:
        count = 0

        for i, ch in enumerate(word.lower()):
            if ALPHABET[i] == ch:
                count += 1
        result.append(count)
    return result

print(count_letters_in_position(["abode", "ABc", "xyzD"]) == [4, 3, 1])
print(count_letters_in_position(["abide", "ABc","xyz"]) == [4, 3, 0])
print(count_letters_in_position(["IAM", "CODING", "HELP"]) == [0, 0, 0])
print(count_letters_in_position(["", "a", "b", "c"]) == [0, 1, 0, 0])
