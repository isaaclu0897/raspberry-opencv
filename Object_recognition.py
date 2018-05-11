#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 20:46:21 2018

@author: wei
"""

import cv2
import numpy as np
MIN_MATCH_COUNT = 4


# load data
img1 = cv2.imread('./test_recognition/1371867.jpg')
img2 = cv2.imread('./test_recognition/1371866.jpg')
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Create features of detector(SIFT) 
sift = cv2.xfeatures2d.SIFT_create() # you can choose SIFT or SURF

#(kps, descs) = sift.detectAndCompute(gray1, None)
#print("# kps: {}, descriptors: {}".format(len(kps), descs.shape))
## kps: 274, descriptors: (274, 128)
#surf = cv2.xfeatures2d.SURF_create()
#(kps, descs) = surf.detectAndCompute(gray1, None)
#print("# kps: {}, descriptors: {}".format(len(kps), descs.shape))
## kps: 393, descriptors: (393, 64)

## (3) Create flann matcher
matcher = cv2.FlannBasedMatcher(dict(algorithm = 1, trees = 5), {})

## (4) Detect keypoints and compute keypointer descriptors
kpts1, descs1 = sift.detectAndCompute(gray1,None)
kpts2, descs2 = sift.detectAndCompute(gray2,None)

## (5) knnMatch to get Top2
matches = matcher.knnMatch(descs1, descs2, 2)
# Sort by their distance.
matches = sorted(matches, key = lambda x:x[0].distance)

## (6) Ratio test, to get good matches.
good = [m1 for (m1, m2) in matches if m1.distance < 0.7 * m2.distance]

canvas = img2.copy()

## (7) find homography matrix
## 当有足够的健壮匹配点对（至少4个）时
if len(good)>MIN_MATCH_COUNT:
    ## 从匹配中提取出对应点对
    ## (queryIndex for the small object, trainIndex for the scene )
    src_pts = np.float32([ kpts1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
    dst_pts = np.float32([ kpts2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)
    ## find homography matrix in cv2.RANSAC using good match points
    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
    ## 掩模，用作绘制计算单应性矩阵时用到的点对
    #matchesMask2 = mask.ravel().tolist()
    ## 计算图1的畸变，也就是在图2中的对应的位置。
    h,w = img1.shape[:2]
    pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
    dst = cv2.perspectiveTransform(pts,M)
    ## 绘制边框
    cv2.polylines(canvas,[np.int32(dst)],True,(0,255,0),3, cv2.LINE_AA)
else:
    print( "Not enough matches are found - {}/{}".format(len(good),MIN_MATCH_COUNT))


## (8) drawMatches
matched = cv2.drawMatches(img1,kpts1,canvas,kpts2,good,None)#,**draw_params)

## (9) Crop the matched region from scene
h,w = img1.shape[:2]
pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
dst = cv2.perspectiveTransform(pts,M)
perspectiveM = cv2.getPerspectiveTransform(np.float32(dst),pts)
found = cv2.warpPerspective(img2,perspectiveM,(w,h))

## (10) save and display
cv2.imwrite("matched.png", matched)
cv2.imwrite("found.png", found)
cv2.imshow("matched", matched);
cv2.imshow("found", found);
cv2.waitKey();cv2.destroyAllWindows()

#%%
import cv2
import numpy as np

def SIFT(img):
    I = cv2.imread(img)
    gray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
    descriptor = cv2.xfeatures2d.SIFT_create()
    kps, features = descriptor.detectAndCompute(gray, None)
    nkps = []
    for i in kps:
        if i.size > 100:
            nkps.append(i)
    cv2.drawKeypoints(I,nkps,I,(0,255,255),flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow('Vikings Detected!!', I)
    cv2.imwrite('sift_keypoints.jpg',I)
    cv2.waitKey(0)

if __name__ == '__main__':
    img = './test_recognition/1371867.jpg'
    SIFT(img)
    
# https://blog.csdn.net/yzxnuaa/article/details/79221174