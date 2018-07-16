import cv2 as cv 
import numpy as np 

def blur(img):
 dst=cv.blur(img,(30,1))#均值模糊。(1,30)是在v方向o模糊，(30,1)是在h方向模糊
 dst=cv.medianBlur(img,5)#中值模糊，去除点噪声

 kernel=np.ones([3,3],np.float)/9
 kernel=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]],np.float)#用这个kernele可以锐化
 kernel=np.array([[0,1,0],[1,-3,1],[0,1,0]],np.float)
 dst=cv.filter2D(img,-1,kernel=kernel)#自定义模糊

 return dst



img=cv.imread('a.png')
cv.imwrite('blur.png',blur(img))