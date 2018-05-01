#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 04:16:45 2018

@author: pi
"""
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setup(35,GPIO.OUT) #left clockwise
GPIO.setup(36,GPIO.OUT) #left counter clockwise 
GPIO.setup(37,GPIO.OUT) #right counter clockwise
GPIO.setup(38,GPIO.OUT) #right clockwise

print('motor on')
GPIO.output(35,GPIO.HIGH)
GPIO.output(38,GPIO.HIGH)
time.sleep(10)
print('motor shutdown')
GPIO.output(35,GPIO.LOW)
GPIO.output(38,GPIO.LOW)
time.sleep(1)
