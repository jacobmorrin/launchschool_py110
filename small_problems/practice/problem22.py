"""
P:
Write a function that takes two strings as input, 
full_text and search_text, and returns the number of 
times search_text appears in full_text.

E:
solution('abcdeb','b') # should return 2 since 'b' shows up twice
solution('aaabbbcccc', 'bbb') # should return 1
solution('aaabbbbcccc', 'bbb') # should return 2

D:
Input: Two strings
Outputn: int

A:
Get the length of the search text
Get the length of the full text
intialize a count variable
Loop throug the indices of the full text



"""
def solution(full_text, search_text):
    full_length = len(full_text)
    search_length = len(search_text)
    count = 0
    
    if not search_text:
        return 0

    for i in range(full_length):
        if full_text[i:i + search_length] == search_text:
            count += 1
    
    return count

print(solution('abcdeb','b') == 2) # should return 2 since 'b' shows up twice
print(solution('aaabbbcccc', 'bbb') == 1) # should return 1
print(solution('aaabbbbcccc', 'bbb') == 2) # should return 2