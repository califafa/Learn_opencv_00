import cv2 as cv
import numpy as np


def access_pixels(image):
 print(image.shape)
 height=image.shape[0]
 width=image.shape[1]
 channelCount=image.shape[2]
 print('width:%s,height:%s,channelCount:%s'%(width,height,channelCount))
 b=cv.getTickCount()
 for row in range(height):
  for col in range(width):
   for c in range(channelCount):
    pv=image[row,col,c]
    if (row+col+c)%2==0:
     image[row,col,c]=int((255-pv)*((row/400)+(col/400)+(c/3))*3) #反色
 image=cv.bitwise_not(image) #反色
 a=cv.getTickCount()
 print((a-b)/cv.getTickFrequency(),'秒')
 return image



def create_image():
 img=np.zeros([400,400,3],np.uint8)#np.array([[[,],],],np.uint8)
 img[0:200,200:400,0:2]=np.ones([200,200,2])*255
 img[200:400,0:200,1:3]=np.ones([200,200,2])*255
 return img

a=create_image()
a=access_pixels(a)
cv.imwrite('a.png',a)
