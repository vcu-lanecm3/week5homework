"""Homework file for my students to have fun with some algorithms!"""


def find_greatest_number(incoming_list):
    """
    Required parameter, incoming_list,
    should be a list. Find the largest number in the list.
    """

    max_number = max(incoming_list)
    return max_number


def find_least_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """

    min_number = min(incoming_list)
    return min_number


def add_list_numbers(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Add all the values together and return it.
    """
    if incoming_list == None or incoming_list == []:
        list_sum = 0
    else:
        list_sum = sum(incoming_list)
    return list_sum


def longest_value_key(incoming_dict):
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length,
    use the len() function
    """
    if incoming_dict == None or incoming_dict == {}:
        longest_key = None
    else:
        dictkeys = list(incoming_dict.keys())
        dictvalues = list(incoming_dict.values())
        longest_value = max(dictvalues, key = len)
        position = dictvalues.index(longest_value)
        longest_key = dictkeys[position]
    return longest_key
