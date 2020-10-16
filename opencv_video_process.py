# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 10:24:51 2020

@author: shangyonggang
"""

import cv2
import os
import time

if __name__ == "__main__":
    
    if 0:
        #摄像头读取
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("error: read video capture failed!")
            exit()
                   
        
        while True:
            ret, frame = cap.read()            
            if not ret:
                break
            
            cv2.imshow("frame", frame)
            cv2.waitKey(30)

        cap.release()
        
    
    if 0:
        #视频文件读取
        video_path = "./qifengle.mkv"
        cap = cv2.VideoCapture(video_path)

        while cap.isOpened():
            ret, frame = cap.read()
            
            if not ret:
                break

        cap.release()
        
    if 0:
        #读取图片序列
        imgs_path = "./imgs//%04d.jpg"
        cap = cv2.VideoCapture(imgs_path)            
        
        while cap.isOpened():
            ret, frame = cap.read()
            
            if not ret:
                break

        cap.release()
        
    if 1:
        #获取视频整体信息
        video_path = "./qifengle.mkv"
        #video_path = "./video1.mp4"
        cap = cv2.VideoCapture(video_path)
        
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) #宽
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) #高
        fps = cap.get(cv2.CAP_PROP_FPS) #帧率
        fourcc = cap.get(cv2.CAP_PROP_FOURCC) #编码格式
        count = cap.get(cv2.CAP_PROP_FRAME_COUNT) #帧数
        format1 = cap.get(cv2.CAP_PROP_FORMAT) #图片存储格式
        mode = cap.get(cv2.CAP_PROP_MODE) #？？？
        brightness = cap.get(cv2.CAP_PROP_BRIGHTNESS) #亮度，仅支持有该功能的摄像头方式
        contrast = cap.get(cv2.CAP_PROP_CONTRAST) #对比度，仅支持摄像头方式
        saturation = cap.get(cv2.CAP_PROP_SATURATION) #饱和度，仅支持摄像头方式
        hue = cap.get(cv2.CAP_PROP_HUE) #色调，仅支持摄像头方式
        gain = cap.get(cv2.CAP_PROP_GAIN) #增益， 亮度，仅支持有该功能的摄像头方式
        exposure = cap.get(cv2.CAP_PROP_EXPOSURE) #曝光度，仅支持有该功能的摄像头方式
        b_rgb= cap.get(cv2.CAP_PROP_CONVERT_RGB) #是否应该转为RGB格式
        

        print("111 = ", cap.set(cv2.CAP_PROP_POS_FRAMES,320))
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT,320)
        
        while cap.isOpened():
            ret, frame = cap.read()
            
            if not ret:
                break
            
            #print("111 = ", frame.shape)
            

        cap.release()
        
    if 0:
        #保存视频        
        cap = cv2.VideoCapture(0)        
        
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #宽
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #高        
        
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('./output.avi', fourcc, 30.0, (width, height))
        num = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:  
                break
                       
            out.write(frame)
            
            num += 1           
            if num >= 150:
                break

        cap.release()
        out.release()
        
        