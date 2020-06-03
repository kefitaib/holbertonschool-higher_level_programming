#!/usr/bin/python3
"""
Module
"""


import sys
l = __import__('8-load_from_json_file').load_from_json_file
s = __import__('7-save_to_json_file').save_to_json_file


list = []
try:
    list = l("add_item.json")

except Exception:
    print('[]')

list += sys.argv[1:]
s(list, "add_item.json")
