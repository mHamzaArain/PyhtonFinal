# # if-elif-else
# try-except-finally

##Comperatives
#  ==   -> equals to
#  !=     -> not equals to
# >=    -> greater than equals to 
# <=    -> less than equals to

## Logic gates
# and    -> * (all true)
# or       -> + (not all true)
# not     -> not true 

########################## if-elif-else
var1 = 6
var2 = 56

if var1>var2:
    print("Greater")
elif var1==var2:
    print("Equal")
else:
    print("Lesser")

# Conditinals if-else inside list comorehensions
nums = list(range(1, 20+1))
all = [i * 2 if i%2 == 0 else -i for i in nums]  # -> [-1, 4, -3, 8, -5, 12, -7, 16, -9, 20]
print(all)

# using if-else dictoionary comprehension
# dic = {1: 'odd', 2: 'even', 3: 'odd'}
even_odd = {i : ('even' if i%2 ==  0 else  'odd') for i in range(1, 11)}
print(even_odd) 
# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd', 6: 'even', 7: 'odd', 8: 'even',
#  9: 'odd', 10: 'even'}

###################### try-except-finally
try:
    print("a")  # a
except:
    print('b')  # This won't print
finally:
    print('c')   # c