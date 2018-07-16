import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 

#图像梯度

def lapulasi(img):
 # dst=cv.Laplacian(img,cv.CV_32F)
 # lpls=cv.convertScaleAbs(dst)

 kernel=np.array([[0,1,0],[1,-4,1],[0,1,0]])#拉普拉斯算子
 dst=cv.filter2D(img,cv.CV_32F,kernel)
 lpls=cv.convertScaleAbs(dst)

 plt.imshow(lpls)
 plt.show()



def sobel(img):
 grad_x=cv.Scharr(img,cv.CV_32F,1,0)#Scharr和sobelo都是求导，Scharr能增强边缘
 grad_y=cv.Sobel(img,cv.CV_32F,0,1)
 gradx=cv.convertScaleAbs(grad_x)
 grady=cv.convertScaleAbs(grad_y)
 plt.imshow(gradx)
 plt.show()
 plt.imshow(grady)
 plt.show()
 grad=cv.addWeighted(gradx,0.5,grady,0.5,0)
 plt.imshow(grad)
 plt.show()

img=cv.imread('a.png')
sobel(img)
lapulasi(img)