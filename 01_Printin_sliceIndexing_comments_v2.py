########1.Printing
# 1.1. simple print
# 1.2. Escape Characters
# 1.3. Concatination with variable
# 1.4. f-string
# 1.5. format()
# 1.6. Print special character

########2. Indexing & slicing

########3. Comments
# 3.1. Single line comment
# 3.2. Single-quote multi-lines comment
# 3.3. Double -quote multi-lines comment

# =================================

##################1. Printing
# ####1.1:
print("Hello", end='')  
print("World", 'this', 'me', sep=' * ') # HelloWorld * this * me
print('''This will  
        jump to next line''')

# conversion specifier
print('%s: of class %s of %s' %('Hamza', 'BSCS', 'A' ))

# ####1.2: Python escape characters
# 1. \\" -> "
# 2. \\' -> '
# 3. \t  -> tab(i.e; 4 spaces)
# 4. \n -> newline
# 5. \r  -> raw input
print(" \"double-comma \'single-comma \ttab  \nnewline")
#                                                   #"double-comma 'single-comma    tab
#                                                   #newline

# ####1.3: Concatination with variable
var = "hamza" + \
    "hanif"

# print('This is ' + var)

# # ####1.4: f-string
print(f"This is {var}") # hamz
                        # hamza

# # ####1.5: format method  -> format()  
num = 100000                # ->  100,000
print("{:,}".format(num))

# # ####1.6: For raw input
print(r" \"  \'  \t  \n")

# # ####1.7: Special Character print
# #  emoji site:                https://unicode.org/emoji/charts/full-emoji-list.html
print("\U0001F970")    # this print emoji, U+1F970 ->
#                                     # replace '+' with three 0's & place '\' in the

# #==================================================

##############string indexing 
name = 'hamza'
print(name[0])          # h -> 
print(name[:-1])        # hamz ->    (last char not printed)
print(name[:])            # hamza ->  (print everything)
print(name[3:])          # za -> from 3rd index till the end
print(name[2:-2])       # m -> start from index 2 till 2nd last index which is not printed

# #==================================================

#############Coments
"""
This is a double comma, multiline Comment
"""
'''
This is a sigle-comma, multiline comment
'''