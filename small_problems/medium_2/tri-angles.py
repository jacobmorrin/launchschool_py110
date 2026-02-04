"""
PROBLEM:
Right: One angle is a right angle (exactly 90 degrees).
Acute: All three angles are less than 90 degrees.
Obtuse: One angle is greater than 90 degrees.

To be a valid triangle, the sum of the angles must be exactly 180 degrees, 
and every angle must be greater than 0. If either of these conditions is 
not satisfied, the triangle is invalid.

Write a function that takes the three angles of a triangle as arguments 
and returns one of the following four strings representing the triangle's 
classification: 'right', 'acute', 'obtuse', or 'invalid'.

RULES:
You may assume that all angles have integer values, so you do not have to 
worry about floating point errors. You may also assume that the arguments 
are in degrees.

EXAMPLE:
print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True

DATA:
Input: ints
Output: String

ALGORITHM:
Check for validity

Classify triangle


"""

def is_invalid_triangle(angle1, angle2, angle3):
    angles_greater_than_zero = angle1 * angle2 * angle3 <= 0
    sum_to_180 = (angle1 + angle2 + angle3) != 180

    return angles_greater_than_zero or sum_to_180

def triangle(angle1, angle2, angle3):
    angles = (angle1, angle2, angle3)
    
    if is_invalid_triangle(angle1, angle2, angle3):
        return "invalid"
    elif 90 in angles:
        return "right"
    elif all(angle < 90 for angle in angles):
        return "acute"
    else:
        return "obtuse"

print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True