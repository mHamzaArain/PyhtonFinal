def even_generator(n):
    for i in range(2, n+1, 2): yield i

for i in even_generator(9): # calling f() with loop
     print(i, end = ' ')
print()

# making f() as obj
numbers = even_generator(10)

# printing numbers 1st time
for number in numbers:
    print(number, end = ' ')

# this will not work 2nd time -> since gen, delete data from memory 
for number in numbers:
    print(number)