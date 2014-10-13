#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Merging data"""


import task_09_utility


DATA_FILES = [
    {'data': 'task_09_data/router_01.csv'},
    {'data': 'task_09_data/router_02.csv'},
    {'data': 'task_09_data/router_03.csv'}
]


def load_data(datalist):
    """accepts the DATA_FILES"""
    datadict = {}
    counter = 0
    for info in datalist:
        counter += 1
        datadict[counter] = task_09_utility.get_data(info['data'])
    return datadict


def merge_data(routerdict):
    """merging data"""
    merged = {}
    for rout_key, csv_info in routerdict.iteritems():
        for info in csv_info:
            clock = info.get('clock')
            month = clock[8:10]
            hour = clock[11:13]
            candidate_key = month, hour
            if candidate_key in merged:
                lst = merged[candidate_key]
            else:
                lst = [clock, 0, 0, 0]
            lst[rout_key] = info.get('value_avg')
            merged[candidate_key] = lst
    return task_09_utility.sort_dict(merged)