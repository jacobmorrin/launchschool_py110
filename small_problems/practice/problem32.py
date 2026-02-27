"""
P:
Write code that identifies whether a number is bouncy.
And a bouncy number is a number that has both ascending and descending digits.

E:
Ascending => 123, 3445, 2489
Descending => 321, 5443, 9842
Bouncy => 313, 92543

D:
Input: A list of its
Output is goiong to be the number of bouncy numbers in the list.

HL-A:
Init a count variable
Loop through each number in the list
    - ascending, descending, unknown = 0, 0, 0
    - Loop through two digits at a time using range - 1
        - if i < i + 1, then ascending += 1
        - if i > i + 1, then descending += 1
        - if i < i + 1, then unknown += 1

    Check if that number is bouncy
        if ascending > 0 and descending > 0:
            count += 1
        
    Return count

"""
def bouncyCount(lst):
    count = 0

    for num in lst:
        str_num = str(num)
        ascending = 0
        descending = 0

        for i in range(len(str_num) - 1):
            left = str_num[i]
            right = str_num[i + 1]
            
            if int(left) < int(right):
                ascending += 1
            elif  int(left) > int(right):
                descending += 1
        
        if ascending != 0 and descending != 0:
            count += 1

    return count

print(bouncyCount([]) == 0)
print(bouncyCount([11, 0, 345, 21]) == 0)
print(bouncyCount([121, 4114]) == 2)
print(bouncyCount([176, 442, 80701644]) == 2)