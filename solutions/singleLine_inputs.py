#Ask user to 3 inputs separated by commas 
#make it there average 
#print formatted output 

#a=[eval(b) for b in input().split(',')] 
#print( f"{sum(a)/len(a)}" )

num1, num2, num3 =input("Enter # three time separated by ','  : ").split(',')  #multiple inputs splited by comma
print(f"Average: { ((float(num1) + float(num3) + float(num3))/3) }") # py 3.6 formatted



#take 2 inputs, 1 is for name, 2nd for required char
#count len of name
#count character insesitively(e.g; "A" or "a")

name, query_char = input("Enter name & a character separated by ','  ").split(',') #multy inputs
#use len([]), [].count([]),  [].lower() [].strip()
print(f"Length: {len(name.strip().lower())} \nRequired Character: {name.strip().lower().count(query_char.strip().lower())}")
# name.strip().lower().count(char_query.strip().lower())
