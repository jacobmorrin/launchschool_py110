"""
P:
Write a function that takes a non-empty string as an argument.
The string will be all lowercase alphabetic characters. The 
function should return the length of the longest vowel substring.

R:
VOWELS = "aeiou"

E:
print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)

D:
Input: alpha string
Output: Int
String: Iterate through the string
Int: Use as a counter

A:
Set result variable to 0
set counter to 0
Set constant vowels
Loop through the letters.
If ch is vowel, count += 1.
else
    if count > result:
        result = count
        count = 0
    else:
        count = 0

"""
VOWELS = "aeiou"

def longest_vowel_substring(s):
    result = 0
    count = 0

    for ch in s:
        if ch in VOWELS:
            count += 1
        else:
            if count > result:
                result = count
                count = 0
            else:
                count = 0
    
    result = max(result, count)

    return result

print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)