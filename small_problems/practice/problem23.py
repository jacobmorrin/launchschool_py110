"""
P:
A pangram is a sentence that contains every single letter of the alphabet at least once.
Given a string, detect whether or not it is a pangram. Return True if it is, False if not.
 Ignore numbers and punctuation.

E:
pangram("The quick brown fox jumps over the lazy dog.") # should return True
pangram("This is not a pangram.") # should return False
"""
def pangram(s):
    return len({letter for letter in s.lower() if letter.isalpha()}) == 26

print(pangram("The quick brown fox jumps over the lazy dog.") == True) # should return True
print(pangram("This is not a pangram.")  == True)