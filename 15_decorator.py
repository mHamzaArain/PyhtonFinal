# decorator -> return name, doc, time, Check proper input by passing args

from functools import wraps             # Redirect  org function
import time                                        # Calculate executable time

def super_decorator(dataType, dataType2 = None):
    '''Return name, doc-string, time,
     check proper input(s) by passing args'''

    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            # Return name & doc-string of functoins
            print(f'Function: {function.__name__}')             # name
            print(f'Docstring: {function.__doc__}')               # doc-string

            # check all args given perfectly
            # all() -> Return true if condition passed -> True
            if all( [type(arg) == dataType or type(arg) == dataType2 for arg in args] ):
                t1 = time.time() # time before execution
                returnable = function(*args, *kwargs)
                t2 = time.time() #time after execution
                print(f'Time: {t2-t1}s') # final time
                return returnable
            return 'Invalid argument'
        return wrapper
    return decorator

@super_decorator(int, float)
def add(*args):
    '''This is adder'''
    return sum(args)

print(add(1,2,3,4.0))       #perfect input
# print(add(1,2,3,4.0, []))   #falty input