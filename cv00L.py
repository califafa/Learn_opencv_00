#对象测量

import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 

def measure(img):
 gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
 ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY_INV|cv.THRESH_OTSU)
 print(ret)
 plt.imshow(binary)
 plt.show()
 outImage,contours,hireachy=cv.findContours(binary,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
 for i,contour in enumerate(contours):
  area=cv.contourArea(contour)#面积
  rect=cv.boundingRect(contour)#外接矩形
  mm=cv.moments(contour)#几何距
  print(area)
  cx=mm['m10']/mm['m00']
  cy=mm['m01']/mm['m00']
  cv.circle(img,(np.int(cx),np.int(cy)),2,(255,0,0),2)
  cv.rectangle(img,(rect[0],rect[1]),(rect[0]+rect[2],rect[1]+rect[3]),(0,255,0))
  approxCurve=cv.approxPolyDP(contour,4,True) 
  print(approxCurve.shape)
  if approxCurve.shape[0]>4:#可以区分形状
   cv.drawContours(img,contours,i,(255,0,0),2)

 plt.imshow(img)
 plt.show()


img=cv.imread('xz.jpg')
measure(img)

