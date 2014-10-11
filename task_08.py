#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Dict Comprehensions"""


from data import FRUIT
shoplist = {'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1}

def get_cost_per_item(shoplist):
    """how much items cost"""
    return {item: nums * FRUIT.values() for item, nums in shoplist.iteritems() if item in FRUIT}
    #  return fruit_cost

def get_total_cost(shoplist):
    """finds total cost"""
    return sum(get_cost_per_item.values(shoplist))

print get_cost_per_item({'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1})
print get_total_cost({'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1})
