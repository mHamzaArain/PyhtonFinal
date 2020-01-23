name = "  hamzaARAIN is"
char = '4'
num = 1, 2, 3, 4
n = 4

variable = name.capitalize()                       #  capitalize() -> Hamzaarain
variable = name.title()                                #  title()         -> Hamzaarain
variable = name.lower()                             #  lower()      -> hamzaarain
variable = name.upper()                            #  upper()      -> HAMZAARAIN

variable = name.index("h")                           # index() -> 2
variable = name.endswith("is")                  # True
variable = name.startswith("hamza")             # False 

variable = name.join("."+char)    # join() -> .  hamzaARAIN is4  -> to concatinate
variable = name.replace("is", "are")            # replace()  -> hamzaARAIN are
variable = name.find("a", 2)                        # find()  -> ('item', index to start find ) 3th index after 2nd index 

variable = name.strip()                                # strip()  -> (move white spaces) amzaARAIN is
variable = name.rstrip()                                # strip()  -> (remove white spaces of R) amzaARAIN is
variable = name.lstrip()                                # strip()  -> (remove white spaces of l) amzaARAIN is
variable = name.rjust(10, '*')                      # rjust() -> return white spaces with string on right
variable = name.center(10, '=')                     # center() -> return white spaces with string on center
variable = name.ljust(10)                           # ljust() -> return white spaces with string on left


variable = name.count('a')                          # count()  -> total items
variable = len(name)                                    # len() -> (total char) 15     
variable = range(1, 5, 2)                                   # range() -> 1, 3 -> range(start, end+2, jump)

variable = type(name)                                   # type() ->  <class 'str'> used as T/F
variable = list(num)                                      # list()  -> [1, 2, 3, 4]
variable = tuple(num)                                   # tuple()  -> (1, 2, 3, 4)
variable = dict()                                             # empty dictinoary
variable = set(num)                                        # Converting into set {1, 2, 3, 4}
variable = float(n)                                          # float()  -> 4.0
variable = str(n)                                             # str() ->  '4' 
variable = int(n)                                              # int() -> 4

variable = input("enter name: ")                   # input()   -> to input

name1, name2 = ("Hamza, Arain").split(',')    # split() -> to split by char
#   |               |
# Hamza     Arain

variable = name.isupper()               # Checj string is upper
variable = name.lower()                 # Checj string is lower
variable = name.isascii()              # isascii() -> True -> T:if all ASCII in string
variable = char.isalpha()              # isascii() -> False  -> T: if all char in sring are aplhabatic not numeric
variable = char.isdecimal()          # isdecimal() -> True  -> T: if all char in sring are deciaml not alphabatic
variable = char.isalnum()              # isalnum() -> check all is number
variable = char.isspace()               # isspace() -> check white spaces
variable = char.istitle()               # istitle() -> check string is title

variable = max(5,7)                     # max() -> 7
variable = min(5,7)                      # min() -> 5

# print(variable)
# print(name1, name2)

