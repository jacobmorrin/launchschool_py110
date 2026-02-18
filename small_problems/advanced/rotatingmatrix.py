"""
P:
- Write a function that takes an arbitrary MxN matrix.
- Rotate the matrix 90 degrees
- Return the new rotated matrix. Don't mutate the original.

E:
3  4  1
9  7  5

9  3
7  4
5  1


00 01 02
10 11 12

00 -> 01
01 -> 11
02 -> 21

10 -> 00
11 -> 10
12 -> 20



D:
Boolean: No
Number: No
String: No
Array: Yes. Need to create new array


Algorithm:
- Find rows, columns of input matrix x 
- Create the rotated array (columns x rows) x
- Populate the new array



"""

def rotate90(input_matrix):
    rows = len(input_matrix) #0 1
    columns = len(input_matrix[0]) #0 1 2 

    rotated90 = [[] for _ in range(columns)]

    for row in range(rows):
        for col in range(columns):
            rotated90[col].insert(0, input_matrix[row][col])

    return rotated90

matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]

new_matrix1 = rotate90(matrix1)
new_matrix2 = rotate90(matrix2)
new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# These examples should all print True
print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
print(new_matrix3 == matrix2)