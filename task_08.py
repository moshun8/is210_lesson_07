#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Dict Comprehensions"""


from data import FRUIT


def get_cost_per_item(shoplist):
    """how much items cost"""
    return {item: nums * FRUIT.get(item) for item, nums in shoplist.iteritems() if item in FRUIT}


def get_total_cost(shoplist):
    """finds total cost"""
    return sum(get_cost_per_item(shoplist).itervalues())