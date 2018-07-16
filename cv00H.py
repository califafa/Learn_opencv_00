#canny 边缘提取

import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 

def edge(img):
 blurred=cv.GaussianBlur(img,(3,3),0)
 gray=cv.cvtColor(blurred,cv.COLOR_BGR2GRAY)
 xgrad=cv.Sobel(gray,cv.CV_16SC1,1,0)
 ygrad=cv.Sobel(gray,cv.CV_16SC1,0,1)
 edg_output=cv.Canny(xgrad,ygrad,40,160)
 plt.imshow(edg_output)
 plt.show()
 dst=cv.bitwise_and(img,img,mask=edg_output)
 plt.imshow(dst)
 plt.show()

img=cv.imread('a.png')
edge(img)
