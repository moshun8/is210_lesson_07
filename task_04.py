#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Merging Dictionaries"""


import data


data.BANDS['Buckingham Nicks'] = {'Lindsey Buckingham': [
    'guitar', 'vocals'], 'Stevie Nicks': [
    'vocals', 'tambourine']}

AddToFM = data.BANDS['Buckingham Nicks']
data.BANDS.pop('Buckingham Nicks')
data.BANDS['Fleetwood Mac'].update(AddToFM)