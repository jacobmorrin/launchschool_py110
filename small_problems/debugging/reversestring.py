"""
WHAT IS THE BUG?
- The bug is that the looping is not working as intended. Each time 
we loop through "string" we are creating a new string comprised of the 
character from the iteration plus on the first loop the original string
and on subsequent loops the growing string. Like so:

hhello
ehhello
lehhello
llehhello
ollehhello

To fix this we need to introduce a new string variable (result) and prepend 
each character of the original string to it. To prepend we add the character 
and then the rest of the result from the last iteration.

Another approach would be to just use slicing.

"""
def reverse_string(string):
    result = ''
    for char in string:
        result = char + result
    return result

print(reverse_string("hello") == "olleh")

def reverse_string2(string):
    return string[::-1]

print(reverse_string("hello") == "olleh")