"""

ALGORITHM:
- Create blank list for stack []
- Set register to zero
- Get inputs into a list
- Test whether the command is a number
- if its a number go to the next command

"""


def minilang(inputs: str):
    register = 0
    stack = []

    for token in inputs.split(' '):
        if token == 'PUSH':
            stack.append(register)
        elif token == 'ADD':
            register += stack.pop()
        elif token == 'SUB':
            register -= stack.pop()
        elif token == 'MULT':
            register *= stack.pop()
        elif token == 'DIV':
            register //= stack.pop()
        elif token == 'REMAINDER':
            register %= stack.pop()
        elif token == 'POP':
            register = stack.pop()
        elif token == 'PRINT':
            print(register)
        else:
            register = int(token)
    
    return register

# minilang('PRINT')
# # 0

# minilang('5 PUSH 3 MULT PRINT')
# # # 15

# minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# # 5
# # 3
# # 8

# minilang('5 PUSH POP PRINT')
# # 5

# minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# # 5
# # 10
# # 4
# # 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

minilang('6 PUSH')
# (nothing is printed)