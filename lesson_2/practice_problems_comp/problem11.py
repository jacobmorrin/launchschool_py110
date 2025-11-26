"""
The following dictionary has list values that contains strings. 
Write some code to create a list of every vowel (a, e, i, o, u) 
that appears in the contained strings, then print it.

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

# Your code goes here

print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']

ALGORITHM:
- Three Loops
    - Loop through dictionary values
    - Loop through value list
    - Loop through list elements

"""
dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

vowels = 'aeiou'
list_of_vowels = [char for lst in dict1.values()
                       for word in lst
                       for char in word if char in vowels]

print(list_of_vowels)
