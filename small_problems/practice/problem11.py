"""
P:
Write a function that takes a nonempty string as an argument.
Return a tuple consisting of a string and an integer.

s is the string.
the returned tuple is t.
The int in the tuple is k.
s == t * k 

E:
print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))

D: 
Input: S
Output: Tuple

A:
Start with the smallest substring of 1
Check if that substring occurs 

"""
def repeated_substring(s):
    m = len(s)
    for end in range(1, len(s) + 1):
        count = s.count(s[:end])

        if count * s[:end] == s:
            return (s[:end], count)
        
print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))