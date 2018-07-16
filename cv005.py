import cv2 as cv 
import numpy as np 

#img.copy()
#img[:,:]=img[:,:]

def fill_color(img):
 copyImg=img.copy()
 h,w=img.shape[:2]
 mask=np.ones([h+2,w+2],np.uint8)#mask必须为h+2,w+2, 不知道为什么。并且mask为0的位置才会被填充
 mask[100:h-19,100:w-19]=0
 #泛洪填充， 画图里的墨水桶（彩色图像
 # cv.floodFill(copyImg,mask,(30,30),(0,255,128),(100,100,100),(50,50,50),cv.FLOODFILL_MASK_ONLY)
 # cv.imwrite('mask_only.png',copyImg)
 cv.floodFill(copyImg,mask,(40,50),(0,255,128),(100,100,100),(50,50,50),cv.FLOODFILL_FIXED_RANGE)#填充方式：FLOODFILL_FIXED_RANGE    FLOODFILL_MASK_ONLY
 cv.imwrite('fixedRange.png',copyImg)
 cv.imwrite('mask.png',mask)



image=cv.imread('a.png')
fill_color(image)