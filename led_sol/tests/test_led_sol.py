#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `led_sol` package."""


import unittest

from led_sol import led_sol


class TestLed_sol(unittest.TestCase):
    

    def setUp(self):
        matrix = led_sol.create(999)
    
        led_sol.turnOnOrOff(499, 500, 499, 500)
    
        print(matrix[499][500])

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""
        
        
    
