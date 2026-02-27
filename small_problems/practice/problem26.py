"""
P:
Write a function that takes a list of words and constructs a new word 
by concatenating the nth letter from each word, where n is the position 
of the word in the list. Ignore if the nth letter from the word does not exist.

E:
nth_char(['yoda', 'best', 'has']) # 'yes'
nth_char(['hello', 'hello', 'hello', 'hello', 'hello', 'no']) # 'hello'

D:
Input: List of strings
Output: word

A:
Initialize empty string
Loop through index
    once in the index, take the ith character and add it to the empty string

"""
def nth_char(lst):
    result = ''

    for i in range(len(lst)):
        if len(lst[i]) >= i + 1:
            result += lst[i][i]
        else:
            continue
    
    print(result)

nth_char(['yoda', 'best', 'has']) # 'yes'
nth_char(['hello', 'hello', 'hello', 'hello', 'hello', 'no']) # 'hello'
