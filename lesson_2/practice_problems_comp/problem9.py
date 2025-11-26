"""
This problem may prove challenging. Try it, but don't stress about it. 
If you don't solve it in 20 minutes, you can look at the answer.

Given the following data structure, write some code to return a list 
that contains only the dictionaries where all the numbers are even.

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

[{'e': [8], 'f': [6, 10]}]

ALGORITHM:
- Okay we are looping through dictionaries
- We want to return the dictionary if all of the numbers in the values
are even 

Helper Function:
- Send list to helper function
- Check for odds
- If there are odds, return false


"""
def even_lst(dict1):
    for key, value in dict1.items():
        for num in value:
            if num % 2 == 1:
                return False
    return True
        
lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

even_lst = [dictionary for dictionary in lst if even_lst(dictionary)]

print(even_lst)

