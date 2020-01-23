# Example 1:
# example = [  [1, 2, 3],  [1, 2, 3], [1, 2, 3]  ]
# Method 1:         ->  [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
new_list = []
for i in range(3):
    new_list.append([1, 2, 3])
print(new_list)

# Method 2:
nested__list_comp = [  [i for i in range(1, 4)] for j in range(3)  ]  # -> [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
print(nested__list_comp)  

# Example 2
# even num -> num * 2
# odd num -> - num

# Method 1
nums = list(range(1, 11))                               # -> [-1, 4, -3, 8, -5, 12, -7, 16, -9, 20]
new_list = []
for i in nums:
    if i%2 == 0:
        new_list.append(i * 2)
    else:
        new_list.append(-i)
print(new_list)

# Method 2
all = [i * 2 if i%2 == 0 else -i for i in nums]  # -> [-1, 4, -3, 8, -5, 12, -7, 16, -9, 20]
print(all)



##############List compresion

# Example 1
#  create list of  square  from 1, 10
sqr2 = [i ** 2 for i in range(1, 11)]       # -> [-1, 4, -3, 8, -5, 12, -7, 16, -9, 20]
print(sqr2)

# Example 2
# Creating list of negative numbers from -1, -10
negative2 = [-i for i in range(1, 11)]       # -> [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
print(negative2)

# Example 3
# Creating list of 1st char of each element from list
names = ['Kumail', 'Ayesha', 'Maham']               # -> ['K', 'A', 'M']
list_comp = [name[0] for name in names]
print(list_comp)

# Example 2
# make func that contain every data 
# and separate out only int and float 
# convert it into string
def int_float_separator(array):
    return [str(num) for num in array if type(num) == float or type(num) == int]

lst = [1, 0.1, "C", 's' ,[] ,{}, True, False, None,    [1, 0.1, "C", 's', [], {}],     {1: [], 2: {}} ]
print(int_float_separator(lst))             # -> ['1', '0.1']

# Example 5
# Making func() that reverse each element
def reverse_list(list):
    return [x[::-1] for x in lst]  # [x.reverse for x in lst]

lst = ['abc', 'tuv', 'xyz']         # -> ['cba', 'vut', 'zyx']
print(reverse_list(lst))










