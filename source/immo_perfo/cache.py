#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@date: 2021-04
@author: nboutin
'''

from typing import Dict
from .variable import Variable
from . import periods


class Cache:

    def __init__(self, variable: Variable):
        self.variable: Variable = variable
        self.values: Dict[periods.Period, Variable.value_type] = {}

    def set_value(self, period: periods.Period, value):
        '''
        :param value: Variable.value_type
        '''
        if not isinstance(value, self.variable.value_type):
            raise Exception(
                "Input value_type {} is not compatible with Variable {} value_type {}".format(
                    type(value), self.variable.name, self.variable.value_type))
        self.values[period] = value

    def get_value(self, period: periods.Period):
        return self.values.get(period, None)

    @property
    def get_default_value(self):
        return self.variable.default_value
