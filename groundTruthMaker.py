import json
import os
import re
import shutil
path = "combinedTest"
file_names = os.listdir(path)

answers = {}
#declare i to 0
i = 0
#sort file_names alphabetically
file_names.sort()
for file_name in file_names:
    
    my_list = re.split(r'(\d+)', file_name)
    lang = my_list[0]
    #json object key is test_{i+1} and value is lang
    answers["test_"+str(i+1)] = lang
    # answers[f"test_{i+1}"] = f"accent_{lang}"
    i+=1

with open("truth.json", "w") as f:
		json.dump(answers, f)

