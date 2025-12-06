"""
PROBLEM:
We have a list of lists and want to duplicate it. 
After making the copy, we modify the original list, 
but the copied list also seems to be affected:

import copy

original = [[1], [2], [3]]
copied = copy.copy(original)

original[0][0] = 99

print(copied[0] == [1])

The problem is that copy.copy makes a shallow copy, which means that 
it creates a new object for the outer list, but retains the references 
to nested lists. So original[0][0] and copied[0][0] are references to the
same objects. The solution is to make a deep copy.

"""
import copy

original = [[1], [2], [3]]
copied = copy.deepcopy(original)

original[0][0] = 99

print(copied[0] == [1])

