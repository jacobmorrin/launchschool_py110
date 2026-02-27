"""
P:
Where My Anagrams At?
Two words are anagrams of each other if they both contain the same letters.

Write a method that will find all the anagrams of a word from a list.
You will be given two inputs a word and an array with words.
You should return an array of all the anagrams or an empty array if
there are none.

input
one word string, LIST of words

output
list of words that have the same letters

boundaries
no punctuation to worry about
everything is in lowercase

tests
('racer', ['crazer', 'carer', 'racar', 'caers', 'Racer']);
# ['carer', 'Racer']

helpers and structures
dictionaries might be helpful

algo - hl
create a dictionary of the chars in the input word

loop through the words in the list
    if lengths don't match 
        break

    for each word, create a dictionary


"""
def dict_maker(word):
    ch_dict = {}
    for ch in word.lower():
        ch_dict[ch] = ch_dict.get(ch, 0) + 1
    return ch_dict

def anagrams(base_word, word_lst):
    base_word_dict = {}
    anagrams = []

    base_word_dict = dict_maker(base_word)

    for word in word_lst:
        if len(word) != len(base_word):
            continue
        
        anagram_dict = dict_maker(word)

        for ch, occurences in anagram_dict.items():
            if base_word_dict.get(ch) != occurences:
                break
            
        anagrams.append(word)

    print(anagrams)
    

        
anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'Racer'])