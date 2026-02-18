"""
P:
Write a function that takes a list of lists
representing a matrix.

Return the transpose of the matrix, i.e. the
matrix that results when you swap the rows and columns.

R:
Don't modify the original matrix.

E:
matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

becomes

1  4  3
5  7  9
8  2  6

D: 
Input: matrix (lst of lsts)
Output: same

A:
00 --> 00
01 --> 10
02 --> 20

00 10 20
01 11 21
02 12 22

Create the blank matrix. --> Do we need to create the 3x3 now?
Get length of matrix.
Iterate through the elements of the input_matrix

matrix_size = len(input_matrix)

for row_idx in range(matrix_size):
    for column_idx in range(matrix_size):
        transposed_matrix[column_idx]




for row_idx in range(3):
    for column_idx in range(3):
        transposed_matrix[row_idx][row_idx] = matrix[row_idx][column_idx]


transposed_matrix = [[], [], []]
for row in matrix:

    [input_matrix[row_idx][column_idx] for row_idx in range(3)
                                       for column_idx in range(3)] 
    
"""

def transpose(input_matrix):
    matrix_size = len(input_matrix)
    transposed_matrix = [[] for _ in range(matrix_size)]

    for row_idx in range(matrix_size):
        for column_idx in range(matrix_size):
            transposed_matrix[column_idx].append(input_matrix[row_idx][column_idx])

    return transposed_matrix

matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])    