"""
BOUNCY COUNT
Some numbers have only ascending digits, like 123, 3445, 2489, etc.
Some numbers have only descending digits, like 321, 5443, 9842, etc.
A number is "bouncy" if it has both ascending and descending digits, like 313, 92543, etc.
Write a method that takes a list of numbers and counts how many of them are bouncy.



"""

def anagram_finder(s1, s2):
    char_set = [char for char in s1]



def anagram_difference(string1, string2):
    unique_set = set()
    for char in string1:
        unique_set.add(char)
    for char in string2:
        unique_set.add(char)
    
    total = 0
    for char in unique_set:
        count1 = string1.count(char)
        count2 = string2.count(char)
        total += abs(count1-count2)
    return total

print(set('hello'))