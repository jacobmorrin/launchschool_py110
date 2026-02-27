"""
PROBLEM:
Create a function that takes a string argument and returns the character
that occurs most often in the string. 

RULES:
When counting characters, consider uppercase and lowercase versions to be the same.
If there are multiple characters 
with the same greatest frequency, return the one that appears first in the string. 

E:
print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')

DATA:
Input: String
Output: string (character)
INtermediary:
Dictionary

Algorithm:
Loop through string
Create a dictionary counting the instances of characters using .lower


"""
def most_common_char(s):
    character_count = {}
    s_lower = s.lower()

    for char in s_lower:
        character_count[char] = character_count.get(char, 0) + 1
    
    return max(character_count, key=character_count.get)

print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')