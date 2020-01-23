# Files sizes in specific folder(i.e; contain files & folders)

def total_files_size(path):
    import os
    totalSize = 0
    for filename in os.listdir(path):
        # if folder in list  -> just contue to loop
        if  os.path.isfile(os.path.join(path, filename)):     
            # Total size of files in list in bytes
            totalSize += os.path.getsize(os.path.join(path, filename))
    # bytes/1024 -> MBs
    return totalSize/1024

path =  r'C:\Users\Family\Desktop\Practice_v1.6'
print(f"{ total_files_size(path) } MBs" )
