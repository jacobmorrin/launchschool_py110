"""
P:
Write a function that returns the count of distinct case-insensitive 
alphabetic characters and numbers that occur more than once.

E:
print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5

D:
Input: string
Output: Int
Dict: Put all in dictionary, go through dictionary and count those >= 2

A:
Create dictionary with counts of characters using .get and .lower
Loop through dictionary and count instance of value greater than 2.
"""
def distinct_multiples(s):
    chars = {}
    result = 0

    for ch in s.lower():
        chars[ch] = chars.get(ch, 0) + 1
    
    for value in chars.values():
        if value >= 2:
            result += 1
    
    return result

print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5