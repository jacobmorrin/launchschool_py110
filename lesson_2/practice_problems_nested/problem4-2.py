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
    for name, info in dct.items():
        print(f'{name} is a {info['age']}-year-old {info['gender']}')

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

print_name_and_age(munsters)

