################Functions
#1. Simple function
#3. doc string
#2. args 
#3. kwargs 
#4. Order of parameter (i.e; normalParameter, *args, defaultParameter, **kwargs)
#5.Lambda Expressions


###########################1. Simple Function
def simple():
    '''doc-string'''
    return None

#===================================

#########2. arg parameter working with list and tuple

# #to_power(3, *nums)
# # input -> [1, 2, 3]
# # output -> [1 , 8, 27]

def iterable_power(power, *args):
    '''Applying power through list or tuple'''
    if args :  return [(num ** power) for num in args]
    else: return  'Parse no data'

#Working with list                    
lst = [1, 2, 3, 4, 5]
print(iterable_power(2, *lst))           # -> [1, 4, 9, 16, 25]

# #Working with tuple
tupl = (1, 2, 3, 4, 5)
print(iterable_power(2, *tupl))        # -> [1, 4, 9, 16, 25]

# #Exceptional case
print(iterable_power(2))                  # -> Parse no data

print(iterable_power.__doc__)          # -> Applying power through list or tuple
#===================================

############3. kwargs

#Example 1:
#data modeling example
def func(list, **kwargs):
    '''Make reverese or unreverse the list  '''
    if kwargs.get('reverse_str'):  #[]get('reverse_str') == True
        return  [name[::-1].title() for name in list]
    else:
          return [name.title() for name in list]

names = ['hamza', 'arain']
print(func(names, reverse_str = True)) # -> ['Azmah', 'Niara']
print(func(names))                               #  -> ['Hamza', 'Arain']

print(func.__doc__)         # -> Make reverese or unreverse the list

#Example 2:
#kwargs as parameter
def dic(**kwargs):
    '''What is kwargs'''  
    for k, v in kwargs.items():  
        print(f"{k} : {v}")

# #Passing argument 
print(dic(first = "Hamza", last = "Arain")) 
#                                               # first : Hamza
#                                               # last : Arain
#                                               # None

# #kwargs as argument
d = {'name' : 'Hamza', 'age' : 22}
print(dic(**d)) #unpacking dictionary -> d**
#                                               # name : Hamza
#                                               # age : 22
#                                               # None
print(dic.__doc__)          # -> What is kwargs

#======================================

#4. Order of parameter

#Passing all parametre within order
####PADK
#Parametre
#args
#Defalut
#Kwargs

def parameter_order(name, *args, age = None , **kwargs):
    '''PADK Order'''
    print(f'Normal parameter : name : {name}')
    print(f'*args parameter : *args : {args}')
    print(f'Default parameter :  age : {age}')
    print(f'**kwargs parameter : **kwargs : {kwargs}')

#parameter values
name = "Hamza"     # parameter(normal)
lst = ['1',' 2', '3']        # list or tuple = (1, 2, 3) -> *args argument
age = 22                  #  Default parameter
d = {'1' : 'Python',  '2': 'C#', '3': 'JAVA Script'}   # **kwargs argument 

#Calling these all
parameter_order(name,       # parameter(normal)
                    age=22,            #  Default parameter
                            *lst,           # *args argument
                            **d)           # **kwargs argument 

                   # Normal parameter : name : Hamza
                  # *args parameter : *args : ('1', ' 2', '3')
                  # Default parameter :  age : 22
                  # **kwargs parameter : **kwargs : {'1': 'Python', '2': 'C#', '3': 'JAVA Script'}
print(parameter_order.__doc__)      # -> PADK Order

#=====================================================

##########5. Lambda Expressions
#Exmaple 1
#Method 1
def add(a, b):
    '''sum''' 
    return a+b
print(add(2,3))                             # 5            
print(add)                                    # <function add at 0x00000000001AC1E0>

print(add.__doc__)          # -> sum

# #Method 2
add_var = lambda a, b : a+b
print(add_var(2,3))                       # 5
print(add_var)                              # <function <lambda> at 0x000000000049BAE8>

#Example 2:
#Method 1
def is_even(list):
    '''return True if it is even''' 
    return  [True if n%2 == 0 else False for n in list]

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(is_even(lst))                # -> [False, True, False, True, False, True, False, True, False, True]

print(is_even.__doc__)      # -> return True if it is even

# #Method 2: Using lambda expressions
even = lambda list : [True if n%2 == 0 else False for n in list]
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(even(lst))                    # -> [False, True, False, True, False, True, False, True, False, True]