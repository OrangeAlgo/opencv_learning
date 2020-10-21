# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 13:55:46 2020

@author: shangyonggang
"""

import cv2
import time
import numpy as np

if __name__ == "__main__":
    #像素处理
    if 0:
        img_path = "./zhaoliying_r2.jpg"

        img_color = cv2.imread(img_path, cv2.IMREAD_COLOR)                 
        
        img_color = cv2.resize(img_color, (2000, 3000))
        

        height, width, changel = img_color.shape
        print("height, width, changel = ", height, width, changel)
        
        time_1 = time.time()
        #numpy形式
        for h in range(height):
            for w in range(width):
                a = img_color[h,w,0]
                b = img_color[h,w,1]
                c = img_color[h,w,2]                
                
                img_color[h,w] = (100,100,100)
        time_2 = time.time()
        print("diff time = ", time_2 - time_1)
        
        time_1 = time.time()
        #item形式
        for h in range(height):
            for w in range(width):
                a = img_color.item(h,w,0)
                b = img_color.item(h,w,1)
                c = img_color.item(h,w,2)
                
                img_color.itemset((h,w,0), 100)
                img_color.itemset((h,w,1), 100)
                img_color.itemset((h,w,2), 100)
        time_2 = time.time()
        print("diff time = ", time_2 - time_1)
    
    #图像分离    
    if 0:
        img_path = "./zhaoliying_r2.jpg"

        img_color = cv2.imread(img_path, cv2.IMREAD_COLOR)                 
        
        img_color = cv2.resize(img_color, (2000, 3000))
        
        time_1 = time.time()
        #split方式
        b,g,r = cv2.split(img_color)
        time_2 = time.time()
        print("111 = ", time_2 - time_1)
        
        
        time_1 = time.time()
        #numpy方式
        b = img_color[:,:,0]
        g = img_color[:,:,1]
        r = img_color[:,:,2]        
        time_2 = time.time()
        print("111 = ", time_2 - time_1)
      
    
    #边界填充
    if 0:
        img_path = "./huge_r2.jpg"
        img_color = cv2.imread(img_path, cv2.IMREAD_COLOR)
        img_pad = cv2.copyMakeBorder(img_color,10,10,10,10,cv2.BORDER_CONSTANT,value=[0,0,0])
        
        cv2.imshow("src", img_color)
        cv2.imshow("pad", img_pad)
        
        cv2.waitKey(0)
        
    #数学运算
    if 0:
        img1 = cv2.imread("./fengjing.jpg", cv2.IMREAD_COLOR)        
        img2 = cv2.imread("./opencv_log.png", cv2.IMREAD_COLOR)
        
        img2 = cv2.resize(img2, (int(img2.shape[1]*0.4), int(img2.shape[0]*0.4)))
        
        #提取log掩膜
        img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)
        
        #mask是对dst又进行的掩膜操作
        #提取图片前景，其它部分黑色
        rows,cols,channels = img2.shape
        roi = img1[0:rows, 0:cols]
        img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
        
        cv2.imshow("roi", roi)
        img2_t = cv2.bitwise_and(roi, img2)
        cv2.imshow("img2_t", img2_t)
        
        #提取log前景，其它部分黑色
        img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
        
        #叠加
        dst = cv2.add(img1_bg,img2_fg)
        img1[0:rows, 0:cols ] = dst
        
        cv2.imshow("img2", img2)
        cv2.imshow("mask", mask)
        cv2.imshow("mask_inv", mask_inv)
        cv2.imshow("img1_bg", img1_bg)
        cv2.imshow("img2_fg", img2_fg)
        
        cv2.imshow("img1", img1)
        
        
        cv2.waitKey(0)
        
    #性能优化
    if 1:
        if cv2.useOptimized() == False:
            cv2.setUseOptimized(True)
            
        img = cv2.imread("./fengjing.jpg", cv2.IMREAD_COLOR)
        
        print("cv2.useOptimized() = ", cv2.useOptimized())
        
        time_1 = time.time()
        res = cv2.medianBlur(img,49)
        time_2 = time.time()
        print("diff time = ", time_2 - time_1)
        
        

        
        
