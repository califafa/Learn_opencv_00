import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 


#分水岭算法


def watershed_demo():
 print(src.shape)
 blurred=cv.pyrMeanShiftFiltering(src,10,100)
 #gray/binary img
 gray=cv.cvtColor(blurred,cv.COLOR_BGR2GRAY)
 ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
 plt.imshow(binary)
 plt.show()

 kernel=cv.getStructuringElement(cv.MORPH_RECT,(3,3))
 mb=cv.morphologyEx(binary,cv.MORPH_OPEN,kernel,iterations=2)
 sure_bg=cv.dilate(mb,kernel,iterations=3)
 plt.imshow(sure_bg)
 plt.show()

 #distance transform
 dist=cv.distanceTransform(mb,cv.DIST_L2,3)
 dist_output=cv.normalize(dist,0,1.0,cv.NORM_MINMAX)
 plt.imshow(dist_output*50)
 plt.show()

 ret,surface=cv.threshold(dist,dist.max()*0.6,255,cv.THRESH_BINARY)
 plt.imshow(surface)
 plt.show()

 surface_fg=np.uint8(surface)
 unknown=cv.subtract(sure_bg,surface_fg)
 ret,markers=cv.connectedComponents(surface_fg)
 print(ret)

 #watershed transform
 markers=markers+1
 markers[unknown==255]=0
 markers=cv.watershed(src,markers=markers)
 src[markers==-1]=[255,0,0]
 plt.imshow(src)
 plt.show()
 

src=cv.imread('yb.jpg')
watershed_demo()