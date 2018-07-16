#边缘保留滤波

import cv2 as cv 
import numpy as np 

def bi(img):
 # img=cv.bilateralFilter(img,0,100,15)#边缘保留滤波，有美颜功能
 img=cv.pyrMeanShiftFiltering(img,10,20)#油画效果
 cv.imwrite('bi.png',img)

img=cv.imread('a.png')
bi(img)
cv.imwrite('bi1.png',img)