#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 00:00:33 2018

@author: wei
"""

import cv2
import matplotlib.pyplot as plt
#import numpy as np
        
def print_picture(image):
    cv2.imshow('picture', image)
def save_picture(image):
    cv2.imwrite('test.png', image)

class Camera(cv2.VideoCapture):
    def __init__(self, camera_number):
        self.camera_number = camera_number
        super(Camera, self).__init__(self.camera_number)
    
    def preview(self):
        while True:
            ret, img = self.read()
            img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imshow('preview', img)
            cv2.imshow('gray', img1)
            self.key = cv2.waitKey(10) # & 0xff
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
                    print_picture(img)
                    save_picture(img)
                if self.key == 112:
                    print_picture(img)
                if self.key == 115:
                    save_picture(img)
        self.release()
        cv2.destroyAllWindows()
    def preview_matplotlib(self):

        count = 0
        """
        because setting time of the camara too slow,
        if use the other camara just type "if self.isOpened():"
        """
        while count <= 10:
            count += 1
            ret, img = self.read()
        #    print(ret, img)
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            plt.imshow(img)
            plt.show()
        self.release()
    def take_picture(self, use_matplotlib=False):
        count = 0
        """
        because setting time of the camara too slow,
        if use the other camara just type "if self.isOpened():"
        """
        if use_matplotlib:
            while count <= 10:
                count += 1
                ret, img = self.read()
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            plt.imshow(img)
            plt.show()
        else:
            while count <= 10:
                count += 1
                ret, img = self.read()
            cv2.imshow('picture', img)
        self.release()
#        cv2.destroyAllWindows()  
        
#    def take_pic(self):
#        while True:
#            ret, img = self._cap.read()
#            else:
#                ret = False
#        cv2.imshow('good', img)
#        self._cap.release()
    
if __name__=='__main__':
    cam = Camera(1)
    cam.take_picture(True)

    
#    get_vision(0)#, get_vision(1)
#    take_pic(0)
    










