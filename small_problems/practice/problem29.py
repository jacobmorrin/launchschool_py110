"""
Write a function that, given a string of text, returns a list of the top-3 
most occurring words, in descending order of the number of occurrences.

input
long string

output
list with top three words

boundaries
punctuation should not be included in the count and should be taken off of words

cases
top_3_words(" , e .. ") # ["e"]
top_3_words(" ... ") # []
top_3_words(" ' ") # []
top_3_words(" ''' ") # []

data structures and helpers
definitely need a dictionary for counting

use a list (or two) to get all of the words (helper)

algo - hl
clean the words and get them all into a list X
run through the list with .get to create a dictionary of counts
run through the keys, and values to find the highest 

algo - helper
    clean_words = []
    cleaned = ''
    dirty_words = s.split(' ')

    for word in dirty_words:
        if word.isalpha():
            clean_words.append(word)
        else:
            for ch in word:
                if ch.isalpha():
                    cleaned += ch
            clean_words.append(cleaned)
            cleaned = ''
    
    return clean_words

algo - main
    init word_counts = {}
    for word in cleaned:
        word_counts[word] = word_counts.get(word, 0) + 1
    
    while
    loop through keys and values
        compare each value to max_count
        if value greater, max count = value, max_word = key

    after loop addthe

"""
def clean_words(s):
    clean_words = []
    cleaned = ''
    dirty_words = s.split(' ')

    for word in dirty_words:
        if word.isalpha():
            clean_words.append(word)
        else:
            for ch in word:
                if ch.isalpha():
                    cleaned += ch
                    
            if cleaned != '':
                clean_words.append(cleaned)
        cleaned = ''
    return clean_words

def top_3_words(s):
    cleaned = clean_words(s)
    max_words = []
    word_counts = {}
    max_count = 0
    max_word = ''
    
    for word in cleaned:
        word_counts[word] = word_counts.get(word, 0) + 1
    

    while len(max_words) < 3 and len(word_counts) > 0:
        for key, value in word_counts.items():
            if value > max_count:
                max_word = key
                max_count = value
        
        max_words.append(max_word)
        del word_counts[max_word]
        max_count = 0
        max_word = ''
    print(max_words)
    return max_words




top_3_words(" , e .. ") # ["e"]
top_3_words(" ... ") # []
top_3_words(" ' ") # []
top_3_words(" ''' ") # []
top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.""") # should return ["a", "of", "on"]