#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 00:00:33 2018

@author: wei
"""

import cv2
import matplotlib.pyplot as plt
from threading import Timer
        

def print_picture(name, image):
    cv2.imshow('picture_{}'.format(name), image)

def save_picture(name, image):
    cv2.imwrite('good_{}.png'.format(name), image)

def saveandshow_pic(name):
    global ret
    global image
    print(ret)
    if ret:
        cv2.imwrite('pic_{}.png'.format(name), image)
    else:
        print('camara{} not yet open'.format(name))

def saveandshow_pic2(name, image):
    if ret[0]:
        cv2.imwrite('./share/pic_{}.png'.format(name[0]), image[0])
    if ret[1]:
        cv2.imwrite('./share/pic_{}.png'.format(name[1]), image[1])
    if ret[2]:
        cv2.imwrite('./share/pic_{}.png'.format(name[2]), image[2])
    else:
        print('camara{} not yet open'.format(name))

def timer(func, second=2, *arg):
    func(*arg)
    t = Timer(second, timer, args=(func, 2, *arg))
    t.setDaemon(True)
    if t.daemon:
        t.start()
    else:
        global ret
        global img
        global name
        del ret, img, name
        return 0
        
class Camera(cv2.VideoCapture):
    def __init__(self, camera_number):
        self.camera_number = camera_number
        super(Camera, self).__init__(self.camera_number)
    
    def preview(self):
        while True:
            ret, img = self.read()
            cv2.imshow('preview', img)
            self.key = cv2.waitKey(10)
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


if __name__=='__main__':
    import cv2

    cam = [cv2.VideoCapture(i) for i in range(1, 4)]
    cam_num = 3
    ret = [0 for i in range(cam_num)]
    img = [0 for i in range(cam_num)]
    name = [i for i in range(cam_num)]
    timer(saveandshow_pic2, 3, name, img)
    while True:
        for i in range(cam_num):    
            ret[i], img[i] = cam[i].read()
            cv2.namedWindow(str(i), cv2.WINDOW_NORMAL)
            cv2.imshow(str(i), img[i])
        if cv2.waitKey(5) == 27:
            break
        if cv2.waitKey(5) == 115:
            for i in range(2):
                save_picture(i, img[i])
    for i in range(cam_num):
        cam[i].release()
    cv2.destroyAllWindows()
    
# BUG, 守護現成殺不掉 變數沒有清除
# 雞巴！

