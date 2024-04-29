def add_func(n1, n2):
    retVal = n1 + n2
    return retVal

def sub_func(n1, n2):
    retVal = n1 - n2
    return retVal

def trt_func(n1, n2):
    retVal = n1 * n2
    return retVal

def foq_func(n1, n2):
    retVal = n1 / n2
    return retVal








num1, num2, res = 100, 200, 0

res = add_func(num1, num2)
print(num1, '+', num2, '=', res)

res = sub_func(num1, num2)
print(num1, '-', num2, '=', res)

res = trt_func(num1, num2)
print(num1, '*', num2, '=', res)

res = foq_func(num1, num2)
print(num1, '/', num2, '=', res)



