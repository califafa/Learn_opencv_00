#霍夫直线检测

import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 
#import ___
#import cv00H


def line_detection(img):#直线
 gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
 edges=cv.Canny(gray,50,150,apertureSize=3)
 lines=cv.HoughLines(edges,1,(np.pi)/180,150)#确保最后一个参数合适，过大将返回None，下面的for语句会出错。过小会导致满屏直线（测不准）
 for line in lines :
  rho,theta=line[0]
  a=np.cos(theta)
  b=np.sin(theta)
  x0=a*rho
  y0=b*rho
  x1=int(x0+1000*(b))
  y1=int(y0-1000*(a))
  x2=int(x0-1000*(b))
  y2=int(y0+1000*(a))
  cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)
 plt.imshow(img)
 plt.show()




def line_detect_possible(img):#线段
 gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
 edges=cv.Canny(gray,50,150,apertureSize=3)
 lines=cv.HoughLinesP(edges,1,(np.pi)/180,120,minLineLength=50,maxLineGap=100)#确保最后一个参数合适，过大将返回None，下面的for语句会出错。过小会导致满屏直线（测不准）
 # if lines.any()!=None: 
 for line in lines:
  x1,y1,x2,y2=line[0]
  cv.line(img,(x1,y1),(x2,y2),(0,0,255),1)
 plt.imshow(img)
 plt.show()
 # else:
  # print('No Lines')


img=cv.imread('a.png')
img1=img.copy()
line_detection(img)
line_detect_possible(img1)