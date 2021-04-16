#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@date: 2021-04
@author: nboutin
'''

import unittest

from .res.test_variable.variable import Var1, Var2


class TestVariable(unittest.TestCase):

    def test01a_attribute(self):

        var = Var1()
        self.assertEqual(var.name, 'Var1')
        self.assertEqual(var.value_type, int)
        self.assertEqual(var.period, 'MONTH')
        self.assertEqual(var.default_value, None)
        self.assertEqual(var.formula, None)

    def test01b_attribute(self):

        var = Var2()
        self.assertEqual(var.name, 'Var2')
        self.assertEqual(var.value_type, str)
        self.assertEqual(var.period, 'YEAR')
        self.assertEqual(var.default_value, "default")
        self.assertEqual(var.formula(None, None), "formula")


if __name__ == "__main__":
    unittest.main()
