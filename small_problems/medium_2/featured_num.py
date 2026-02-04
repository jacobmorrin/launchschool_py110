"""
PROBLEM:
Write a function that takes an integer as an argument and returns 
the next featured number greater than the integer. Issue an error 
message if there is no next featured number.

RULES:
A featured number is:
- Multiple of 7
- Odd
- Digits each occur once

- In this case, all inputs > 0
- The largest possible featured number is 9876543201

EXAMPLE:
print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True

DATA:
- Input: int
- Output: Int (unless greater than 9876543201)

ALGORITM:
Option 1:
- Develop a list of all feature numbers
- Go through the list and return the first one greater than the input number

Option 2:
- Starting with input, go through each next number and test if its a feature number

for number in range(num, MAX_FEATURE_NUMBER + 1):
    if


"""
MAX_FEATURE_NUMBER = 9876543201
ERROR_MESSAGE = ("There is no possible number that "
             "fulfills those requirements.")

def is_feature(n):
    s = str(n)
    return (n % 2 == 1 and
            n % 7 == 0 and
            len(s) == len(set(s))
        )
        
def next_featured(start):
    for number in range(start + 1, MAX_FEATURE_NUMBER + 1):
        if is_feature(number):
            return number
    return ERROR_MESSAGE


print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
