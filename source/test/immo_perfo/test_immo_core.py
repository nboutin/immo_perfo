#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@date: 2021-04
@author: nboutin
'''

import unittest
import os

from immo_perfo.immo_core import ImmoCore

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


class TestImmoCore(unittest.TestCase):

    def test01_load_variable(self):
        ic = ImmoCore()
        dir_path = os.path.join(location, 'res', 'test_immo_core', 'model1')
        ic.load_variables_from_directory(dir_path)

        self.assertEqual(ic.variables['M1V1'].name, "M1V1")
        self.assertEqual(ic.variables['M1V2'].name, "M1V2")
        self.assertEqual(ic.variables['SM1V1'].name, "SM1V1")
        self.assertEqual(ic.variables['SM1V2'].name, "SM1V2")


if __name__ == "__main__":
    unittest.main()
