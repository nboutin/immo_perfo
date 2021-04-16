#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@date: 2021-04
@author: nboutin
'''

from immo_perfo.variable import Variable


class M1V1(Variable):
    value_type = int
    period = 'MONTH'


class M1V2(Variable):
    value_type = int
    period = 'MONTH'
