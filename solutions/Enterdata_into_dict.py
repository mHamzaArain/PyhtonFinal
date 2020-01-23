# Function takes number, and return dict.
#  contanig cube of key
def storing_data_dict():
    #this store data into dictionary
    d = {}
    d['name']     = input("Enter name: ").title()
    d['age']        = int(input("Enter age: "))
    d['movies']   = input("Enter movies: ").strip().title().split(',')
    d['tunes']     = input("Enter tunes: ").strip().title().split(',')
    return d

def display_dict(d):
    #this represent data 
    for key, value in d.items():
        print(f"{key}          :    {value}")
    print()

display_dict(storing_data_dict())