"""
P:
Write a function that takes two strings as arguments.
Return True is some portion of the characters in the first string
can be rearranged to match the characters of the second string
Otherwise return false

R:
Both strings just lowercase

E:
print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)
print(unscramble('olc', 'cool') == False)

D:
Input: Two strings
Output: Boolean
Set: Intersect would be nice but what about double characters?
List: 
Dict: Maybe count characters in each in separate dictionaries and compare values?

A:
Get both strings into separate dictionaries
Loop through the ch of s1 and compare the key value to those in s2
if the value in s2 is >= the value in s1 then True


Can the first string be rearrranged to make the second string.
In other words, are all characters of the second string in the first string
eturn True is some portion of the characters in the first string
can be rearranged to match the characters of the second string
Otherwise return false
"""
def unscramble(s1, s2):
    s1_dict = {}
    s2_dict = {}

    for ch in s1:
        s1_dict[ch] = s1_dict.get(ch, 0) + 1
    
    for ch in s2:
        s2_dict[ch] = s2_dict.get(ch, 0) + 1

    for key, value in s2_dict.items():
        if s1_dict.get(key, 0) < value:
            return False
        
    return True

print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)
print(unscramble('olc', 'cool') == False)