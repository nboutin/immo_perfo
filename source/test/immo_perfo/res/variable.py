#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@date: 2021-04
@author: nboutin
'''

from immo_perfo.variable import Variable


class Var1(Variable):
    '''
    all mandatory attribute
    '''
    value_type = int
    period = 'MONTH'


class Var2(Variable):
    '''
    all mandatory attribute
    '''
    value_type = str
    period = 'YEAR'
    default_value = "default"

    def formula(population, period):
        return "formula"
