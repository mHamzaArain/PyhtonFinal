# #1. max()             -> give maximum
# #2. min()              -> give minimum
# #3. filter()             -> returns only True
# #4. map()             -> return both T\F
# #5. enumerate()   -> return index along item in list
# #6. zip()                -> each item passed and then paired through loop 
# #7. sorted()          -> sort throgh list/dictionary
# #8. all()                 -> return T -> if all item in list is T  
# #9. any()               -> return T -> if any item in list is T  
# #10. join()             -> string to join with item of or tuple
# #11. reduce()        -> to make soncise result from list(i.e; sum of all elements in list)

#####################1. max() & 2. min()            # -> return max & min respectively

# #Example 1:
# names = ['hamza', 'khurram', 'musab']

#max() ->it gives name on basis on length 
# print(max(names, key = lambda item : len(item)))    # -> khurram
# #min() ->it gives name on basis on length 
# print(min(names, key = lambda item : len(item)))    # -> hamza

# # #Example 2:
# students_dict = {     #dict inside dict
#     'hamza' : {'score' : 10, 'age' : 22},
#     'uzair' : { 'score' : 70, 'age' : 20},
#     'khurram' : { 'score' : 40, 'age' : 20}
# }
# # print(  max( students_dict, key = lambda item : students_dict[item]['score'] ) )# student[key][value]
# #                                                                            #uzair
# # #Example 3:
# students_lst = [      #dict inside list
#     {'name' : 'hamza', 'score' : 10, 'age' : 22},
#     {'name' : 'uzair', 'score' : 70, 'age' : 20},
#     {'name' : 'khurram', 'score' : 40, 'age' : 20}
# ]
# #high scored person name
# print( min(students_lst, key = lambda a : a.get('score'))['name'] ) 
# #                                                                            #hamza

# #==========================================

#######################3. filter() & 4. map() -> return only T, return both T\F

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even = list( filter(lambda n : n%2 == 0, lst) ) # filter() 
# print(even)                                                     # -> [2, 4, 6, 8, 10]

is_even = list( map(lambda n : n%2 == 0, lst) )  #map()
print(is_even)                                              # -> [False, True, False, True, False,
#                                                                     # True, False, True, False, True]

# #==================================================

#######################5. enumerate()
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# odd_index =[print(index, end=' ') for index, item in enumerate(lst) if item%2 == 0]
# # -> 1 3 5 7 9 = index of odd numbers

# #====================================================

######################6. zip
# zip() -> pass n no. of lists as arg & return average of same index value
# e.g; [1, 2, 3] [4, 5, 6] --> (1+4)/2   (2+5)/2  (3+6)/2

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l3 = [7, 8 ,9]
# #extreme compact way
# avg  = lambda *args : list(sum(pair)/len(pair) for pair in zip(*args))
# print(avg(l1, l2, l3))          # -> [4.0, 5.0, 6.0]

# if any list has less element as compared-> zip won't for remainig element
# user_id = ['user1' , 'user2', ] # 1 less element, thus it zip upto 2 elements 
# names = ['hamza', 'uzair', 'khurram']
# print(tuple(zip(user_id, names)))       # -> (('user1', 'hamza'), ('user2', 'uzair'))

# #3. Using elements of iterable simultaneously
# lst1 = [1, 3, 5, 7, 9]
# lst2 = [2, 4, 6, 8, 10] 
# maximum = [i + j for i, j in zip(lst1, lst2)]
# print(maximum)

# #====================================================

#####################7. sorted()
# sorted( [lst/dict], key =  [function], revers = [True/False])

# guitars = [
#     {'model' : 'yammaha 1', 'price' : 8400},
#     {'model' : 'yammaha 2', 'price' : 5000},
#     {'model' : 'yammaha 3', 'price' : 35000},
#     {'model' : 'yammaha 4', 'price' : 45000}
# ]

# low_high = sorted(guitars, key = lambda dic : dic['price'])
# print(low_high) #low to high order

# high_low = sorted(guitars, key = lambda dic : dic['price'], reverse = True)
# print(high_low) #Reverse order

# #==================================================

##############################8. all() & 9. any()
# even_all = [2 ,4 ,6 ,8 , 10]
# even_any = [1, 3, 5, 7, 20] # true -> 20

#all()  - Ant false in list it returns false
# [True, True, False] ---> False
# [True, True, True]---> True 

# print( all([n%2 == 0 for n in even_all]) )  #even_true -> True

# #any() - Any true return true
# # [True, False False] ---> True
# print( any([n%2 == 0 for n in even_any]) )  #even_any -> True

# #==================================================

#############################10. join()
# n = ['a', 'b', 'c', 'd', 'e']
# t = ", ".join(n)
# s = "/ ".join(n)
# print(t)                    # -> a, b, c, d, e
# print(s)                    # -> a/ b/ c/ d/ e

# #==================================================

##############################11. reduce() 
# from functools import reduce

# lst = [1,2,3,4,2]   # 1*2*3 *4*5 = 48
# product_ofList = reduce(lambda x,y:x*y, lst)
# print(product_ofList) # 48

# # using reduce to compute sum of list  # 1+2+3+4+5 = 12
# sum_of_list = reduce(lambda a,b : a+b, lst) 
# print(sum_of_list)   # 12