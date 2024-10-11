def xor(args1, args2):
    '''
        or - returns a truthy value if either or both of its operands are truthy, a falsy value if both operands are falsy
            TT - T
            TF - T
            FT - T
            FF - F
        and -  returns a truthy value if both of its operands are truthy, and a falsy value if either operand is falsy.
            TT - T
            TF - F
            FT - F
            FF - F
        xor
            TT - F
            TF - T
            FT - T
            FF - F
            
    '''
    if (args1 and args2):
        return False
    elif (not args1 and not args2):
        return False
    else:
        return True

# Will Print True for all below:
print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)