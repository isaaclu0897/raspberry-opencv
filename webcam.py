#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 00:00:33 2018

@author: wei
"""

import cv2
import matplotlib.pyplot as plt
#import numpy as np

def get_vision(num):
    cap = cv2.VideoCapture(num)
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
#        print(k)
        if k == 27:
            break
    
    cap.release()
    cv2.destroyAllWindows()

def take_pic(num):
    cap = cv2.VideoCapture(num)
    if cap.isOpened():
        ret, img = cap.read()
        print(img)
        print(ret)
        
    else:
        ret = False
#    cv2.imshow('good', img)
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.imshow(img1)
    plt.title('color image')
    
    cap.release()
    
if __name__=='__main__':
#    get_vision(0)#, get_vision(1)
    take_pic(1)
#while True:
#    
#[https://www.google.com.tw/search?ei=EfbhWqXXAYPM8wWwo7HYDA&q=python+webcam+capture&oq=python+webcam+&gs_l=psy-ab.1.1.0i67k1j0l9.898.898.0.2582.1.1.0.0.0.0.79.79.1.1.0....0...1c.1.64.psy-ab..0.1.77....0.ojqEwGnEej4]
#[https://www.youtube.com/watch?v=v7Z2WAj33Hs]
#[https://www.google.com.tw/search?ei=effhWs-hOImk8QXpjZOIBw&q=OpenCV+Webcam+python&oq=OpenCV+Webcam+python&gs_l=psy-ab.3..0j0i8i30k1l9.4528.6040.0.6328.7.7.0.0.0.0.132.585.4j3.7.0....0...1c.1.64.psy-ab..0.7.584...0i67k1j0i30k1.0.X3XaluxnA2c]
#[https://www.youtube.com/watch?v=bt-0GEeUgBY]
#[https://www.google.com.tw/search?q=cv2.waitKey(10)%26+0xff&oq=cv2.waitKey(10)%26+0xff&aqs=chrome..69i57.553j0j7&sourceid=chrome&ie=UTF-8]
#[https://stackoverflow.com/questions/35372700/whats-0xff-for-in-cv2-waitkey1]
#[https://blog.csdn.net/Addmana/article/details/54604298]
#[https://www.jianshu.com/p/30c40d7ce5dc]
#[https://www.google.com.tw/search?q=bash+webcam&oq=bash+webcam&aqs=chrome..69i57j0.7656j0j7&sourceid=chrome&ie=UTF-8]
#[https://askubuntu.com/questions/106770/take-a-picture-from-terminal]
#[https://www.google.com.tw/search?ei=L_3hWrr1AYj28QWv97T4BQ&q=streamer+ubuntu&oq=streamer+ubuntu&gs_l=psy-ab.3..0j0i30k1l2j0i5i30k1l7.553.1989.0.2394.7.7.0.0.0.0.129.537.5j2.7.0....0...1c.1j4.64.psy-ab..0.7.534...0i10k1j0i10i30k1.0.vnANr5cPNwc]
#[https://www.youtube.com/watch?v=kY6audSZ0Xo]
#[https://www.google.com.tw/search?ei=n_3hWtfbI4T98QXn1omgDA&q=%E4%B8%B2%E6%B5%81+%E5%A5%BD%E8%99%95&oq=%E4%B8%B2%E6%B5%81+%E5%A5%BD%E8%99%95&gs_l=psy-ab.3..0i30k1.29260.30411.0.30683.7.7.0.0.0.0.64.318.6.6.0....0...1c.1j4.64.psy-ab..1.2.108...0.0.1SLcKN15STw]
#[http://blog.xuite.net/johnny_0214/mood/5342155-%E4%B8%B2%E6%B5%81%E5%AA%92%E9%AB%94%28streaming%29]
#[https://www.google.com.tw/search?q=cv2.waitKey(10)+%26+0xff&oq=cv2.waitKey(10)+%26+0xff&aqs=chrome..69i57.387j0j7&sourceid=chrome&ie=UTF-8]
#[https://www.google.com.tw/search?q=cv2+waitkey+10+27&sa=X&ved=0ahUKEwjb47K_sdjaAhXBUrwKHUQOD7IQ1QIIiAEoAA]
#[https://stackoverflow.com/questions/14494101/using-other-keys-for-the-waitkey-function-of-opencv]
#[http://monkeycoding.com/?tag=opencv%E5%BD%B1%E5%83%8F%E8%AE%80%E5%8F%96%E5%84%B2%E5%AD%98]
#目前已經可以成功將影片出來了
#waitkey稍唯有一點點點點了解 要在確認
#下次要拍照
#然後要看能不能分好幾個相機









