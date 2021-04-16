#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@date: 2021-04
@author: nboutin
'''


class Variable:

    def __init__(self):
        # class introspection
        attr = {name: value for name, value in self.__class__.__dict__.items() if not name.startswith('__')}

        # Mandatory attribute
        self.name: str = self.__class__.__name__
        self.value_type = attr['value_type']
        self.period = attr['period']

        # Optional attribute
        self.default_value = attr.get('default_value', None)
        self.formula = attr.get('formula', None)
