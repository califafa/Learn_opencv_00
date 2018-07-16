#直方图a反向投影
import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 

def hist2d(img):
 hsv=cv.cvtColor(img,cv.COLOR_RGB2HSV)
 hist=cv.calcHist([hsv],[0,1],None,[180,256],[0,100,0,256])
 cv.imwrite('hist2d.png',hist)
 plt.imshow(img,interpolation='nearest')
 plt.show()


def back_proj():
 sample=cv.imread('a.png')[400:420,200:220]
 target=cv.imread('a.png')
 s_hsv=cv.cvtColor(sample,cv.COLOR_BGR2HSV)
 t_hsv=cv.cvtColor(target,cv.COLOR_BGR2HSV)

 s_hist=cv.calcHist([s_hsv],[0,1],None,[18,26],[0,180,0,256])
 cv.normalize(s_hist,s_hist,0,255,cv.NORM_MINMAX)
 dst=cv.calcBackProject([t_hsv],[0,1],s_hist,[0,180,0,256],1)

 cv.imwrite('tt.png',dst)
 dst=cv.imread('tt.png')
 dst=cv.bitwise_and(dst,target)
 plt.imshow(dst)
 plt.show()
 # plt.imshow(sample)
 # plt.show()
 # plt.imshow(target)
 # plt.show()



# img=cv.imread('a.png')
# hist2d(img)
back_proj()