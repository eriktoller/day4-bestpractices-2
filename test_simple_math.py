# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 14:42:01 2021

@author: erito849
"""

from simple_math import simple_add, simple_sub, simple_mult, simple_div, poly_first, poly_second
import pytest

@pytest.mark.parametrize("a,b, expected", [	
    (0,1, 1),
    (1,1, 2),
    (3,15, 18)
])
def test_simple_add(a,b, expected):
    assert simple_add(a,b) == expected

@pytest.mark.parametrize("a,b, expected", [	
    (0,1, -1),
    (1,1, 0),
    (3,15, -12)
])
def test_simple_sub(a,b, expected):
    assert simple_sub(a,b) == expected

@pytest.mark.parametrize("a,b, expected", [	
    (1,1, 1),
    (4,2, 8),
    (17,5, 85)
])
def test_simple_mult(a,b, expected):
    assert simple_mult(a,b) == expected

@pytest.mark.parametrize("a,b, expected", [	
    (1,1, 1),
    (4,2, 2),
    (17,5, 3.4)
])
def test_simple_div(a,b, expected):
    assert simple_div(a,b) == expected

@pytest.mark.parametrize("x,a0,a1, expected", [	
    (1,1,2, 3),
    (4,2,1, 6),
    (17,5,3, 56)
])
def test_poly_first(x,a0,a1, expected):
    assert poly_first(x,a0,a1) == expected

@pytest.mark.parametrize("x,a0,a1,a2, expected", [	
    (1,1,1,1, 3),
    (2,3,4,5, 31),
    (6,23,515,8, 3401)
])
def test_poly_second(x,a0,a1,a2, expected):
    assert poly_second(x,a0,a1,a2) == expected