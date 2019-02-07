def xor (a, b):
    result = 0
    if (a == 0 and b == 0) or (a == 1 and b == 1):
        result = 0
    elif (a == 0 and b == 1) or (a == 1 and b == 0):
        result = 1
    return result