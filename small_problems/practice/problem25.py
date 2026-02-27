"""
P:
Write a function that takes a string of integers as input and 
returns the number of substrings that result in an odd number 
when converted to an integer.

E:
solve("1341") # should return 7
solve("1357") # should return 10

D:
Input: s
Ooutput: I

A:
Use two loops to loop through all combinations


"""
def solve(s):
    lst = []
    count = 0
    for i in range(len(s) + 1):
        for j in range(i + 1, len(s) + 1):
            if int(s[i:j]) % 2 == 1:
                lst.append(s[i:j])
                count += 1
    print(lst)
    return count

solve("1341")