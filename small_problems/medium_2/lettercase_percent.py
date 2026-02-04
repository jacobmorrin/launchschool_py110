"""
PROBLEM:
Write a function that takes a string and returns a dictionary containing:
- the % lowercase letters
- the % uppercase letters
- the percent letters that are neither

RULES:
Percentages should be returns as strings.
And rounded to two decimal points.
Strings will not be empty.

DATA:
Input: string
Output: string
intermediary: float

ALGORITHM:


"""
def to_percentage(count, total):
    return format(count / total * 100, '.2f')

def letter_percentages(s):
    total = len(s)
    upper = 0
    lower = 0
    neither = 0

    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        else:
            neither += 1

    return {
        'lowercase': to_percentage(lower, total),
        'uppercase': to_percentage(upper, total),
        'neither': to_percentage(neither, total)
    }

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)