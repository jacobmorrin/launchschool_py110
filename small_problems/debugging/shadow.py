"""
We defined a function intending to multiply the sum of numbers 
by a factor. However, the function raises an error. Why? How 
would you fix this code?

def sum(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(sum(numbers, 2) == 20)

"""

def get_sum(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(get_sum(numbers, 2) == 20)