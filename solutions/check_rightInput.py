def adder(*args):
    if all( [ (type(arg) == int or  type(arg) == float) for arg in args ] ): #only int&float
        total = 0
        for i in args: total += i
        return total
    else: 
        return "Wrong input"

print(adder(1 ,3 ,0.9, [1], 'hamza' )) #wromg input
print(adder(1 ,0.3 )) #perfect input
