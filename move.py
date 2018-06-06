#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 13:05:23 2018

@author: wei
"""

import time
import RPi.GPIO as GPIO
from Non_block_input import waitkey

left_pin = 15
left_pin1 = 35
left_pin2 = 36
right_pin = 13
right_pin1 = 38
right_pin2 = 37
S0 = 55
speed = S0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(left_pin, GPIO.OUT)
GPIO.setup(left_pin1, GPIO.OUT)
GPIO.setup(left_pin2, GPIO.OUT)
GPIO.setup(right_pin, GPIO.OUT)
GPIO.setup(right_pin1, GPIO.OUT)
GPIO.setup(right_pin2, GPIO.OUT)

pwm_L = GPIO.PWM(left_pin, 500)
pwm_R = GPIO.PWM(right_pin, 500)
pwm_L.start(0)
pwm_R.start(0)


def W():
    GPIO.output(left_pin1, True)
    GPIO.output(left_pin2, False)
    GPIO.output(right_pin1, True)
    GPIO.output(right_pin2, False)

def S():
    GPIO.output(left_pin1, False)
    GPIO.output(left_pin2, True)
    GPIO.output(right_pin1, False)
    GPIO.output(right_pin2, True)

def A():
    GPIO.output(left_pin1, True)
    GPIO.output(left_pin2, False)
    GPIO.output(right_pin1, False)
    GPIO.output(right_pin2, True)

def D():
    GPIO.output(left_pin1, False)
    GPIO.output(left_pin2, True)
    GPIO.output(right_pin1, True)
    GPIO.output(right_pin2, False)
    
def stop():
    GPIO.output(left_pin1, False)
    GPIO.output(left_pin2, False)
    GPIO.output(right_pin1, False)
    GPIO.output(right_pin2, False)

try:
    while True:
        key = ord(waitkey())
        print(key)
        if key == 27:
            break
        if key == 32:
            stop()
        if key == 119:
            W()
        if key == 115:
            S()
        if key == 97:
            A()
        if key == 100:
            D()
        if key == 43:
            if speed < 95:
                speed = speed +10
                print("Now speed is",speed) 
            else:
                print("Now speed is",speed)
        if key == 45:
            if speed > 15:
                speed = speed -10
                print("Now speed is",speed) 
            else:
                print("Now speed is",speed)
        pwm_L.ChangeDutyCycle(speed)
        pwm_R.ChangeDutyCycle(speed)

finally:
    stop()
    pwm_L.stop()
    pwm_R.stop()
    GPIO.cleanup()
