# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 20:26:21 2020

@author: shangyonggang
"""

import cv2
import numpy as np

if __name__ == "__main__":
    #image read
    if 0:
        img_path = "./zhaoliying_r2.jpg"

        img_color = cv2.imread(img_path, cv2.IMREAD_COLOR)
        img_gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

        print("img_color.shape = ", img_color.shape)
        print("img_gray.shape = ", img_gray.shape)

        cv2.imshow("img_color", img_color)
        cv2.imshow("img_gray", img_gray)

        cv2.waitKey(0)
        
    #color space
    if 0:
        img_path = "./fengjing_r.jpg"
        
        img_color = cv2.imread(img_path, cv2.IMREAD_COLOR)
        
        img_rgb = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)
        img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
        img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV)
        
        cv2.imshow("img_color", img_color)
        cv2.imshow("img_rgb", img_rgb)
        cv2.imshow("img_gray", img_gray)
        cv2.imshow("img_hsv", img_hsv)
        
        cv2.waitKey(0)
        
        
    #image roi
    if 0:
        img_path_1 = "./huge_r2.jpg"
        img_path_2 = "./zhaoliying_r2.jpg"
        
        img_1 = cv2.imread(img_path_1, cv2.IMREAD_COLOR)
        img_2 = cv2.imread(img_path_2, cv2.IMREAD_COLOR)
        
        img_1_roi = img_1[: , :int(img_1.shape[1]/2)]
        img_2_roi = img_2[: , int(img_2.shape[1]/2):]
           
        cv2.imshow("img_1_roi", img_1_roi)
        cv2.imshow("img_2_roi", img_2_roi)

        cv2.waitKey(0)
        
    #image resize
    if 0:
        img_path_1 = "./huge_r2.jpg"
        
        img_1 = cv2.imread(img_path_1, cv2.IMREAD_COLOR)
        img_1_resize1 = cv2.resize(img_1, (int(img_1.shape[1]*3/4), int(img_1.shape[0]*3/4)))
        img_1_resize2 = cv2.resize(img_1, (int(img_1.shape[1]/2), int(img_1.shape[0]/2)))
        
        cv2.imshow("img_1", img_1)
        cv2.imshow("img_1_resize1", img_1_resize1)
        cv2.imshow("img_1_resize2", img_1_resize2)
        
        cv2.waitKey(0)
        
    #split and merge
    if 0:
        img_path = "./fengjing_r.jpg"
        
        img_color = cv2.imread(img_path, cv2.IMREAD_COLOR)
        
        B,G,R = cv2.split(img_color)  
        img_merge = cv2.merge((B,G,R))
                
        cv2.imshow("B", B)
        cv2.imshow("G", G)
        cv2.imshow("R", R)
        cv2.imshow("img_merge", img_merge)
        
        cv2.waitKey(0)
        
    #image concat
    if 0:
        img_path_1 = "./zhaoliying_r2.jpg"
        img_path_2 = "./huge_r2.jpg"
        
        img_1 = cv2.imread(img_path_1, cv2.IMREAD_COLOR)
        img_2 = cv2.imread(img_path_2, cv2.IMREAD_COLOR)        
        
        img_1_resize = cv2.resize(img_1, (int(img_1.shape[1]/2), int(img_1.shape[0]/2)))
        img_2_resize = cv2.resize(img_2, (int(img_2.shape[1]/2), int(img_2.shape[0]/2)))
        
        img_concat1 = np.concatenate((img_1_resize, img_2_resize), axis=0)#vertical
        img_concat2 = np.concatenate((img_concat1, img_concat1), axis=1)#horizontal
        img_concat2 = cv2.hconcat((img_concat2, img_concat2))#horizontal
                
        cv2.imshow("concat2", img_concat2)
        
        cv2.waitKey(0)
        
    #图像旋转
    if 1:
        img_path_1 = "./huge_r2.jpg"

        img_1 = cv2.imread(img_path_1, cv2.IMREAD_COLOR)
        
        A1 = cv2.getRotationMatrix2D((int(img_1.shape[1]/2.0), int(img_1.shape[0]/2.0)), 30, 1.0)
        d1 = cv2.warpAffine(img_1, A1, (img_1.shape[1], img_1.shape[0]), borderValue = 125)
        
        A2 = cv2.getRotationMatrix2D((int(img_1.shape[1]/2.0), int(img_1.shape[0]/2.0)), -30, 1.0)
        d2 = cv2.warpAffine(img_1, A2, (img_1.shape[1], img_1.shape[0]), borderValue = 125)
        
        cv2.imshow("30", d1)
        cv2.imshow("-30", d2)
        
        cv2.waitKey(0)
        
    #图片叠加
    if 0:
        img_path_base = "./fengjing.jpg"
        img_path_1 = "./huge_r2.jpg"
        img_path_2 = "./zhaoliying_r2.jpg"
        
        img_base = cv2.imread(img_path_base, cv2.IMREAD_COLOR)
        img_1 = cv2.imread(img_path_1, cv2.IMREAD_COLOR)
        img_2 = cv2.imread(img_path_2, cv2.IMREAD_COLOR)
        
        A1 = cv2.getRotationMatrix2D((int(img_1.shape[1]/2.0), int(img_1.shape[0]/2.0)), 30, 1.0)
        d1 = cv2.warpAffine(img_1, A1, (img_1.shape[1], img_1.shape[0]), borderValue = 125)
        cv2.imshow("a", d1)
        
                
        img_1_resize = cv2.resize(img_1, (int(img_1.shape[1]/2), int(img_1.shape[0]/2)))
        img_2_resize = cv2.resize(img_2, (int(img_2.shape[1]/2), int(img_2.shape[0]/2)))
        
        h_s = img_base.shape[0]-img_1_resize.shape[0]
        h_e = img_base.shape[0]
        w_s = int(img_base.shape[1]/2)-img_1_resize.shape[1]
        w_e = int(img_base.shape[1]/2)
        img_roi1 = img_base[h_s:h_e, w_s:w_e]
        img_roi1 = cv2.addWeighted(img_roi1, 0.3, img_1_resize, 0.8, 0)
        img_base[h_s:h_e, w_s:w_e] = img_roi1[:, :]
        
        h_s = img_base.shape[0]-img_2_resize.shape[0]
        h_e = img_base.shape[0]
        w_s = int(img_base.shape[1]/2)
        w_e = int(img_base.shape[1]/2)+img_1_resize.shape[1]
        img_roi2 = img_base[h_s:h_e, w_s:w_e]
        img_roi2 = cv2.addWeighted(img_roi2, 0.5, img_2_resize, 0.7, 0)
        img_base[h_s:h_e, w_s:w_e] = img_roi2[:, :]
            
        
        cv2.imshow("img_base", img_base)
                    
        cv2.waitKey(0)
        