import cv2 as cv

img = cv.imread('resources/leaf.jpg')
# cv.imshow('leaf image',img)

# ------------> 1.Resized <------------
img_resized = cv.resize(img,(910,540),interpolation=cv.INTER_AREA)
cv.imshow('resized image',img_resized)

# ------------> 2.converting to grayScale <------------
img_gray = cv.cvtColor(img_resized,cv.COLOR_BGR2GRAY)
cv.imshow('gray image',img_gray)

# ------------> 3.blurring image <------------
img_blur = cv.GaussianBlur(img_resized,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur image',img_blur)

# ------------> 4.Edge cascade <------------
# try to find the edges that present in the images
# many of edge detector 'canny' is famous one in OpenCv
img_canny = cv.Canny(img_resized,125,175)
cv.imshow('canny image',img_canny)

# ------------> 5. Dilating the image <------------
img_dilated = cv.dilate(img_canny,(7,7),iterations=3)
cv.imshow('dilated image',img_dilated)

# ------------> 6.Eroding <------------
img_eroded = cv.erode(img_dilated,(7,7),iterations=3)
cv.imshow('eroded image',img_eroded)

# ------------> 7.Cropping image <------------
img_cropped = img_resized[50:200,200:400]
cv.imshow('cropped image',img_cropped)

cv.waitKey(0)