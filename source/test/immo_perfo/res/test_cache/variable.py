#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@date: 2021-04
@author: nboutin
'''

from immo_perfo.variable import Variable


class Var1(Variable):
    value_type = int
    period = 'MONTH'


class Var2(Variable):
    value_type = int
    period = 'MONTH'
    default_value = 123
