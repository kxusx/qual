import os
import re
import shutil

pattern = "_[0-9]+"
path = "recordings"
file_names = os.listdir("recordings")
for file_name in file_names:
    
    my_list = re.split(r'(\d+)', file_name)
    lang = my_list[0]
    print(lang)  
    folder_name = lang
    
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    shutil.move(path+"/"+file_name, os.path.join(folder_name, file_name))
    # shutil.move(file_name, folder_name+file_name)