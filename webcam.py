#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 00:00:33 2018

@author: wei
"""

import cv2
#import numpy as np

cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
#    print(img)
    cv2.imshow('good', img)
    k = cv2.waitKey(10) # & 0xff
    ''' waitKey([, delay]) -> retval
    delay：等待時間，
    當delay<=0時,程式靜止
    當delay>0時,函式會等待參數時間(ms)後,返回按鍵的ASCII碼,
    如果這段時間沒有按鍵按下,會返回-1。
    '''
    print(k)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
#while True:
    