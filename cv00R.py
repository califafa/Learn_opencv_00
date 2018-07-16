import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 
from PIL import Image
import pytesseract as tess
#验证码识别
def recognize_text(src):
 gray=cv.cvtColor(src,cv.COLOR_BGR2GRAY)
 ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
 kernel=cv.getStructuringElement(cv.MORPH_RECT,(1,2))
 bin1=cv.morphologyEx(binary,cv.MORPH_OPEN,kernel)
 kernel=cv.getStructuringElement(cv.MORPH_OPEN,(2,1))
 open_out=cv.morphologyEx(bin1,cv.MORPH_OPEN,kernel)
 plt.imshow(open_out)
 plt.show()

 cv.bitwise_not(open_out,open_out)#使背景为白色
 textImage=Image.fromarray(open_out)
 text=tess.image_to_string(textImage)
 print('result:%s'%text)

img=cv.imread('y1.jpeg')
recognize_text(img)