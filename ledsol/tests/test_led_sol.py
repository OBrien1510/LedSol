#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `led_sol` package."""


import unittest

from ledsol import ledsol


class TestLed_sol(unittest.TestCase):
    

    def setUp(self):
        
        matrix = ledsol.create(999)
    
        ledsol.turnOnOrOff(499, 500, 499, 500, matrix)
    
        print(check(matrix))
        
    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""
        
        
    
