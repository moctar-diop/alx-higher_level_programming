#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Replace a element of a list at a specific"""
    if idx > 0 and idx < len(my_list):
        my_list[idx] = element 
    return (my_list)
