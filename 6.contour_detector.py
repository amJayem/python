import cv2 as cv
import numpy as np

img = cv.imread('resources/cat.jpg')
cv.imshow('cat image', img)


def s(win_name, mat):
    return cv.imshow(win_name, mat)


# ---------> 1.converting bgr 2 gray <---------
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
s('gray image', gray)

# ---------> 2.canny edge detector <---------
canny = cv.Canny(img, 125, 175)
s('canny image', canny)

# ---------> 3.contours and hierarchy <---------
'''
 --------------- 
|   ---------   |<-- rectangle1
|  |         |<-|-- rectangle2 
|  |    0 <--|--|-- circle
|  |         |  |
|   ---------   |
 ---------------
the hierarchy essentially the representation,
the openCv uses to find the contours
'''
contours, hierarchy = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# cv.RETR_LIST     -> all contours of an image
# cv.RETR_EXTERNAL -> only external contours
# cv.RETR_TREE     -> all hierarchical contours
#
# cv.CHAIN_APPROX_NONE -> does nothing returns all of the contours
# cv.CHAIN_APPROX_SIMPLE -> two ends point of a line such as 'a' & 'b' (a)---------------(b)
print(f'contours {len(contours)} found!')

# ---------> 4. blurring image <---------
blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
s('blur image', blur)

# ---------> 5.threshold <---------
_, thresh = cv.threshold(gray, 155, 255, type=cv.THRESH_BINARY)
# threshold -> returns the binarize the image value like '0' or '1'
contours, hierarchies = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
print(f'contours {len(contours)} found!')
s('threshold image', thresh)

# ---------> 6.draw contours <---------
blank = np.zeros(img.shape,'uint8')
# s('blank image',blank)

cv.drawContours(blank,contours,-1,(0,0,255),2)
s('drawing contours on blank image',blank)
cv.waitKey(0)
