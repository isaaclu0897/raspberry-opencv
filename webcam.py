#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 00:00:33 2018

@author: wei
"""

import cv2
import matplotlib.pyplot as plt
#import numpy as np
from threading import Timer
import time
        
def print_picture(name, image):
    cv2.imshow('picture_{}'.format(name), image)
def save_picture(name, image):
    cv2.imwrite('pic_{}.png'.format(name), image)
def saveandshow_pic(name, image=None):
    if image is None:
        print('camara not yet open')
    else:
        cv2.imshow('picture_{}'.format(name), image)
        cv2.imwrite('pic_{}.png'.format(name), image)


class Camera(cv2.VideoCapture):
    def __init__(self, camera_number):
        self.camera_number = camera_number
        super(Camera, self).__init__(self.camera_number)
    
    def preview(self):
        while True:
            ret, img = self.read()
#            img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imshow('preview', img)
#            cv2.imshow('gray', img1)
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

def timer(func, second=3, *arg):
#    print(func, second, *arg)
    func(*arg)
    Timer(second, timer, args=(func, 3, *arg)).start()

    
if __name__=='__main__':
    import cv2

#    cam = [cv2.VideoCapture(i) for i in range(2)]
##    cam1 = cv2.VideoCapture(0)
##    cam2 = cv2.VideoCapture(1)
#    ret = [i for i in range(2)]
#    img = [i for i in range(2)]
#    timer(save&show_pic, name='', image='')
#    while True:
#        for i in range(2):    
#            ret[i], img[i] = cam[i].read()
#            cv2.imshow(str(i), img[i])
#        print(cv2.waitKey(5))
#        if cv2.waitKey(5) == 27:
#            break
#        if cv2.waitKey(5) == 115:
#            for i in range(2):
#                print_picture(str(i), img[i])
#                save_picture(i, img[i])
#    for i in range(2):
#        cam[i].release()
#    cv2.destroyAllWindows()
    
    cam = cv2.VideoCapture(0)
    global img
    img = None
    timer(saveandshow_pic, 3, '1', img)
    while True:
        ret, img = cam.read()
        cv2.imshow('1', img)
        if cv2.waitKey(5) == 27:
            break
        if cv2.waitKey(5) == 115:
            print_picture('1', img)
            save_picture('1', img)

    cam.release()
    cv2.destroyAllWindows()

#%% add timer for take a picture
from threading import Timer
import time
def hello(name, idnum):
    print('Hello {}! My id is {}'.format(name, idnum))


def timer(func, second=3, *arg):
    print(func, second, arg, *arg)
    func(*arg)
    Timer(second, timer, args=(func, 3, *arg)).start()

if __name__=='__main__':
    timer(hello, 2, 'a', 22)
#    for i in range(10):
#        time.sleep(1)
#        print(i)
    
#%%
from threading import Timer
import time

def hello():
    global a
    if a is 1:
        print('a still is 1')
    else:
        print('good, now a is {}'.format(a))

def timer(func, *arg):
    func(*arg)
    t = Timer(1, timer, args=(hello, *arg))
    t.setDaemon(True)
    if t.daemon:
        t.start()
    else:
        return 0
    
    
if __name__=='__main__':
#    start = time.time()
#    timer(hello)
     a = 1
     timer(hello)
     for i in range(6):
         time.sleep(0.5)
         a = i

