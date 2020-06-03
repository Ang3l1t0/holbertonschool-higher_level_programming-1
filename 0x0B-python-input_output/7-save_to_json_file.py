#!/usr/bin/python3
"""[Save Object to a file]
"""
import json


def save_to_json_file(my_obj, filename):
    """[save_to_json_file]
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
