"""
PROBLEM:
We have a string of words + non-alpha characters
Have to return the words + all non-alphas replaced by spaces, but...
If 1+ non-alphas are in a row, we replace that with just 1 space

EXAMPLE:
print(clean_up("---what's my +*& line?") == " what s my line ") # True

DATA STRUCTURES:
Input: string
Intermediary: maybe list? maybe a string also?
Output: a new string

ALGORITHM:
def clean_up(s):
- inter_string = ''
- start_idx = None
- end_idx 

- check each character to see if it's alpha

for idx in range(len(s)):
    if s[idx].isalpha():
        inter_string += s[idx]

    else:
        inter_string += ' '

        for sub_idx in range(idx, len(s)):
            if s[sub_idx].isalpha()
            idx = sub_idx - 1
            break
    
    

- Loop through each character
- If the character is alpha, add it to result
- If the character is not-alpha:
    - Find the location of the next alpha character
    - Add a space to result
    - Start looping again at the location of the next alpha character




inter_string = a

a-*&&(*^#&*$^@*())are
0123

loop 0: alpha
loop 1: nonalpha
    - save the start point of the first nonalpha -- this is a number
    - and then find the end point of nonalpha



- Check through each character
- If its alpha, add it
- if its non alpha
- Save that index as the the start_idx
- check all of the characters after that until you find an alpha
- return the index right before the next alpha
- Save that index as the end_index
- Replace s[start_idx: end_idx] with a ' '



s[0:3] = ' '

s[start_idx:start_idx + 1]



- in a new string or list, we need to add a space per one or multiple non-alphas in a row
- if it's a list, we need to convert it to a string, probably with .join
- and return the string either way

variables: input_string, words_in_list, 

"""

def clean_up(s):
    result = ''

    for idx in range(len(s)):
        
        if s[idx].isalpha():
            result += s[idx]
    
        else:
            if result == '':
                result += ' '
            elif result[-1] != ' ':
                result += ' '

    print(f'"{result}"')
    return result
    
print(clean_up("---what's my +*& line?") == " what s my line ") # True