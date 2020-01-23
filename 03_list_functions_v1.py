numbers = [2, 7, 9, 11, 3]
alphabets = ['z', 'a', 'Z', 'A']

# list functions
numbers.remove(9)       # remove() -> [2, 7, 11, 3]         (remove 9 in the list)
del numbers[0]         # [7, 9, 11, 3]

numbers.pop()               # pop()      -> [2, 7, 9, 11]          (pop last item from list that can be stored in var to use it)

numbers.sort()               # sort()      -> [2, 3, 7, 9, 11]       (sort in order numerically)
numbers.sort(reverse=True)  # sort(reverse=True)    -> [11, 9, 7, 3, 2]     (sort in reverse order alphanumerically)
alphabets.sort()            # sort()        -> ['A', 'Z','a', 'z']      (Sort in ASII-batical order)
alphabets.sort(key=str.lower)            # sort()        -> ['A', 'a','Z', 'z']      (Sort in alphabatiacl order)

numbers.reverse()          # reverse() ->[3, 11, 9, 7, 2]       (reverse list)
numbers.insert(2, 67)     # insert()   -> [2, 7, 67, 9, 11, 3] (insert 67 at position 2) 
numbers.index(7)        # index()   -> 1    (gives index of element)

list('hello')

print(numbers)

