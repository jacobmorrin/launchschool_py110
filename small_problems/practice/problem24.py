"""
P:
Write a function that takes a lowercase string as input and 
returns the length of the longest substring that consists 
entirely of vowels (a, e, i, o, u).

E:
solve("roadwarriors") # should return 2
solve("suoidea") # should return 3

D:
Input: s
Output: Int

A:
Initialize count variable and VOWELS constant and current max
loop ch of s
if ch in vowels, count += 1
"""
VOWELS = 'aeiou'
def solve(s):
    current_max = 0
    count = 0

    for ch in s:
        if ch in VOWELS:
            count += 1
        else:
            current_max = max(current_max, count)
            count = 0

    return max(count, current_max)

print(solve("roadwarriors") == 2) # should return 2
print(solve("suoidea") == 3) # should return 3