import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 

#形态学操作
def topHat(img):
 gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
 kernel=cv.getStructuringElement(cv.MORPH_RECT,(15,15))
 dst=cv.morphologyEx(gray,cv.MORPH_TOPHAT,kernel)#顶帽操作
 cimg=np.array(gray.shape,np.uint8)
 cimg=100
 dst=cv.add(dst,cimg)
 plt.imshow(dst)
 plt.show()

def blackHat(img):
 gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
 kernel=cv.getStructuringElement(cv.MORPH_RECT,(15,15))
 dst=cv.morphologyEx(gray,cv.MORPH_BLACKHAT,kernel)#黑帽操作
 cimg=np.array(gray.shape,np.uint8)
 cimg=100
 dst=cv.add(dst,cimg)
 plt.imshow(dst)
 plt.show()


def gradient(img):
 gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
 kernel=cv.getStructuringElement(cv.MORPH_RECT,(15,15))
 dst=cv.morphologyEx(gray,cv.MORPH_GRADIENT,kernel)#黑帽操作
 cimg=np.array(gray.shape,np.uint8)
 cimg=100
 dst=cv.add(dst,cimg)
 plt.imshow(dst)
 plt.show()


def gra(img):
 gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
 kernel=cv.getStructuringElement(cv.MORPH_RECT,(5,5))
 dm=cv.dilate(img,kernel)
 em=cv.erode(img,kernel)
 dst1=cv.subtract(img,em)#intermal gradient
 dst2=cv.subtract(dm,img)#external gradient

 plt.imshow(dst1)
 plt.show()
 plt.imshow(dst2)
 plt.show()

img=cv.imread('yy.jpg')
topHat(img)
blackHat(img)
gradient(img)
gra(img)