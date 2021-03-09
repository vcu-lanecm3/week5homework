"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    """Required parameter, incoming_list, should be a list. Find the largest number in the list.""" 
    
    Max_Number = max(incoming_list)
    return Max_Number


def find_least_number(incoming_list):
    """Required parameter, incoming_list, should be a list. Find the smallest/least number in the list."""
    
    Min_Number = min(incoming_list)
    return Min_Number


def add_list_numbers(incoming_list):
    """Required parameter, incoming_list, should be a list. Add all the values together and return it."""
    
    Sum = sum(incoming_list)
    return Sum


def longest_value_key(incoming_dict):
    """Required parameter, incoming_dict, should be a dict. Find the KEY that has a value with the highest length, use the len() function"""
    
    keys = list(incoming_dict.keys())
    Values = list(incoming_dict.values())
    Longest_Value = max(Values, key = len)
    Position = Values.index(Longest_Value)
    Longest_Key = keys[Position]
    return Longest_Key
    