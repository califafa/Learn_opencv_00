#膨胀与腐蚀
import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 

def erode(img):
 print(img.shape)
 gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
 ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
 kernel=cv.getStructuringElement(cv.MORPH_RECT,(10,10))
 dst=cv.erode(binary,kernel)#腐蚀
 dst1=cv.dilate(binary,kernel)#膨胀
 plt.imshow(dst)
 plt.show()
 plt.imshow(dst1)
 plt.show()

img=cv.imread('yy.jpg')
erode(img)