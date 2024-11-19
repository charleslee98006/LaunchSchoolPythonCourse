def minilang(text):
    str_array = text.split()
    stack = []
    registered_value = 0
    for each in str_array:
        if each.isnumeric() or '-' in each:
            registered_value = int(each)
        elif each == 'PRINT':
            print(registered_value)
        elif each == 'PUSH':
            stack.append(int(registered_value))
        elif each == 'MULT':
            value = stack.pop(-1)
            registered_value *= value
        elif each == 'ADD':
            value = stack.pop(-1)
            registered_value += value
        elif each == 'SUB':
            value = stack.pop(-1)
            registered_value -= value
        elif each == 'DIV':
            value = stack.pop(-1)
            registered_value //= value
        elif each == 'REMAINDER':
            value = stack.pop(-1)
            registered_value %= value
        elif each == 'POP':
            registered_value = stack.pop(-1)
        
minilang('PRINT') == 0
# 0

minilang('5 PUSH 3 MULT PRINT')
# # 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# # 5
# # 3
# # 8

minilang('5 PUSH POP PRINT')
# # 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# # 5
# # 10
# # 4
# # 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# # 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# # 8

minilang('6 PUSH')
# # (nothing is printed)