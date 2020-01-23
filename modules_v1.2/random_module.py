import random

# random.randint(start, end)      -> return any no. from start to end 
# rand = random.random() * n   -> return any float no. b/w  1 to n 
# choice = random.choice()        -> return any item in the lst pass through choice(lst)

random = random.randint(1, 6)   # return any no. b\w start and end no.
print(random)   # -> 3

rand = random.random() * 10  #  gives any float no. b/w  * n -> *10
print(rand)         # -> 4.2930959230219825

lst = ['hamza', 'wajiha', 'mahnoor']
choice = random.choice(lst)
print(choice)   # -> wajiha