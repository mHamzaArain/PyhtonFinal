##################################Text files
## Functions
# open()        -> to open .txt file in program
# close()        -> Close .txt file in program
# encoding()    -> read data from given encoding scheme
# read()          -> Read whole .txt data
# readline()    ->  Read .txt data line by line
# readlines()[:2]   -> Read text all line by line, slicing is optional -> read 2 lines 
# write()         -> write data on .txt file 
# tell()            -> Current positon of prompt in .txt file
# seek()            -> Move positon of prompt in .txt file
# file.name     -> give path of file we are working with 

### Encoding scheme -> encoding = 'utf-8'

### Modes for .txt file
# r         -> read file as string  (default)
# a         -> create unpresent file & append
# w        -> create unpresent file & re-wrirte 
# r+        -> Not create unpresent file & over write by default from cudor position 0
#                   although we overcome on it by moving cursor
# x         -> create .txt file if not exist
# +         -> read and write(i.e; update)
# t          -> text mode default (i.e; open file with text mode)
# b         -> binary mode
# rt           -> Read text (default)

############1. Move prompt/cursor in reading file
file = "path"
with open(file) as f: 
    print(f'Cursor: {f.tell()}')          # tell()         ->  Current cursor position
    print(f.read())                         # read()       ->  Read whole data
    print(f'Cursor: {f.seek(0)}')      # seek()       -> Moving cursor to position in  arg
    print(f.readline(), end = '')     # readline() ->  Read line remove space
    f.close()                                   # close()      ->   Always close file after working

###########2. Read character
file = 'path'
with open(file) as f:
    data = f.read(4)    # read 4 char     
    print(data)

############3. Read line by line till desired line 
file = "path"
with open(file, 'r') as f:   
    lines  = f.readlines() [:2]                 # readlines() -> contain 2 lines
    for  num, line in enumerate(lines):
        print(f'{num+1}.  {line}', end = '')
    f.close()
    print(f.name) # name -> name of file
    print(f.closed)  # closed -> check file has closed (True/False) 

###########4. Read emojis
emoji = 'path'
with open(emoji, 'r', encoding = 'utf-8') as f:
    f.encoding()
    data = f.read()     
    print(data)

###########5. Write from 1 file to another file
transfer = reciever = 'path'
with open(transfer, 'r') as rf:
    with open(reciever, 'w') as wf:
        wf.write( rf.read() )

# #======================================================

###################################2. csv file

# from csv import DictWriter, DictReader 

# DictWriter()  -> Write file in dictionary from csv file
# DictReader() -> Read file in dictionary from csv file
# writeheader() -> Header to information for column(i.e; name, phone, email)
# writerow()       -> Write row wise

################1. Reading\Writting csv

from csv import DictReader, DictWriter
readFile = writeFile = 'path'
with open(readFile) as rf:
    with open(writeFile, 'w', newline = '') as wf:
        csvRead = DictReader(rf)  #Read

        csvWrite = DictWriter(wf, fieldnames = ['name', 'designation', 'salary']) #write
        csvWrite.writeheader()
        for row in csvRead:
            name, designation, salary = row['name'], row['designation'], row['salary']
            csvWrite.writerow(
                {
                    'name' :  name.title(),
                    'designation' : designation.upper(),
                    'salary' : salary
                }
            )

#====================================================

################2. Writting csv

from csv import DictWriter
target = 'path'
with open(target, 'w', newline = '') as f:        # newline -> instead of '\n'
    burnData = DictWriter(f, fieldnames = ['name', 'country', 'age'])
    burnData.writeheader()

    #Method 1 -> do it multiple times
    burnData.writerow(
        {
            'name' : 'hamza',
            'country' : 'Pakistan',
            'age' : 22
        }
    )
    
    #method 2 -> Do everything 1 time
    burnData.writerows(
        [
            {'name': 'Hamza', 'country': 'Pakistan', 'age': 22},
            {'name': 'Wajiha', 'country': 'Pakistan', 'age': 20},
            {'name': 'Mahnoor', 'country': 'Pakistan', 'age': 26},
        ]
    )

#==========================================================================================

#############################################3. json module

# json.load() -> Read json file
# json.dump() -> Write json file -> convert a Python datastructure to a JSON string

##################################2. Read

# import rhinoscriptsyntax as rs
import json

# prompt the user for a file to import
filter = "JSON file (*.json)|*.json|All Files (*.*)|*.*||"
# filename = rs.OpenFileName("Open JSON File", filter)
filename = 'path'
# Read JSON data into the datastore variable
if filename:
    with open(filename, 'r') as f:
        datastore = json.load(f)

# Use the new datastore datastructure
print*( datastore["office"]["parking"]["style"])

#####################################1. Write
import json
# import rhinoscriptsyntax as rs

#Get the file name for the new file to write
filter = "JSON File (*.json)|*.json|All Files (*.*)|*.*||"
# filename = rs.SaveFileName("Save JSON file as", filter)

# If the file name exists, write a JSON string into the file.
if filename:
    # Writing JSON data
    with open(filename, 'w') as f:
        json.dump(datastore, f)