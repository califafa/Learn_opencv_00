#读取/写入图片/视频（写入帧），转换灰度图像，使用摄像头


import cv2 as cv 
import numpy as np
import time
import os
#read image:
src=cv.imread("/home/california/.face")

#需要配置GTK+2.x或Carbon
#cv.namedWindow("image_xxx",cv.WINDOW_AUTOSIZE)
#cv.imshow("image_xxx",src)
#cv.waitKey(0)

print('',type(src))
print('height,weight,channelCount		',src.shape)
print('pixelCount		',src.size)					#height*weight*channelCount
print('bitCount_perChannel		',src.dtype)

pixel_info=np.array(src)
print(pixel_info)







#read video:
capture=cv.VideoCapture(0) #0是设备号，可以替换成视频文件路径
b=time.time()
while(time.time()-b<0.1):
	ret,frame=capture.read() #使用摄像头
	frame=cv.flip(frame,1)			#镜像，frame是帧
	str='a'+str(time.time())+'.png'
	cv.imwrite(str,frame)					#将每一幀写入磁盘
# cv.imshow("video_xxx",frame)
#	c=cv.waitKey(50)
# if c==27:
#  break
grey=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)	#生成灰度图像
cv.imwrite('a.png',grey)

