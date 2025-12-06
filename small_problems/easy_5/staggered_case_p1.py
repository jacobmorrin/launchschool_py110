"""
PROBLEM:
Write a function that takes a string as an argument and returns 
that string with a staggered capitalization scheme. Every other 
character, starting from the first, should be capitalized and 
should be followed by a lowercase or non-alphabetic character. 
Non-alphabetic characters should not be changed, but should be 
counted as characters for determining when to switch between upper 
and lower case.

Write a function that takes a string as an argument. The function should
return that string with a every other character capitalized.

RULES:
- Non-alphabetic characters should not be changed, but should be 
counted as characters for determining when to switch between upper 
and lower case.
- Start from the first character

EXAMPLE:
string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True

DATA:
Input: String
Output: string
Intermediary: **result** string

ALGORITHM:
Strategy 1: Comprehension and ''.join
- Probably can do this with a comprehension

"""
def staggered_case(string):
    lower_string = string.lower()
    result = ''

    for idx in range(len(lower_string)):
        if idx % 2 == 0:
            result += lower_string[idx].upper()
        else:
            result += lower_string[idx]

    return result

def staggered_case2(string):
    lower_string = string.lower()
    char_lst = [lower_string[idx].upper() if idx % 2 == 0 else lower_string[idx]
                for idx in range(len(lower_string))
                ]
    return ''.join(char_lst)

def staggered_case3(string):
    result = ''
    for idx, char in enumerate(string):
        func = char.upper if idx % 2 == 0 else char.lower
        result += func()
    return result

def staggered_case4(string):
    result = ''
    for idx, char in enumerate(string):
        result += char.upper() if idx % 2 == 0 else char.lower()
    return result


# string = 'I Love Launch School!'
# result = "I LoVe lAuNcH ScHoOl!"
# print(staggered_case(string) == result)  # True

# string = 'ALL_CAPS'
# result = "AlL_CaPs"
# print(staggered_case(string) == result)  # True

# string = 'ignore 77 the 4444 numbers'
# result = "IgNoRe 77 ThE 4444 nUmBeRs"
# print(staggered_case(string) == result)  # True

# print(staggered_case('') == "")          # True

string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case4(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case4(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case4(string) == result)  # True

print(staggered_case4('') == "")          # True