import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 

#轮廓发现

def contours(img):
 gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
 ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
 plt.imshow(binary)

 cloneImg,contours,heriachy=cv.findContours(binary,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
 for i ,contour in enumerate(contours):
  cv.drawContours(img,contours,i,(0,0,255),1)
  print(i)

 plt.imshow(img)
 plt.show()

img=cv.imread('yb.jpg')
contours(img)