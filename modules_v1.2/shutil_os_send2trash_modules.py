import shutil
import os
from send2trash import send2trash

# ####Copy 
# shutil.copy()                               # Copy & rename file
# shutil.copytree()                         # Copy & rename folder

# ####Move
# shutil.move()                               # Copy & rename file/folder 

# ####Delete
# shutil.rmtree()                              # delete entire folder permanatly
# os.unlinks()                                  # permanatly delete file
# os.rmdir()                                     # Remove empty folder permanantly
# send2trash()                                 # send the file to recyclybin

# ####Rename
#  os.rename()                                # Rename file or folder
# shutil.move()                               # Copy & rename file/folder 

# ######## Path
# #####################################
# #Relative path
#  .        -> This folder
# ..        -> Parent folder 

# os.chdir()                            # Change Directory
# print(os.listdir())                 # list contain files & folders
#  os.rename(<Old>, <New>)  # Rename file or folder
#  print(os.path.splitext(file))   # 1.jpg ->   ('1', '.jpg')
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
# os.unlinks(<path/file>)              # permanatly delete file
# os.rmdir(<path/file>)                 # Remove empty folder permanantly
#  os.walk(path)                            # it list-up folder/sub-folder/file





# # Copy file 
# shutil.copy(r"Concepts.txt" , r'modules_v1.2\Concepts.txt')

# # Copy & Rename file
# shutil.copy(r"Concepts.txt" , r'modules_v1.2\Conceptsv1.1.txt')

# Copy folder in other folder
# shutil.copytree(r'modules_v1.2', r'B:\courses\2-Automate the Boring Stuff with Python Programming\11. Files\modules_v1.2')

# Copy & Rename folder in other folder
# shutil.copytree(r'modules_v1.2', r'B:\courses\2-Automate the Boring Stuff with Python Programming\11. Files\modules_v1.3')

# Move file
# shutil.move(r'Concepts.txt', r'B:\courses\2-Automate the Boring Stuff with Python Programming\11. Files\Concepts.txt')

# Move & rename file/folder
# Note: This is used to rename file
# shutil.move(r'Concepts.txt', r'B:\courses\2-Automate the Boring Stuff with Python Programming\11. Files\Concepts1.txt')

# Delete Folder permanently
# shutil.rmtree(<path/folder>)      -> delete entire folder               
# #####################################
# #Relative path
#  .        -> This folder
# ..        -> Parent folder 

# os.chdir()                            # Change Directory
# print(os.listdir())                 # list contain files & folders
#  os.rename(<Old>, <New>)  # Rename file or folder
#  print(os.path.splitext(file))   # 1.jpg ->   ('1', '.jpg')
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
# os.unlinks(<path/file>)              # permanatly delete file
# os.rmdir(<path/file>)                 # Remove empty folder permanantly
#  os.walk(path)                            # it list-up folder/sub-folder/file



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

# ###################To know exact path
# finalPath = ''
# for path, folder, file in os.walk(os.getcwd()):
#     # Considering each path whose ends with img(i.e; img folder)
#     if path.endswith('img'):
#         # join path e.g;  "C:\Users\Hamza Arain\Desktop\Alien Project v1.3\Ch12_Firing_fromShip\img"    +   "ship.bmp(i.e; image file)"  
#         finalPath = os.path.join(path, 'starfield.bmp')
#         break
#  ################################
# send2trash(<path/file>)       # send the file to recyclybin