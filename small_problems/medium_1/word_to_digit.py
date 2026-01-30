"""
PROBLEM:
Write a function that takes a string as an argument and returns 
that string with every occurrence of a "number word"

EXAMPLE:
message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True

DATA:

ALGORITHM:
- Turn the string into a list
- Iterate through the list
- Check if the word is in the dictionary
    - if it is in the dictionary, replace the word with the value



"""
def word_to_digit(sentence):
    str_lst = sentence.split(' ')
    result = []

    str_nums = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
        }

    for word in str_lst:
        if word in str_nums:
            result.append(str_nums.get(word))
        else:
            result.append(word)

    return ' '.join(result)

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")