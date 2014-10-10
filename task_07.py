#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Iterating Dictionaries"""


DATA = {
    2: 7493945,
    76: 4654320,
    3: 4091979,
    90: 1824881,
    82: 714422,
    45: 1137701,
    10: 374362,
    0: 326226,
    -15: 417203,
    -56: 333525,
}


def inter_dict_funky_sum(weekend):
    running_total = 0
    for first, second in DATA.iteritems():
        running_total += second - first
    return running_total