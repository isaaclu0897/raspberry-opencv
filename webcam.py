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
#import time
        
def print_picture(name, image):
    cv2.imshow('picture_{}'.format(name), image)
def save_picture(name, image):
    cv2.imwrite('good_{}.png'.format(name), image)
def saveandshow_pic(name):
    global ret
    global image
    print(ret)
    if ret:
#        cv2.imshow('picture_{}'.format(name), image)
        cv2.imwrite('pic_{}.png'.format(name), image)
    else:
        print('camara{} not yet open'.format(name))

def saveandshow_pic2(*name):
    global ret
    global image
    print(ret)
    if ret:
#        cv2.imshow('picture_{}'.format(name), image)
        cv2.imwrite('pic_{}.png'.format(name), image)
    else:
        print('camara{} not yet open'.format(name))
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

def timer(func, second=2, *):
#    print(func, second, *arg)
    func(*arg)
    t = Timer(second, timer, args=(func, 2, *arg))
    t.setDaemon(True)
    if t.daemon:
        t.start()
    else:
        return 0

    l
if __name__=='__main__':
    import cv2

    cam = [cv2.VideoCapture(i) for i in range(2)]
#    cam1 = cv2.VideoCapture(0)
#    cam2 = cv2.VideoCapture(1)
    ret = [0 for i in range(2)]
    image = [0 for i in range(2)]
    timer(saveandshow_pic, 3, '1')
#    timer(saveandshow_pic, 3, '2')
    while True:
        for i in range(2):    
            ret[i], img[i] = cam[i].read()
            cv2.imshow(str(i), img[i])
        print(cv2.waitKey(5))
        if cv2.waitKey(5) == 27:
            break
        if cv2.waitKey(5) == 115:
            for i in range(2):
#                print_picture(str(i), img[i])
                save_picture(i, img[i])
    for i in range(2):
        cam[i].release()
    cv2.destroyAllWindows()
    
    
#    cam = cv2.VideoCapture(0)
#    ret = image = 0
#    timer(saveandshow_pic, 3, '1')
#    while True:
#        ret, image = cam.read()
#        cv2.imshow('1', image)
#        if cv2.waitKey(5) == 27:
#            break
##        if cv2.waitKey(5) == 115:
##            print_picture('1', img)
##            save_picture('1', img)
#
#    cam.release()
#    cv2.destroyAllWindows()
#%%
from threading import Timer 
import time 
 
def hello(name, image): 
#    global a 
    if name[0]==0 and name[1]==0: 
        print(name[0], name[1]) 
    else: 
        print('good, now a is {}'.format(name))
        print('a is {} & {}, b is {} & {}'.format(name[0], name[1], image[0], image[1]))
 
def timer(func, *arg):
    print(*arg, arg)
    global k
    print(k)
    func(*arg) 
    t = Timer(5, timer, args=(hello, *arg)) 
    t.setDaemon(True) 
    if t.daemon: 
        t.start() 
    else: 
        return 0 
     
     
if __name__=='__main__': 
#    start = time.time() 
#    timer(hello) 
     k = [0, 0]
     a = [0, 0]
     b = [0, 0]
     timer(hello, a, b) 
     for i in range(6): 
         time.sleep(1)
         k[0] = 11
         k[1] = 222
         a[0]=2
         a[1]=3
         b[0]=5
         b[1]=7


