"""
PROBLEM:
Write a function that takes the lengths of three sides.
Returns one of the following strings representing the triangle's
classification

equilateral -> all sides equal
isosceles -> two sides equal, third different
scalene -> all sides have different lengths
invalid -> see below

RULES:
For it to be a triangle:
sum of the two shortest sides must be greater than the longest
Every side > 0
If not these, invalid.

EXAMPLE: 
print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True

DATA:
input: ints
output: string

ALGORITHM:
Determine Triangle validity (helper function)
- Check to see if any side equals zero
    - if side1 or side2 or side3 == 0:
        return "invalid"

- Check to see if sides make sense
    - Add up sum of smaller sides
        - Insert into a list, sort, and add indices 0, 1

        

"""
def is_invalid_triangle(side1, side2, side3):
    sorted_sides = sorted([side1, side2, side3])

    has_zero_side = side1 * side2 * side3 <= 0
    sides_too_short = sorted_sides[0] + sorted_sides[1] <= sorted_sides[2]

    if has_zero_side or sides_too_short:
        return True
    
    return False

def triangle(side1, side2, side3):
    if is_invalid_triangle(side1, side2, side3):
        return "invalid"
    elif side1 == side2 == side3:
        return "equilateral"
    elif len({side1, side2, side3}) == 3:
        return "scalene"
    else:
        return "isosceles"

print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True