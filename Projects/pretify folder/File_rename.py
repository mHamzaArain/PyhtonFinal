
# Oh soldier Prettify my Folder

# path, dictionary file, format

# def soldier("C://", "harry.txt", "jpg")

import os
def soldier(path, format, file):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    print(files)
    with open(file) as f:
        filelist = f.read().split("\n")

    for file in files:
        if file not in filelist:
            os.rename(file, file.capitalize())

        # print(os.path.splitext(file))       ('1', '.jpg')
        if os.path.splitext(file)[1] == format:
            os.rename(file, f"{i}{format}")
            i +=1

path = r'C:\Users\Family\Desktop\Practice_v1.4\Projects\pretify folder'
soldier(path=path, format= ".jpg", file='check.txt' )
