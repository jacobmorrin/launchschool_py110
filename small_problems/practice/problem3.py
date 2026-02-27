"""
PROBLEM:
Create a function that takes a string argument and returns a copy 
of the string with every second character in every third word 
converted to uppercase. Other characters should remain the same.

RULES:
Every second character means starting with index 1.
Every third word means starting with index 2, 5
Spaces separate words
return a copy of the string, so leave original 

EXAMPLE:
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

DATA:
Input: String
Output: New string
List: Use list to break apart sentence

ALGORITHM:
Double loop. Loop through words, loop through characters
Break senetence into new list
Loop through every third word.
Loop through  characters.


"""
def to_weird_case(s):
    s_lst = s.split(' ')
    weird_word = ''

    for word_idx in range(2, len(s_lst), 3):
        for char_idx in range(len(s_lst[word_idx])):
            if char_idx % 2 == 0:
                weird_word += s_lst[word_idx][char_idx]
            else:
                weird_word += s_lst[word_idx][char_idx].upper()
        s_lst[word_idx] = weird_word
        weird_word = ''
    
    return ' '.join(s_lst)

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