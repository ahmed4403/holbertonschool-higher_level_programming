#!/usr/bin/python3
'''This is a module'''
import json


def load_from_json_file(filename):
    '''This is a function'''
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
