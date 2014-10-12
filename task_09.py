#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Merging Data"""


import task_09_utility


DATA_FILES = [{
	'data': 'task_09_data/router_01.csv'},
	{'data': 'task_09_data/router_02.csv'},
	{'data': 'task_09_data/router_03.csv'
}]


def load_data(theData):
    """loads data"""
    counter = 0
    for thing in theData:
        newDict = {counter: task_09_utility.get_data(thing['data'])}
        counter += 1
    return newDict


#def merge_data(something):
#    aDict = {}
#    for key, value in something.iteritems():
#    info = value.split(',')
#    task_09_utility.sort_dict