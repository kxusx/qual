import json
import os
import re
import shutil
path = "combinedTest"
path2 = "renamedTest"
file_names = os.listdir(path)
file_names.sort()
i=0
for file_name in file_names:
    #change file name to test_{i+1}.mp3
    os.rename(path+"/"+file_name, path2+"/test_"+str(i+1)+".mp3")
    i+=1
