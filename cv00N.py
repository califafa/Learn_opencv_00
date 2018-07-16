import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 

#开闭操作


def open(img):
 gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
 ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
 kernel=cv.getStructuringElement(cv.MORPH_RECT,(5,1))
 binary=cv.morphologyEx(binary,cv.MORPH_OPEN,kernel)
 plt.imshow(binary)
 plt.show()

def close(img):
 gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
 ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
 kernel=cv.getStructuringElement(cv.MORPH_RECT,(1,5))
 binary=cv.morphologyEx(binary,cv.MORPH_CLOSE,kernel)
 plt.imshow(binary)
 plt.show()


img=cv.imread('yy.jpg')
open(img)
close(img)