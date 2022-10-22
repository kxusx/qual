import os
import re
import shutil

path2 = "combinedTest"
path = "div/test"
folder_names = os.listdir(path)
listy = []
for folder in folder_names:
    if(folder!=".DS_Store"):
        file_names = os.listdir(path+"/"+folder)
        for file in file_names:
            print(file)
            shutil.move(path+"/"+folder+"/"+file, path2+"/"+file)
