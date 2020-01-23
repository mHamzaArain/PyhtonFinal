# Note: It has no order

# dict()                # convert datatype into dictionary
# items()             # in  looping, prompt key & value 
# keys()               # in looping, prompt only leys
# values()             # in looping, prompt only values
# fromkeys()
# get()                # get value of key 
# setdefault()          # Add key & value 

### setdefault()
message = 'this is hamza'
counter = {}
for char in message:
    counter.setdefault(char, 0)
    counter[char] += 1   
print(counter)

### Accesssssing diictoinary
dic = {'a' : '1'}
print(dic.get("1", 'get'))
print(dic.get('a', ''))

dic['2'] = 'access'            # ADD or access key
print(dic['2'])        

# ## Cmoparison
[1,3,4] == [4,3,1]   # -> T as dict has no order 
#Example 1:
# you can change list into dict. which contain 2 elements inside tuple
example = [('a', 1), ('b', 2)]
print(dict(example))            # -> {'a': 1, 'b': 2}

#Example 2:
# Function takes number, and return dict.
# contanig cube of key
def cube_dict(n):
    d = dict.fromkeys(list(range(1, n +1)), 1) # d = {}
    print(d)                        # -> {1: 1, 2: 1, 3: 1} 
    for i in d:                                                  # for i in range(1, n +1)
        d[i] = i ** 3                                           # as it is as below
    return d
print(cube_dict(3))         # -> {1: 1, 2: 8, 3: 27}

# Example 3:
# Function takes number, and return dict.
#  contanig cube of key
def storing_data_dict():
    #this store data into dictionary
    d = {}
    d['name']     = input("Enter name: ").title()
    d['age']        = int(input("Enter age: "))
    d['movies']   = input("Enter movies: ").strip().title().split(',')
    d['tunes']     = input("Enter tunes: ").strip().title().split(',')
    return d

def   display_dict(d):
    # this represent data  
    for key, value in d.items():
        print(f"{key}          :    {value}")
    print()

display_dict(storing_data_dict())