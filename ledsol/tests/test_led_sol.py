#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `led_sol` package."""


import unittest

from ledsol import ledsol


class TestLed_sol(unittest.TestCase):
    

    def setUp(self):
        
        L = 9
        
        matrix = ledsol.create(L)
        
    
        ledsol.turnOnOrOff(0, 9, 0, 9, matrix)
        
        for i in matrix:
            print(i)
    
        print(ledsol.check(matrix, L))
        
    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""
        
        
    
