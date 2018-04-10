#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 22:32:55 2018

@author: wei
"""

import cv2
#from matplotlib import pyplot as plt

im = cv2.imread('test.jpg')
#plt.hist(im.ravel(),256,[0,256]) # 利用直方圖可檢視圖片的明度藉此找到閾值

# 由於opencv只能處裡灰度圖，所以要先用convert成灰階
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,200,255,0) # 經測試200為合適閾值
GaussianBlur = cv2.GaussianBlur(thresh, (3, 3), 0)
binary,contours,hierarchy = cv2.findContours(GaussianBlur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(im,contours,-1,(255, 0, 0), 2)
"""
我們可以利用 type和 shape來查看圖片的型態和大小
print(type(im), im.shape)
這裡輸出的結果為    # <class 'numpy.ndarray'>, (3200, 2400, 3)
實在是太大了，因此我們可以利用WINDOW_NORMAL控制圖片縮放
"""

cv2.namedWindow('im', cv2.WINDOW_NORMAL)
cv2.imshow('im', im)

# 也許需要利用凸包 http://arbu00.blogspot.tw/2016/12/opencv11-contours-and-convex-hull.html
