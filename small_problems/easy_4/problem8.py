"""
Write a function that returns a list of all palindromic substrings of a string. 
That is, each substring must consist of a sequence of characters that reads the 
same forward and backward. The substrings in the returned list should be sorted 
by their order of appearance in the input string. Duplicate substrings should 
be included multiple times.

PROBLEM:
- Write a function that takes a string. The function should return a list of all
palindromic substrings.
- Substrings should be sorted by their order of appearance.

RULES:
- Case matters
- Assume we receive a string
- Single character strings not palindroms but double are

ALGORITHM:
- two loops
-- Loop through word and 


One Loop:
One Loop (end index):
- Starting with first letter, add leters and check if that substring is the same
backwards and forwards

Second Loop (start index):
- Change the start index

Palindromes:
- With a list of all the palindromes, we just need to see if the substring is the same back and 
forward
"""

def leading_substrings(s):
    return [s[:idx + 1] for idx in range(len(s))]

def substrings(s):
    substrings_lst = []

    for start_idx in range(len(s)):
        string_at_idx = s[start_idx:]

        for substring in leading_substrings(string_at_idx):
            substrings_lst.append(substring)

    return substrings_lst

def palindromes(s):
    all_substrings = substrings(s)
    return [substring for substring in all_substrings 
            if substring == substring[::-1] and len(substring) > 1
    ]

print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True