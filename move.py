#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 13:05:23 2018

@author: wei
"""

import time
import RPi.GPIO as GPIO

enable_pin = 13
in1_pin1 = 11
in1_pin2 = 12
in2_pin1 = 15
in2_pin2 = 16
S0 = 50
speed = S0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(in1_pin1, GPIO.OUT)
GPIO.setup(in1_pin2, GPIO.OUT)
GPIO.setup(in2_pin1, GPIO.OUT)
GPIO.setup(in2_pin2, GPIO.OUT)

pwm = GPIO.PWM(enable_pin, 500)
pwm.start(0)

def W():
    GPIO.output(in1_pin1, True)
    GPIO.output(in1_pin2, False)
    GPIO.output(in2_pin1, True)
    GPIO.output(in2_pin2, False)

def S():
    GPIO.output(in1_pin1, False)
    GPIO.output(in1_pin2, True)
    GPIO.output(in2_pin1, False)
    GPIO.output(in2_pin2, True)

def A():
    GPIO.output(in1_pin1, True)
    GPIO.output(in1_pin2, False)
    GPIO.output(in2_pin1, False)
    GPIO.output(in2_pin2, True)

def D():
    GPIO.output(in1_pin1, False)
    GPIO.output(in1_pin2, True)
    GPIO.output(in2_pin1, True)
    GPIO.output(in2_pin2, False)

try:

    while True:

        cmd = raw_input("W S A D Q + -")
        direction = cmd[0]
        if direction == "q":
            break
        if direction == "w":
            W()
        if direction == "s":
            S()
        if direction == "a":
            A()
        if direction == "d":
            D()
        if direction == "+":
            if speed < 100:
                speed = speed +10
                print("Now speed is",speed) 
            else:
                print("Now speed is",speed)
        if direction == "-":
            if speed > 20:
                speed = speed -10
                print("Now speed is",speed) 
            else:
                print("Now speed is",speed)
        pwm.ChangeDutyCycle(speed)

finally:
    pwm.stop()
    GPIO.cleanup()
