"""
PROBLEM:
Write a function called fibonacci that computes the nth Fibonacci number, 
where nth is an argument passed to the function:

EXAMPLE:
F(1) = 1
F(2) = 1
F(n) = F(n - 1) + F(n - 2)    (where n > 2)
print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True

1 1 2 3 5 
0 1 2 3 4

DATA:
Input: int
Output: Int

ALGORITHM:
if n = 3




"""
def fibonacci(n):
    sequence = []

    if n == 1 or n == 2:
        return 1
    
    for idx in range(n):
        if idx == 0 or idx == 1:
            sequence.append(1)
        else:
            sequence.append(sequence[idx - 1] + sequence[idx - 2])
    return sequence[-1]



print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True