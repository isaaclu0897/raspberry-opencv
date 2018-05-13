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
img1 = cv2.imread('./testtt/7938976811261.jpg')
img2 = cv2.imread('./testtt/7938976997433.jpg')
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Create features of detector(SIFT) 
sift = cv2.xfeatures2d.SIFT_create() # you can choose SIFT or SURF


# Create flann matcher
matcher = cv2.FlannBasedMatcher(dict(algorithm = 1, trees = 5), {})

# Detect keypoints and compute keypointer descriptors
kpts1, descs1 = sift.detectAndCompute(gray1,None)
kpts2, descs2 = sift.detectAndCompute(gray2,None)

# knnMatch to get Top2
matches = matcher.knnMatch(descs1, descs2, 2)

# $ Sort by their distance.
matches = sorted(matches, key = lambda x:x[0].distance)

# to get good matches.
good = [m1 for (m1, m2) in matches if m1.distance < 0.7 * m2.distance]

canvas = img2.copy()

# find homography matrix
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

cv2.namedWindow('kkk', cv2.WINDOW_NORMAL)
cv2.imshow('kkk', canvas)
# drawMatches
#draw_params = dict(matchColor = (0,255,0),
#    singlePointColor = (255,0,0),
##    matchesMask =1 matchesMask,
#    flags = 0)
#matched = cv2.drawMatches(img1,kpts1,img2,kpts2,good,None)#,**draw_params)

# Crop the matched region from scene
#h,w = img1.shape[:2]
#pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
#dst = cv2.perspectiveTransform(pts,M)
#perspectiveM = cv2.getPerspectiveTransform(np.float32(dst),pts)
#found = cv2.warpPerspective(img2,perspectiveM,(w,h))


## (10) save and display
#cv2.imwrite("matched.png", matched)
#cv2.imwrite("found.png", found)
#cv2.imshow("matched", matched);
#cv2.imshow("found", found);
#cv2.waitKey();cv2.destroyAllWindows()
