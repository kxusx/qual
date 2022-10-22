from ctypes import sizeof
import os
import re
import shutil

path = "div/train"
path2 = "div/test"
folder_names = os.listdir(path2)
listy = []
for folder in folder_names:
    if(folder!=".DS_Store"):
        file_names = os.listdir(path2+"/"+folder)
        # size of filenames
        lent = len(file_names) 
        if(lent<1):
            # print(folder)
            listy.append(folder)
            # #delete folder
            # shutil.rmtree(path+"/"+folder)
            # shutil.rmtree(path2+"/"+folder)

#sort listy alphabetically
listy.sort()
print(listy)
    