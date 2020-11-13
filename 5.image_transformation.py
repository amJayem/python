import cv2 as cv
import numpy as np

img = cv.imread('resources/cat.jpg')

cv.imshow('img', img)


# ---------> 1.Translation  <---------

# translation -> shifting an image along the x and y axis
# so (up,down,left,right) combination
def translate(img, x, y):
    translateMatrix = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, translateMatrix, dimensions)


''' -x -> left, -y -> up, x -> right, y -> down '''

translated = translate(img, 100, 100)
# cv.imshow('translated image', translated)


# ---------> 2.Rotation <---------
def rotate(img, angle, rotationPoint=None):
    (height, width) = img.shape[:2]  # first two value taken
    if rotationPoint is None:
        rotationPoint = (width // 2, height // 2)
    rotationMatrix = cv.getRotationMatrix2D(rotationPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotationMatrix, dimensions)


rotated = rotate(img, 45)
# cv.imshow('rotated image', rotated)
rotated_rotated = rotate(rotated, 45)
# cv.imshow('rotated_rotated', rotated_rotated)

# ---------> 3.Resizing <---------
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
# cv.imshow('resized image', resized)

# ---------> 4.Flipping <---------
flipped = cv.flip(img, 0)
# cv.imshow('flipped', flipped)

# ---------> 5.Cropping <---------

cropped = img[0:200,00:300] # [-height:height,-width:width]
cv.imshow('cropped image', cropped)

cv.waitKey(0)
