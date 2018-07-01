#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 13:05:23 2018

@author: wei
"""

import time
import RPi.GPIO as GPIO
from Non_block_input import waitkey
from time import sleep

#left_pin = 15
#left_pin1 = 35
#left_pin2 = 36
#right_pin = 13
#right_pin1 = 38
#right_pin2 = 37

def left_pins():
    left_pin = 13
    left_pin1 = 15
    left_pin2 = 16
    return left_pin, left_pin1, left_pin2

def right_pins():
    right_pin = 13
    right_pin1 = 12
    right_pin2 = 11
    return right_pin, right_pin1, right_pin2


class MOTOR(object):
    def __init__(self, ENABLE_PIN, IN1, IN2, MOTOR_FREQ=500):
        self.enable_pin = ENABLE_PIN
        self.in1_pin = IN1
        self.in2_pin = IN2
        
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.enable_pin, GPIO.OUT)
        GPIO.setup(self.in1_pin, GPIO.OUT)
        GPIO.setup(self.in2_pin, GPIO.OUT)

        self.pwm = GPIO.PWM(self.enable_pin, MOTOR_FREQ)
        self.pwm.start(0)
        self.speed=55

    def start(self):
        GPIO.output(self.in1_pin, False)
        GPIO.output(self.in2_pin, False)
        self.pwm.ChangeDutyCycle(self.speed)

    def forword(self):
        GPIO.output(self.in1_pin, True)
        GPIO.output(self.in2_pin, False)

    def back(self):
        GPIO.output(self.in1_pin, False)
        GPIO.output(self.in2_pin, True)

    def add_speed(self, level=10):
        if self.speed < 95:
            self.speed += level
        else:
            pass
        self.pwm.ChangeDutyCycle(self.speed)
        print('now speed is {}'.format(self.speed))

    def minus_speed(self, level=10):
        if self.speed > 25:
            self.speed -= level
        else:
            pass
        self.pwm.ChangeDutyCycle(self.speed)
        print('now speed is {}'.format(self.speed))
        
    def stop(self):
##        self.pwm.stop()
        GPIO.output(self.in1_pin, False)
        GPIO.output(self.in2_pin, False)

        
class CAR(object):
    def __init__(self, left_wheel, right_wheel):
        self.left_wheel = left_wheel
        self.right_wheel = right_wheel

    def forword(self):
        self.left_wheel.forword()
        self.right_wheel.forword()
        
    def back(self):
        self.left_wheel.back()
        self.right_wheel.back()
        
    def right(self):
        self.left_wheel.forword()
        self.right_wheel.back()
        
    def left(self):
        self.left_wheel.back()
        self.right_wheel.forword()
        
    def add_speed(self):
        self.left_wheel.add_speed()
        self.right_wheel.add_speed()
        
    def minus_speed(self):
        self.left_wheel.minus_speed()
        self.right_wheel.minus_speed()
        
        
    def stop(self):
        self.left_wheel.stop()
        self.right_wheel.stop()


if __name__=='__main__':
    left_motor = MOTOR(*left_pins())
    right_motor = MOTOR(*right_pins())
    
    car = CAR(right_motor, left_motor)
    try:
        left_motor.start()
        while True:
            key = ord(waitkey())
            print(key)
            if key == 27:
                break
            if key == 32:
                car.stop()
            if key == 119:
                car.forword()
            if key == 115:
                car.back()
            if key == 97:
                car.right()
            if key == 100:
                car.left()
            if key == 43:
                car.add_speed()
            if key == 45:
                car.minus_speed()
        
    finally:
        car.stop()
        GPIO.cleanup()


