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
    words = s.split(' ')

    for word_idx in range(2, len(words), 3):
        word = words[word_idx]
        chars = [
            ch.upper() if i % 2 == 1 else ch for i, ch
            in enumerate(word)
        ]
        words[word_idx] = ''.join(chars)
    
    return ' '.join(words)

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