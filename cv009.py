#图像直方图

import matplotlib.pyplot as plt 
import cv2 as cv 
import numpy as np 

def plot(img):
 plt.hist(img.ravel(),256,[0,256])
 plt.show()

def hist(img):
 # plt.hist(img.ravel(),256,[0,256])
 color=('blue','green','red')
 for i , color in enumerate(color):
  hist=cv.calcHist([img],[i],None,[256],[0,256])
  plt.plot(hist,color=color)
  plt.xlim([0,256])
 plt.show()

img=cv.imread('a.png')
# plot(img)
hist(img)