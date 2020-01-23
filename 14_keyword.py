
## 1. Variable scope
# global             -> variable declared outside of function -> accessed inside besides
                                                                                                # outside of function
# local                -> variable declared outside of function -> accessed inside besides
                                                                                                # inside of function

##2. break, continue & pass
# break          -> The break statement terminates the loop containing it.
#                     #  Control of the program flows to the statement immediately 
#                     # after the body of the loop. If break statement is inside
#                     # a nested loop (loop inside another loop),
#                     #  break will terminate the innermost loop. 

# continue      -> The continue statement is used to skip the rest of the code
#                          # inside a loop for the current iteration
#                           # only. Loop does not terminate but
#                           # continues on with the next iteration. 

# pass              -> to handle the condition without the
#                           #  loop being impacted in any way

# ##################1. variable scopes -> global keyword
x = 3 # global variable
def f():
    # x = 5  # local variable
    global x # menupulation globally
    print(x)

# #=======================================

#####################2. break, continue & pass

i = 2
for i in range(5):
    if i == 2:
        continue            # 0                    
    elif i ==4:               # 1 
        break                 # 3
    elif i < 4:
        pass
    print(i, end= ' ')
    i +=1