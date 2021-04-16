#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@date: 2021-04
@author: nboutin
'''

import unittest

from immo_perfo.cache import Cache
from immo_perfo import periods

from .res.test_cache.variable import Var1, Var2


class TestCache(unittest.TestCase):

    def test01_init(self):
        var1 = Var1()
        _ = Cache(var1)

    def test02a_get(self):
        '''
        Get value for unset period
        '''
        var1 = Var1()
        cv = Cache(var1)

        period = periods.period('2021')
        self.assertEqual(cv.get_value(period), None)

    def test02b_get(self):
        '''
        Get value for setted period
        '''
        var1 = Var1()
        cv = Cache(var1)

        period = periods.period('2021')
        value = 456
        cv.set_value(period, value)
        self.assertEqual(cv.get_value(period), value)

    def test03a_set(self):
        '''
        Set value with wrong value_type according to variable value_type
        '''
        var1 = Var1()
        cv = Cache(var1)

        period = periods.period('2021')
        value = "string_value_type"
        with self.assertRaises(Exception):
            cv.set_value(period, value)

    def test04a_default_value(self):
        '''
        default_value not defined
        '''
        var1 = Var1()
        cv = Cache(var1)

        self.assertEqual(cv.get_default_value, None)

    def test04b_default_value(self):
        var = Var2()
        cv = Cache(var)

        self.assertEqual(cv.get_default_value, 123)


if __name__ == "__main__":
    unittest.main()
