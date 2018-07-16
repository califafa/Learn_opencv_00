import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 

#图像金字塔


#gaosi
def pyramid(img):
 level=3
 temp=img.copy()
 pyramid_img=[]
 for i in range(level):
  dst=cv.pyrDown(temp)
  pyramid_img.append(dst)
  temp=dst.copy()
  str1=str(i)+'778.png'
  cv.imwrite(str1,temp)
 plt.imshow(dst)
 plt.show()
 return pyramid_img

def lapulasi(img):
 pimg=pyramid(img)
 level=len(pimg)
 for i in range(level-1,0,-1):
  expand=cv.pyrUp(pimg[i],dstsize=pimg[i-1].shape[:2])
  lpls=cv.subtract(pimg[i-1],expand)
  plt.imshow(lpls)
  plt.show()


pyramid(cv.imread('a.png'))
lapulasi(cv.imread('a.png'))