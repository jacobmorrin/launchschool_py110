"""
P:
Write a function that takes a string of digits as an argument.
The function should return the number of even-numbered substrings 
that can be formed.

R:
If a substring occurs more than once, you should count each occurrence 
as a separate substring.

E:
For example, in the case of '1432', the even-numbered substrings are 
'14', '1432', '4', '432', '32', and '2', for a total of 6 substrings.

print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)

D:
Input: string
Output: int

A:
Two loops:
First loop loops through all strings
Second loop creates window

1432
0123

0123
s[0:4]
s[0:5]
"""

def even_substrings(s):
    count = 0
    j = 1
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if int(s[i:j]) % 2 == 0:
                count += 1
    return count

print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)