"""
Problem:
Create a function that takes a string argument and returns 
a copy of the string with every second character in every 
third word converted to uppercase. Other characters should 
remain the same.

Create a function that takes a string argument and returns
a copy of the string with every second character in every
third word converted to uppercase.

- every second (odd index) every third word (idx + 1 % 3)

Example:
# The following tests should each print True.
original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)

Data:
Input: string
Output: String
Intermediary: lst = [], result = ''

Algorithm:
- every second (odd index) every third word (idx + 1 % 3)

Initialize blank variables
def to_weird_case(s):

Get string into a list
 lst = s.split()

- Loop through each word
- Find the words that are in indices that are multiples of three

for lst_idx in range(len(lst))):
    if (lst_idx + 1) % 3 = 0:
        lst[lst_idx] = every_other_upper(lst[lst_idx])

Define helper function

def every_other_upper(word):
    result = ''

    for idx in word:
        if word_idx % 2 == 0:
            result += word[idx.upper]
        else:
            result+= word[idx]
    
    return result
"""

def to_weird_case(s):
    lst = s.split()

    for lst_idx in range(len(lst)):
        if (lst_idx + 1) % 3 == 0:
            lst[lst_idx] = every_other_upper(lst[lst_idx])
    print(' '.join(lst))
    return ' '.join(lst)

def every_other_upper(word):
    result = ''

    for idx in range(len(word)):
        if idx % 2 == 1:
            result += word[idx].upper()
        else:
            result+= word[idx]
    
    return result

# The following tests should each print True.
original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)