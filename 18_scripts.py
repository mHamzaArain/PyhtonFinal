#############################################Windows

# ############################Script.py
'''
#! python3
print("Hello World")

'''
# Note: 
# 1. recommend path ->  C:\Users\<user>\<Script_folder>
# 2. Run .py in cmd: <path>>py.exe C:\Users\<user>\<Script_folder>\script.py
#  Default Path-> Computer->Properties->Advanced System Settings-> Advanced ->
         # Environment Variables... -> System Variable -> path-> edit -> (insert recommended path) 
# 3. W+r -> (type script without path) -> hello.py

# 3. # #Shabang Line: #! python3

# #=============================================================

# ###########################Script.bat
'''
@py C:\Users\Family\MyPythonScripts\hello.py %*
@pause
'''

# Note: 
# 1. recommend path ->  C:\Users\<user>\<Script_folder>
# 2. Run .bat in cmd: <path>>py.exe C:\Users\<user>\<Script_folder>\script.bat
#  Default Path-> Computer->Properties->Advanced System Settings-> Advanced ->
         # Environment Variables... -> System Variable -> path-> edit -> (insert recommended path) 
# 3. W+r -> (type script without path) -> hello.bat

# 4. Remember
# 5. @py -> Don't show program behind of it
# 6. @pyw -> windowledd program(no GUI appear)
# 7. %*    -> Get ready to run next command

###########################################Linux

# ############################Script.py
'''
 #! /usr/bin/env python3
print("Hello World")

'''

# Note: 
# 1. recommend path ->  home\<user>\
# 2. Terminal -> chmod +x Script.py
# 3. Terminal -> ./Script.py

# 4. Shabang:      #! /usr/bin/env python3
