# making dictionary of number and its  cube 
sqr = {f"{num} is" : num **3 for num in range(1, 11)}
print(sqr)

# Count each char in string
string = "Hamza".lower()
word_count = {char : string.count(char) for char in string}
print(word_count)

# using if-else
# dic = {1: 'odd', 2: 'even', 3: 'odd'}
even_odd = {i : ('even' if i%2 ==  0 else  'odd') for i in range(1, 11)}
print(even_odd) 
