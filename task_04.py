#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Merging Dictionaries"""


import data


data.BANDS['Buckingham Nicks'] = {
    'Lindsey Buckingham': ['guitar', 'vocals'],
    'Stevie Nicks': ['vocals', 'tambourine']}

#  Not supposed to delete and readd, only update
data.BANDS['Fleetwood Mac'].update(data.BANDS['Buckingham Nicks'])