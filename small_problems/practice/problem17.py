"""
P:
Write a function that takes a list of ints as an argument.
Determine the minimum integer that can be appended to the list
such that the sum of the list equals the closest prime number that is greater
than the current sum of the numbers.

E:
For example, the numbers in [1, 2, 3] sum to 6. The nearest prime number greater 
than 6 is 7. Thus, we can add 1 to the list to sum to 7.

print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)

D:
Input: list
Output: INt

A:
Find the sum of the list
From there use helper function to find next prime
Return difference between next prime and sum
"""
def next_prime_finder(n):
    numerator = n + 1
    
    while True:
        for denominator in range(2, numerator):
            if numerator % denominator == 0:
                break
        else:
            return numerator

        numerator += 1

def nearest_prime_sum(lst):
    lst_sum = sum(lst)
    next_prime = next_prime_finder(lst_sum)
    return next_prime - lst_sum

# print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
# print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
# print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37