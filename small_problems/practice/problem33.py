"""
P:
Determine the missing letter in the list

input
list of letters

output
single character that is missing

boundaries
output character must match case of input list
return empty list if input list is empty

cases
# print(determine_missing_letter(['a', 'b']))
print(determine_missing_letter(['a','b','c','d','f']) == 'e')
print(determine_missing_letter(['o','q','r','s']) == 'p')
print(determine_missing_letter(['H','J','K','L']) == 'I')
print(determine_missing_letter([]) == [])

data structure and helpers
constant alphabet with all characters could help
variable checking for is upper helpful X

algo - hl
find the starting index in the alphabet constant

loop through the input list by index
    check to see if start == ALPHABET.index(lst[i])
    if they don't match
        return ALPHABET[start]


"""
ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def determine_missing_letter(lst):
    if not lst:
        return []
    
    start = ALPHABET.index(lst[0])

    for i in range(len(lst)):
        if ALPHABET[start] != lst[i]:
            return ALPHABET[start]
        else:
            start += 1

    return ALPHABET[start]

print(determine_missing_letter(['a', 'b']))
print(determine_missing_letter(['a','b','c','d','f']) == 'e')
print(determine_missing_letter(['o','q','r','s']) == 'p')
print(determine_missing_letter(['H','J','K','L']) == 'I')
print(determine_missing_letter([]) == [])
