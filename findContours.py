#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 22:32:55 2018

@author: wei
"""

import cv2

im = cv2.imread('test.jpg')

"""
我們可以利用 type和 shape來查看圖片的型態和大小
print(type(im), im.shape)
這裡輸出的結果為    # <class 'numpy.ndarray'>, (3200, 2400, 3)
實在是太大了，因此我們可以利用WINDOW_NORMAL控制圖片縮放
"""
#im = im.resizeWindow('image', 600,600)



## 由於opencv只能處裡灰度圖，所以要先用convert成灰階
#imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
#binary,contours,hierarchy = cv2.findContours(imgray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(im,contours,-1,(255, 0, 0), 2)
cv2.namedWindow('im', cv2.WINDOW_NORMAL)
cv2.imshow('im', im)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#cv2.namedWindow('image', cv2.WINDOW_NORMAL)
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()