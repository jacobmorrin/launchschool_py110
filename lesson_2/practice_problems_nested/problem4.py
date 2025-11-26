"""
PROBLEM:
print the following
(name) is a (age)-year-old (male or female).

ALGORITHM:
- Use a for loop and .keys to loop through names
    - Assign name to a variable
- Use a second for loop to loop through the sub-dict

"""
def print_name_and_age(dct):
    for person in dct.keys():
        for stats in dct[person]:
            age = dct[person]['age']
            gender = dct[person]['gender']
        print(f'{person} is a {age}-year-old {gender}.')

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

print_name_and_age(munsters)

