#图像二值化

import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 

def threshold(img):
 gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
 ret,binary=cv.threshold(gray,127,255,cv.THRESH_BINARY|cv.THRESH_TRUNC)
 print(ret)
 plt.imshow(binary)
 plt.show()

#高斯二值化对文档有奇效
def local_threshold(img):
 gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
 binary=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,25,10)
 plt.imshow(binary)
 plt.show()


img=cv.imread('a.png')
# threshold(img)
local_threshold(img)