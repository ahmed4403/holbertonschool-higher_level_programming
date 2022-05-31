#!/usr/bin/python3
'''This is a moudle'''
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

f = open("add_item.json", "a")
try:
    newList = load_from_json_file("add_item.json")
except Exception:
    newList = []
save_to_json_file(newList + sys.argv[1:], "add_item.json")
f.close()
