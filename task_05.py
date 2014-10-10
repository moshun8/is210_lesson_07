#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Changing the Value of a Key"""


import data


#change to wolverine without copying or altering original
data.SUPERHEROES['Logan']['alias'] = 'Wolverine'
print data.SUPERHEROES['Logan']