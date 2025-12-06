"""
PROBLEM
Modify the function from the previous exercise so it ignores 
non-alphabetic characters when determining whether it should 
uppercase or lowercase each letter. The non-alphabetic characters 
should still be included in the return value; they just don't count 
when toggling the desired case.

EXAMPLE:
string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True

DATA: 
Input: String
Output: String
Intermediary: **result** variable

ALGORITHM:
- We need to keep track as to whether the last alpha chracter was uppered

- INITIALIZE variable **upper** = True
- LOOP through each character
    - If you capitalize a character, set UPPER to False
- LOOP through the characters 

"""
def staggered_case(string):
    upper = True
    result = ''
    for char in string:
        if char.isalpha():
            result += char.upper() if upper else char.lower() 
            upper = not upper 
        else: 
            result += char 
    return result

string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True