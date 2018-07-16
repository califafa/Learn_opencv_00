#cv的算数运算

import cv2 as cv 
import numpy as np 
import time
capture=cv.VideoCapture(0)
ret,frame=capture.read()
b=time.time()
while time.time()-b<2:
 f=capture.read()

ret1,frame1=capture.read()
frame3=cv.imread('b.png')
frame2=cv.add(frame[:,:,:]*[0.5,0.5,0.5],frame1[:,:,:]*[0.5,0.5,0.5])
frame4=cv.subtract(frame,frame1)
cv.imwrite('a.png',frame2)   #add,subtract,divide,multiply
cv.imwrite('a4.png',frame4)
mean1=cv.mean(frame4)#return (b,g,r),求各个通道的均值
mean_stddev=cv.meanStdDev(frame4)#return array([均值]),array([方差]),求3通道均值，方差
# cv.imwrite('f1.png',frame1)
# cv.imwrite('f.png',frame)
print(mean_stddev)

#逻辑运算
# cv.bitwise_and
# cv.bitwise_not
# cv.bitwise_or
# cv.bitwise_xor

#权重计算
frame5=cv.addWeighted(frame,1.5,frame4,0.5,20)
cv.imwrite('a5.png',frame5)