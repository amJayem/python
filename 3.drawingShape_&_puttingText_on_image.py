import cv2 as cv
import numpy as np

width,height = 1000,600
# ------------> reading image from storage <------------
img = cv.imread('resources/leaf.jpg')
img = cv.resize(img,(width,height))
cv.imshow('resized leaf image',img)

# ------------> creating a blank image <------------
blank = np.zeros((width,height,3),dtype='uint8') # 'uint8' basically data type of an image
cv.imshow('blank image',blank)

# ------------> 1. paint the image in a certain colour <------------
blank[:] = 0,200,0 # all pixel (color = green)
blank[200:300,300:400] = 0,0,255 # selected pixel (color = red)
cv.imshow('painting blank',blank)

# ------------> 2.drawing rectangle <------------
blank = np.zeros((width,height,3),dtype='uint8')
# cv.rectangle(blank,(0,0),(250,250),(0,255,0),cv.FILLED)# or '-1' is also for filled
# cv.rectangle(blank,(0,0),(250,250),(0,0,255),10)
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=12)
cv.imshow('rectangle blank',blank)

# ------------> 3. draw circle <------------
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=3)
cv.imshow('circle blank',blank)

# ------------> 4. draw line <------------
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,0,255),thickness=3)
cv.imshow('line blank',blank)

# ------------> 5.write text <------------
cv.putText(blank,'hello',(255,255),cv.FONT_HERSHEY_SIMPLEX,1.0,(0,255,0),2)
cv.imshow('text for test',blank)

# ------------> drawing our National flag <------------
width,height = 600,1000
blank = np.zeros((width,height,3),dtype='uint8')
blank[:] = 0,200,0 # all pixel (color = green)

cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),200,(0,0,255),thickness=-1)
cv.rectangle(blank,(0,0),(blank.shape[1],blank.shape[0]),(100,0,0),thickness=12)
cv.putText(blank,'Bangladesh',(400,300),cv.FONT_HERSHEY_SIMPLEX,1.0,(255,0,0),2)
cv.imshow('National flag',blank)

cv.waitKey(0)