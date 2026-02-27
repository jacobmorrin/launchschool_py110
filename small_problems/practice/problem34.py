"""
P:
'''
You live in the city of Cartesia where all roads are laid out in a perfect grid. 
You arrived ten minutes too early to an appointment, so you decided to take the 
opportunity to go for a short walk.

The city provides its citizens with a Walk Generating App on their phones -- every 
time you press the button it sends you a list of one-letter strings representing 
directions to walk (e.g., ['n', 's', 'w', 'e']). You always walk only a single block
in a direction, and you know it takes you one minute to traverse one city block.

Create a function that will return True if the walk the app gives you will take you 
exactly ten minutes (you don't want to be early or late!) and will, of course, return 
you to your starting point. Return False otherwise.

You will always receive a valid list containing a random assortment of direction letters
('n', 's', 'e', or 'w' only). It will never give you an empty list (that's not a walk, 
that's standing still!).

P:
Given a list of directions, write a function that will return true or false if the 
directions will get you back to where you started in 10 or fewer minutes

R:
1 direction equals one block equals one minutes

E:
[n, w, s, e] = True

D:
Input: Lists
Output: Boolean
List: Coordinates
x = 0
y = 0

A:
check length. if > 10
    return false
init x, y = 0, 0
loop through direction
    Add 1 for w, substract 1 for e from x
    Add 1 for n subtract 1 for s from y
return x == 0 and y == 0
'''
"""
def is_valid_walk(directions):
    if len(directions) > 10:
        return False
    
    x, y = 0, 0

    for direction in directions:
        if direction == 'e':
            x += 1
        elif direction == 'w':
            x += -1
        elif direction == 'n':
            y += 1
        elif direction == 's':
            y += -1
    return x == 0 and y == 0

print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']) == True)
print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']) == False)
print(is_valid_walk(['w']) == False)
print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']) == False)