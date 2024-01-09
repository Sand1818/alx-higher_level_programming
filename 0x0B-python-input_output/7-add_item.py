#!/usr/bin/python3
import json
import os
load = __import__('8-load_from_json_file').load_from_json_file
save = __import__('7-save_to_json_file').save_to_json_file

"""Adding arguments to json file"""

filename = "add_item.json"
try:
    my_obj = load(filename)
except:
    with open(filename, mode='w', encoding='UTF8') as f:
        f.write('')
        my_obj = []
if len(os.sys.argv) == 1:
    save(my_obj, filename)
else:
    for i in range(1, len(os.sys.argv)):
        my_obj.append(os.sys.argv[i])
    save(my_obj, filename)
