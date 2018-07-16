import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 

#模板匹配

def temp():
 tpl=cv.imread('a.png')[400:420,200:220]
 target=cv.imread('a.png')
 # method
 methods=[cv.TM_SQDIFF_NORMED,cv.TM_CCOEFF_NORMED,cv.TM_CCORR_NORMED]
 th,tw=tpl.shape[:2]
 for md in methods:
  print(md)
  result=cv.matchTemplate(target,tpl,md)
  min_val,max_val,min_loc,max_loc=cv.minMaxLoc(result)
  if (md==cv.TM_SQDIFF_NORMED):
   tl=min_loc
  else:
   tl=max_loc 
  br=(tl[0]+tw,tl[1]+th)
  cv.rectangle(target,tl,br,(255,0,0),1)
  plt.imshow(target)
  # plt.imshow(result)
  plt.show()

temp()