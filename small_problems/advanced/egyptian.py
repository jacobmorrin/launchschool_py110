"""
PROBLEM:
Write two functions
- One that takes a rational number as an argument and returns a list
of the denominators that are part of an Egyptian Fraction representation 
of the number

another that takes a list of numbers in the same format, and calculates 
the resulting Rational number. You will need to use the Fraction class 
provided by the fractions module.

ALGORITHM:
Egyptian:
create a result variable set to an empty list
denominator = 1
cycle through integers: 1/1, 1/2, 1/3
while loop


"""
from fractions import Fraction

def egyptian(num):
    result = []
    denominator = 1
    remaining = num

    while remaining != 0:
        unit_fraction = Fraction(1, denominator)
        if unit_fraction <= remaining:
            remaining -= unit_fraction
            result.append(denominator)
        denominator += 1
    
    return result

def unegyptian(lst):
    return sum(Fraction(1, num) for num in lst)

print(egyptian(Fraction(2, 1)))      # [1, 2, 3, 6]
print(egyptian(Fraction(137, 60)))   # [1, 2, 3, 4, 5]
print(egyptian(Fraction(3, 1)))

print(unegyptian(egyptian(Fraction(1, 2))) == Fraction(1, 2))
print(unegyptian(egyptian(Fraction(3, 4))) == Fraction(3, 4))
print(unegyptian(egyptian(Fraction(39, 20))) == Fraction(39, 20))
print(unegyptian(egyptian(Fraction(127, 130))) == Fraction(127, 130))
print(unegyptian(egyptian(Fraction(5, 7))) == Fraction(5, 7))
print(unegyptian(egyptian(Fraction(1, 1))) == Fraction(1, 1))
print(unegyptian(egyptian(Fraction(2, 1))) == Fraction(2, 1))
print(unegyptian(egyptian(Fraction(3, 1))) == Fraction(3, 1))