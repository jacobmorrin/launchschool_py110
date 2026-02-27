"""
P
Write a function that generates text following a pattern where:

the first and last characters of each word remain in their original place
characters between the first and last characters are sorted alphabetically
punctuation should remain at the same place as it started

input
string

output
first ch + sorted characters + last character

boundaries
can't sort punctuation 
tsts all lowercase

cases
scramble_words('professionals') # should return 'paefilnoorsss'
scramble_words("you've gotta dance like there's nobody watching, love like you'll never be hurt, sing like there's nobody listening, and live like it's heaven on earth.") # should return "you've gotta dacne like teehr's nbdooy wachintg, love like ylo'ul neevr be hrut, sing like teehr's nbdooy leiinnstg, and live like it's haeevn on earth."

data structures and helpers
for sentence, splitting into list

algo - hl
split string into a list WORDS

for each word (helper)

create dictionary for punctuation
    loop through the ch by index
    if the ch is punctuation 
    add that character and the index to a dictionary

cleaned = ''
clean the word
    loop through the characters
        if the ch is alpha add it to cleaned

        

sort the middle characters
    sorted_ch = sorted(cleaned[1:-2])

add back the first and last ch
    sorted_ch.insert(cleaned[0], 0)
    sorted_ch.insert(cleaned[0], -1)

add back in the punctuation
    for punc_mark, index in punc_dict:
        sorted_ch.insert(punc_mark, index)

reassemble the word
    return ''.join(sorted_ch)
punctuation_places = {}
loop through the ch by indices
    if not ch.isalpa()
    first = word[0]


"""
def word_scrambler(s):
    punc_dict = {}
    cleaned = ''

    for i in range(len(s)):
        if not s[i].isalpha():
            punc_dict[s[i]] = i
        else:
            cleaned += s[i]

    sorted_chars = sorted(cleaned[1:-1])
    sorted_chars.insert(0, cleaned[0])
    sorted_chars.append(cleaned[-1])

    for punc, idx in punc_dict.items():
        sorted_chars.insert(idx, punc)

    return ''.join(sorted_chars)

def scramble_words(s):
    return ' '.join([word_scrambler(word) for word in s.split(' ')])

# print(scramble_words('professionals')) # should return 'paefilnoorsss'
print(scramble_words("you've gotta dance like there's nobody watching, love like you'll never be hurt, sing like there's nobody listening, and live like it's heaven on earth.") == "you've gotta dacne like teehr's nbdooy wachintg, love like ylo'ul neevr be hrut, sing like teehr's nbdooy leiinnstg, and live like it's haeevn on earth.")
                     


