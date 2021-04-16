#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@date: 2021-04
@author: nboutin
'''

import unittest

from immo_perfo import periods


class TestPeriod(unittest.TestCase):

    def test01_period(self):

        p = periods.period('2021')
        self.assertEqual(p.unit, periods.YEAR)
        self.assertEqual(str(p.start), '2021-01-01')
        self.assertEqual(p.size, 1)

        p = periods.period(periods.ETERNITY)
        self.assertEqual(p.unit, periods.ETERNITY)
        self.assertEqual(str(p.start), '0001-01-01')
        self.assertEqual(p.size, float('inf'))


if __name__ == "__main__":
    unittest.main()
