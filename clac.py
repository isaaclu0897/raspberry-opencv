#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 13:56:31 2018

@author: wei
"""

def pixel2real(value_p, weight_p, weight_r):
    return value_p * (weight_r / weight_p)

def real2pixel(value_r, weight_r, weight_p):
    return value_r * (weight_p / weight_r)

def weight_p(value_r, value_p, weight_r):
    return weight_r * (value_p / value_r)
    
    
    