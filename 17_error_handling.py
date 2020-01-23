#############Errors
# ValueError                        -> Inappropraite arg for correct value type
# ZeroDivisionError             -> 2nd arg to division/modulo was zero
# TypeError                         -> Inappropriate arg given
# NotImplementedError      -> Non implemented error

###############################Raising Error

def add(a, b):
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        return a+b
    return TypeError('Entered wrong data type')

print(add(1, 2)) #work fine
print(add('1', '2')) #raise TypeError

# #==================================

###############################Raising Error

class Animal:
    def  __init__(self, name):
        self.name = name

    #Abstract method
    def animal_sound(self): #raise error for not defined mothod in subclass
        raise NotImplementedError('Define for each subclass')

class Dog(Animal): #it raise error as method not defined
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

class Cat(Animal): #it doesnt raise error as method defined
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def animal_sound(self): #method
        return 'mewo mewo'

doggy = Dog('Hari Lal', 'pug')
kitty = Cat('Tom', 'fish')
print(kitty.animal_sound())  # workable
print(doggy.animal_sound()) #raise error bcz method doesnt defined for subclass Dog 

# #=====================================================

###########################Make custom error
#Make custom error
class NameLengthShort(ValueError): #inherit ValueError cls
    pass

def name_len_prompt(name):
    if len(name) <= 8:
        raise NameLengthShort("Name is too short")

username = input('Enter name: ')
name_len_prompt(username)
print('Hello!' + username.title())

# #==================================

################################# try, except, else, finally
divide = lambda a, b: a/b # devode function

def asking(): #ask until ans is true
    while True: #infinite loop
        try:
            a = float(input("Enter numerator: "))
            b = float(input("Enter denominator: "))
            c = divide(a,b)
        except ZeroDivisionError:
            print('Denominator cant be zero')
        except ValueError:
            print('Only numbers allow')
        except:
             print('Unexpected error')
        else:
            print(c)
            break  
        finally:
            print('\n**********************')
asking()