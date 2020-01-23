import os

# #Relative path
#  .        -> This folder
# ..        -> Parent folder 

# os.chdir()                            # Change Directory
# print(os.listdir())                 # list contain files & folders
#  os.rename(<Old>, <New>)  # Rename file or folder
#  print(os.path.splitext(file))       ('1', '.jpg')
#  print(os.path.splitext(file)[1])        '.jpg'
# os.path.join()                            # This join the path to file
# os.path.abspath()                     # Give absolute path of file
# os.path.basename()                      # Return filename without path
# os.path.dirname()                          # Return dir path without filename
# os.path.exists()                            # Checks file/folder exists
# os.path.isfile()                            # Check file exists
# os.path.isdir()                             # Check folder exists
# os.path.getsize()                       # give size of file
# os.makedirs()                           # Make folder inside solder

# print(os.path.join("file1", "file2", "file3"))      # -> file1\file2\file3
# print(os.chdir('C:\\') )
# print(os.path.abspath('Concepts.txt') )     # C:\Users\Family\Desktop\Practice_v1.6\Concepts.txt
# print(os.path.dirname(r'C:\Users\Family\Desktop\Practice_v1.6\Concepts.txt') )     # C:\Users\Family\Desktop\Practice_v1.6
# print(os.path.basename(r'C:\Users\Family\Desktop\Practice_v1.6\Concepts.txt') )     # Concepts.txt
# print(os.path.exists(r'C:\Users\Family\Desktop\Practice_v1.6\Concepts.txt') )     # True
# print(os.path.isfile(r'C:\Users\Family\Desktop\Practice_v1.6\Concepts.txt') )     # True    file
# print(os.path.isdir(r'C:\Users\Family\Desktop\Practice_v1.6') )     # True      Folder
# print(os.path.getsize(r'C:\Users\Family\Desktop\Practice_v1.6\Concepts.txt') )     # Size in bytes

# totalSize = 0
# path = r'C:\Users\Family\Desktop\Practice_v1.6'
# for filename in os.listdir(path):
#     print(filename)
#     # if folder in list  -> just contue to loop
#     if  os.path.isdir(os.path.join(path, filename)):
#         continue
#     # Total size of files in list in bytes
#     totalSize += os.path.getsize(os.path.join(path, filename))
# print(f'{totalSize/1000} MBs')

# os.makedirs(r"C:\Users\Family\Desktop\Practice_v1.6/Check/check2")    # make folders in inside folders