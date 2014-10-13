#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Merging Data"""


import task_09_utility


DATA_FILES = [{
    'data': 'task_09_data/router_01.csv'},
    {'data': 'task_09_data/router_02.csv'},
    {'data': 'task_09_data/router_03.csv'}]


def load_data(the_data):
    """loads data"""
    counter = 0
    new_dict = {}
    for thing in the_data:
        new_dict[counter] = task_09_utility.get_data(thing['data'])
        counter += 1
    return new_dict


def merge_data(something):
    merged = {}
    for key, router_info in something.iteritems():
        clock = router_info['clock']
        day = clock[8:10]
        hour = clock[11:13]
        candidate_key = [day, hour]
        if candidate_key in merged:
            lst = merged[candidate_key, key['clock'], key['value_avg']]
        else:
            lst = [clock, 0, 0, 0]
    sorted_dict = task_09_utility.sort_dict(merged)
    return sorted_dict


loaded_data = load_data(DATA_FILES)
print merge_data(loaded_data)