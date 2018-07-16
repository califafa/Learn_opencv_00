#高斯模糊

import cv2 as cv 
import numpy as np 

#a高斯噪声
def gaussiannoise1df(img1):
 img=img1
 h,w,c=img.shape
 for row in range(h):
  for col in range(w):
   s=np.random.normal(0,20,3)
   b=img[row,col,0]
   g=img[row,col,1]
   r=img[row,col,2]
   img[row,col,0]=b+s[0]
   img[row,col,1]=g+s[1]
   img[row,col,2]=r+s[2]
 cv.imwrite('gs.png',img)





imgd=cv.imread('a.png')
cv.imwrite('gsmh-bb.png',imgd)
gaussiannoise1df(imgd)



#高斯模糊
cv.imwrite('gsmh-be.png',imgd)
img2=cv.GaussianBlur(imgd,(5,5),0)
cv.imwrite('gsmh.png',imgd)