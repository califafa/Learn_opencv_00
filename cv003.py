import cv2 as cv 
import time
import numpy as np
#色彩空间转换

def color_space_translate(img):
 gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
 hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
 yuv=cv.cvtColor(img,cv.COLOR_BGR2YUV)

 #opencv中，hsv范围[0:181]

def extrace_object():
 b=time.time()
 capture=cv.VideoCapture(0)
 ret,frame=capture.read()
 if ret==False:
  return False
 bgr=frame
 frame=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
 
 lowHSV=np.array([35,41,44])
 highHSV=np.array([79,255,255])
 b,g,r=cv.split(bgr)#将frame分为3个通道，每个为灰度图像
 reTogether=cv.merge([g,b,r])#g将三个通道合起来
 #frame[;,;,2]=0
 frame=cv.inRange(frame,lowerb=lowHSV,upperb=highHSV)#过滤，找到lowerb和upperb之间符合条件的i像素点，赋值为1。其余为0。
 cv.imwrite('a.png',frame)
 cv.imwrite('b.png',reTogether)

extrace_object()