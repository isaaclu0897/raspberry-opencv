#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 00:00:33 2018

@author: wei
"""

import cv2
#import matplotlib.pyplot as plt
#import numpy as np


class Capture(object):
    def __init__(self, cap_num):
        self.cap_num = cap_num
        self._cap = cv2.VideoCapture(self.cap_num)
    
    def preview(self):
        while True:
            ret, image = self._cap.read()
            cv2.imshow('preview', image)
            self.key = cv2.waitKey(10) # & 0xff
#            print(self.k)
            ''' waitKey([, delay]) -> retval
            delay：等待時間，
            當delay<=0時,程式靜止
            當delay>0時,函式會等待參數時間(ms)後,返回按鍵的ASCII碼,
            如果這段時間沒有按鍵按下,會返回-1。
            '''
            if self.key != -1:
                if self.key==27 or self.key==113:
                    break
                elif self.key == 97:
                    print_picture(image)
                    save_picture(image)
                if self.key == 112:
                    print_picture(image)
                if self.key == 115:
                    save_picture(image)

        self._cap.release()
        cv2.destroyAllWindows()
        
def print_picture(image):
    cv2.imshow('picture', image)
def save_picture(image):
    cv2.imwrite('test.png', image)
        
#    def take_pic(self):
#        while True:
#            ret, img = self._cap.read()
#            else:
#                ret = False
#        cv2.imshow('good', img)
#        self._cap.release()
    
if __name__=='__main__':
    cam = Capture(0)
    cam.preview()

    
#    get_vision(0)#, get_vision(1)
#    take_pic(0)
    










