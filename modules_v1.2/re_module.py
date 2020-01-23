import re
# re.compiler()
# search()
# findall()
# group()
# | 

"""
# #################Website for direct practice
https://regex101.com/

# #################Function 	Description

re.findall 	Returns a list containing all matches
re.search 	Returns a Match object if there is a match anywhere in the string
re.split 	Returns a list where the string has been split at each match
re.sub 	Replaces one or many matches with a string

# #####################Special Sequences

\A 	Returns a match if the specified characters are at the beginning of the string 	"\AThe" 	
\b 	Returns a match where the specified characters are at the beginning or at the end of a word 	r"\bain"
r"ain\b" 	

\B 	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word 	r"\Bain"
r"ain\B" 	

\d 	Returns a match where the string contains digits (numbers from 0-9) 	"\d" 	
\D 	Returns a match where the string DOES NOT contain digits 	"\D" 	
\s 	Returns a match where the string contains a white space character 	"\s" 	
\S 	Returns a match where the string DOES NOT contain a white space character 	"\S" 	
\w 	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character) 	"\w" 	
\W 	Returns a match where the string DOES NOT contain any word characters 	"\W" 	
\Z 	Returns a match if the specified characters are at the end of the string 	"Spain\Z"

# ################################Metacharacters

Metacharacters are characters with a special meaning:
Character 	Description 	
[] 	A set of characters 	"[a-m]" 	
\ 	Signals a special sequence (can also be used to escape special characters) 	"\d" 	
. 	Any character (except newline character) 	"he..o" 	
^ 	Starts with 	"^hello" 	
$ 	Ends with 	"world$" 	
* 	Zero or more occurrences 	"aix*" 	
+ 	One or more occurrences 	"aix+" 	
{} 	Exactly the specified number of occurrences 	"al{2}" 	
| 	Either or 	"falls|stays" 	
() 	Capture and group 	  	
"""

# message = "Call me on 0300-3501901 or 0334-2843869"

# container = re.compile(r'\d\d\d\d-\d\d\d\d\d\d\d')      # making pattern of no.
# o_only = container.search(message)                                       # search pattern in str

# o_lst = container.findall(message)                                       # search pattern in str

# print(o_only)                    #       <re.Match object; span=(11, 23), match='0300-3501901'>
# print(o_only.group())        #       0300-3501901

# print(o_lst)
##############################################
# batRagex = re.compile(r'bat(man|mobile|bat)')
# container = batRagex.search("This is batman")
# print(container.group())  0300-3501301

#############################Optional
# msg = "Call me on +92-0300-3501901 or 0334-2843869"
# container = re.compile(r'(\+\d\d-)?\d\d\d\d-\d\d\d\d\d\d\d')   # +92-0300-3501901
# msg = 'batman vs batwoman'  # batman
# msg = 'batmen vs batwoman'  # batwomen
# container = re.compile(r'bat(wo)?man')  
# print(container.search(msg))

############## -> * -> in  pattern search n times
# msg = "batwowowoman"
# container = re.compile(r'bat(wo)*man')  # return only one time from multi repeatition 0 or more time
#                                                                 # batwowowoman
# print(container.search(msg).group())
 
# msg = "batman"
# container = re.compile(r'bat(wo)+man')  == None  # -> True 
# # return only one time from multi repeatition 1 or more times
# # batwowowoman
# print(container.search(msg).group())

#############################Escaping Syntax
# msg = "This contain +*? "
# container = re.compile(r'\+\*\?')   # -> True 
# # return only one time from multi repeatition 1 or more times
# # batwowowoman
# print(container.search(msg).group())        # +*?

# ? -> 0 or 1
# + -> 1 or more  
# *   -> 0 or more
# (x){n}-> exact {n} times
# (x){n,n}  -> Slicing

# msg = "123456789"
# container = re.compile(r'(\d){3,5}')   # -> True 
# # return only one time from multi repeatition 1 or more times
# # batwowowoman
# print(container.search(msg).group())        # 12345

# ##################################################################


# ################### search specific word in string
# content = 'Only we can, yes we can'
# word = 'can'

# def findWord(word, str):
#     content = re.findall(word, str)
#     print(content)  # ['can', 'can']

# findWord(word, content) # ['can', 'can']


# ################### make split list 
# content = 'Only we can, yes we can'
# word = '\s'

# def splitStr(word, str):
#     content = re.split(word, str)
#     print(content)  # ['Only', 'we', 'can,', 'yes', 'we', 'can']

# splitStr(word, content)  # ['Only', 
