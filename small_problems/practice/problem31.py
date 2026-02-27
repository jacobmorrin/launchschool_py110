"""
P:
Write a function that takes a string in camelcase and converts it to kebab case.

input
string in camel case

output
string in kebab case

boundaries
need to lowercase all string for final output

cases
myCamelCase => my-camel-case

structures and helpers
could be helpful to put words in a list first

algo - hl
init empty list
loop through the string
when you get to a capital letter take all the ch before the cap and append to an empty list as lower
after running through all words, add last word

algo - main
words = []
start = 0

for i in range(len(s)):
    if s[i].isupper():
        words.append(s[start:i].lower()) # Test list
        start = i

words.append(s[start:].lower()) # Test list
return '-'.join(words)

"""
def kebabize(s):
    words = []
    start = 0

    for i in range(len(s)):
        if s[i].isupper():
            words.append(s[start:i].lower())
            start = i
    
    words.append(s[start:].lower())

    return '-'.join(words)

print(kebabize('myCamelCase'))