import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 
#人脸检测
def face_find(img):
 # mohu=cv.pyrMeanShiftFiltering(img,10,100)
 mohu=img
 gray=cv.cvtColor(mohu,cv.COLOR_BGR2GRAY)

 face_finder=cv.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
 faces=face_finder.detectMultiScale(gray,1.05,12)
 for x,y,w,h in faces:
  cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
 plt.imshow(img)
 plt.show()

img=cv.imread('a.png')
face_find(img)