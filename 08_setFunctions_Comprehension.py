s = set()                            # convert datetype into set
s.add(1)                            #  {1}
# s.add(2)                         # {2}
# s.remove(2)                   # remove 2 if it is in the set
s1 = {4, 6}                         # {4, 6}
print(s.isdisjoint(s1))         # set of s1 != set of s  -> True
print(s1)

# set Comprehension

# set of 1-100
s = {i for i in range(1, 11)}
print(s)

#set 1st char of each name
names = ['Hamza', 'Wajiha', 'Mahnoor']
char1 = {name[0] for name in names}
print(char1)