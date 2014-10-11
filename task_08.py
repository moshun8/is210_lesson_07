#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Dict Comprehensions"""


from data import FRUIT
shoplist = {'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1}

def get_cost_per_item(shoplist):
    """how much items cost"""
    return {item: nums * FRUIT.get(item) for item, nums in shoplist.iteritems() if item in FRUIT}
#  .get(key) returns the value, not the key. 
#  .values() was returning all the values, not the ones I wanted


def get_total_cost(shoplist):
    """finds total cost"""
    return sum(get_cost_per_item(shoplist).itervalues())
#  itervalues goes through the values like iteritems goes through items and values
#  good website: http://python-future.org/compatible_idioms.html

print get_cost_per_item({'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1})
print get_total_cost({'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1})