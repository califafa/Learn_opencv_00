import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 

#霍夫圆检测
#对噪声敏感
def detect_circles(img):
 dst=cv.pyrMeanShiftFiltering(img,20,70)
 cimg=cv.cvtColor(dst,cv.COLOR_BGR2GRAY)
 circles=cv.HoughCircles(cimg,cv.HOUGH_GRADIENT,1,20,param1=60,param2=40,minRadius=0,maxRadius=0)
 circles=np.int16(np.around(circles))
 for i in circles[0,:]:
  cv.circle(img,(i[0],i[1]),i[2],(255,0,0),2)
  cv.circle(img,(i[0],i[1]),2,(255,0,255),2)
 plt.imshow(img)
 plt.show()

img=cv.imread('yb.jpg')
detect_circles(img)