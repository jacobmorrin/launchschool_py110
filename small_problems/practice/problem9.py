"""
P:
Write a function that takes two string arguments.
Returns the # of times that the second string occurs in the first string.

R:
Overlapping strings don't count (e.g. 'babab' contains 1 instance of 'bab', not 2)

E:
print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)

D:
Input: String
Output: Int

Algorithm
- Use the count method here to identify the number of instances

"""

def count_substrings(full_text, search_text):
    count = 0
    i = 0
    n = len(full_text)
    m = len(search_text)

    while i + m <= n:
        if full_text[i:i+ m] == search_text:
            count += 1
            i += m
        else:
            i += 1

    return count

print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)