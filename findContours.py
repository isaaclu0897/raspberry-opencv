#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 22:32:55 2018

@author: wei
"""

import cv2
from matplotlib import pyplot as plt
import numpy as np


im = cv2.imread('7934900393276.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
GaussianBlur = cv2.GaussianBlur(imgray, (3, 3), 0)
ret,thresh = cv2.threshold(GaussianBlur,75,255,0)
binary,contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#    hull = [cv2.convexHull(contours[i]) for i in range(len(contours))]
cv2.drawContours(im,contours,-1,(255, 0, 0), 2)
plt.hist(GaussianBlur.ravel(),256,[0,256])
cv2.namedWindow('thresh2', cv2.WINDOW_NORMAL)
cv2.imshow('thresh2', thresh)


#im = cv2.imread('test.jpg')
##plt.hist(im.ravel(),256,[0,256]) # 利用直方圖可檢視圖片的明度藉此找到閾值
#
## 由於opencv只能處裡灰度圖，所以要先用convert成灰階
#imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
#ret,thresh = cv2.threshold(imgray,200,255,0) # 經測試200為合適閾值
##plt.hist(imgray.ravel(),256,[0,256])
#GaussianBlur = cv2.GaussianBlur(thresh, (9, 9), 0)
#binary,contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#hull = [cv2.convexHull(contours[i]) for i in range(len(contours))]
#"""
#cv2.CHAIN_APPROX_NONE,所有的邊界點都會被存儲
#cv2.CHAIN_APPROX_SIMPLE,只存取重要特徵點
#"""
#cv2.drawContours(im,hull,-1,(255, 0, 0), 2)
#"""
#我們可以利用 type和 shape來查看圖片的型態和大小
#print(type(im), im.shape)
#這裡輸出的結果為    # <class 'numpy.ndarray'>, (3200, 2400, 3)
#實在是太大了，因此我們可以利用WINDOW_NORMAL控制圖片縮放
#"""
#
#cv2.namedWindow('im', cv2.WINDOW_NORMAL)
#cv2.imshow('im', im)
#cv2.namedWindow('thresh', cv2.WINDOW_NORMAL)
#cv2.imshow('thresh', thresh)

# 也許需要利用凸包
#http://arbu00.blogspot.tw/2016/12/opencv11-contours-and-convex-hull.html
#http://ex2tron.top/2017/12/20/Python-OpenCV%E6%95%99%E7%A8%8B%E7%95%AA%E5%A4%96%E7%AF%8710%EF%BC%9A%E5%87%B8%E5%8C%85%E5%8F%8A%E6%9B%B4%E5%A4%9A%E8%BD%AE%E5%BB%93%E7%89%B9%E5%BE%81/
#https://github.com/makelove/OpenCV-Python-Tutorial/blob/master/ch21-%E8%BD%AE%E5%BB%93Contours/%E5%87%B8%E5%8C%85-%E5%87%B8%E6%80%A7%E6%A3%80%E6%B5%8B-%E8%BE%B9%E7%95%8C%E7%9F%A9%E5%BD%A2-%E6%9C%80%E5%B0%8F%E5%A4%96%E6%8E%A5%E5%9C%86-%E6%8B%9F%E5%90%88.py
#http://www.th7.cn/Program/Python/201708/1218178.shtml
#https://zhuanlan.zhihu.com/p/33301371
""" 凸包
函數 cv2.convexHull() 可以用來檢測一個曲線是否具有凸性缺陷，並能糾正缺陷
如果有地方凹進去了就叫做"凸性缺陷"。
convexHull(points[, hull[, clockwise[, returnPoints]]]) -> hull
@param points Input 2D point set, stored in std::vector or Mat.
要傳入點集和，所以我們可以把contours集合用列表生成hull

函數 cv2.isContourConvex(hull) 可檢測輪廓是否為凸性
"""

# 今天成功使用凸包，但是包覆的效果仍不理想，我想我們只是檢測邊緣能不能把再包腹內的輪廓刪掉 還有也許可以使用 各種圖形近似來趨近