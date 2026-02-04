"""
PROBLEM:
Write a function that takes a year as an argument and returns the number of Friday the
13s in the year. The year will be greater than 1752. The same calendar will remain in use
into the future.

EXAMPLE:
print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True

DATA:
Input: int
Output: int

ALGORITHM:
Option 1:
- Get the day of the week for the first day of the year

- Create a list of tuples (Day, Date). 
- Count the number of (Friday, 13) there are.

"""
from datetime import date

def friday_the_13ths(year):
    unlucky_fridays = 0

    for month in range(1, 13):
        d = date(year, month, 13)
        
        if d.weekday() == 4:
            unlucky_fridays += 1
                
    return unlucky_fridays

print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True
