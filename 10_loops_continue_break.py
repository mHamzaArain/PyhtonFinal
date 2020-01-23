#####################Topics
# #1. for
# #2. while
# #3. break             -> This stop the loop and prompt out side of block
# #4. continue        -> This stop the loop but does'nt  go out side of block

###################################For loop

for i in range(1, 11):
    print(i, end=' ')       # 1 2 3 4 5 6 7 8 9 10

# #==========================

#Example 1: for loop for list inside llist
list1 = [ ["Harry", 1], ["Larry", 2],
          ["Carry", 6], ["Marie", 250]]
for item in list1:                               # ['Harry', 1]
    print(item)                                   # ['Larry', 2]
                                                        # ['Carry', 6]        
                                                        # ['Marie', 250]  
    
# #===============================

#Example 2: for loop for converted dictionary from list inside list
dict1 = dict(list1)
for item in dict1:                      # Harry
    print(item)                           # Larry
                                                # Carry
                                                # Marie

# #========================================

# #Example 3: For loop in dictioanry
for key, value in dict1.items():                   # Harry and lolly is  1
    print(key, "and lolly is ", value)              # Larry and lolly is  2
                                                                 # Carry and lolly is  6
                                                                 # Marie and lolly is  250
    
#Example 5: for loop in list comprehension
#even num -> num * 2
#odd num -> - num
nums = list(range(1, 11))  
all = [i * 2 if i%2 == 0 else -i for i in nums]  # -> [-1, 4, -3, 8, -5, 12, -7, 16, -9, 20]
print(all)

# Example 6:  for loop in dictionary comprehension
# using if-else dictoionary comprehension
dic = {1: 'odd', 2: 'even', 3: 'odd'}
even_odd = {i : ('even' if i%2 ==  0 else  'odd') for i in range(1, 11)}
print(even_odd) 
# #{1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd', 6: 'even', 7: 'odd', 8: 'even',
# #9: 'odd', 10: 'even'}

## Example 7: for loop in set comprehension
s = {i for i in range(1, 11)}
print(s)

##################################while loop
#Example 1:
# 1/True   -> only true work
while 1:
    print('while')

#0/False         -> false won't work
while not False:
    print("This will work after turning to true(i.e; not False)")

# Example 2:
game_over =False                # flag false
while not game_over:           # 1st time: flag not false = true,  2nd time: flag not true = false
    print("Game Over")
    game_over = True            # flag true

######################3. break & 4. continue
i = 1
while 1:
    if i == 5: print(i)  # 5
    elif i == 7:
        print(i)             # 7
        break
    i += 1
    continue
    print(i)                # It doesn't print anything
    