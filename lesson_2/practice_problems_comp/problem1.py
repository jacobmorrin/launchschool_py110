munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

# With tradtional loop
age = 0

for person, info in munsters.items():
    if info['gender'] == 'male':
        age += info['age']

print(age)

# With Comprehension
male_ages = [info['age'] for info in munsters.values() if info['gender'] == 'male']
print(male_ages)
print(sum(male_ages))