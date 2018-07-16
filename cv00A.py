import cv2 as cv 
import numpy as np 

#直方图均衡化可以自动调节对比度
def equalHist(img): #直方图均衡化，都是基于灰度图像
 gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
 dst=cv.equalizeHist(gray)
 return dst


def clahe(img):#部分直方图均衡化
 gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
 clahe=cv.createCLAHE(clipLimit=5.0,tileGridSize=(8,8))
 dst=clahe.apply(gray)
 return dst 


def rgb_hist(img):
 h,w,c=img.shape
 rgbHist=np.zeros([16*16*16,1],np.float)
 bsize=256/16
 for row in range(h):
  for col in range(w):
   b=img[row,col,0]
   g=img[row,col,1]
   r=img[row,col,2]
   index=np.int(b/bsize)*16*16+np.int(g/bsize)*16+np.int(r/bsize)
   rgbHist[np.int(index),0]=rgbHist[np.int(index),0]+1
 return rgbHist

def hist_compare(img1,img2):
 hist1=rgb_hist(img1)
 hist2=rgb_hist(img2)
 match1=cv.compareHist(hist1,hist2,cv.HISTCMP_BHATTACHARYYA) #巴氏距离
 match2=cv.compareHist(hist1,hist2,cv.HISTCMP_CORREL) #相关性
 match3=cv.compareHist(hist1,hist2,cv.HISTCMP_CHISQR) #卡方
 print(match1,match2,match3)  

img=cv.imread('a.png')
cv.imwrite('eq.png',equalHist(img))
cv.imwrite('clahe.png',clahe(img))

img1=cv.imread('b.png')
hist_compare(img,img1)