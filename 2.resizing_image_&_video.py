import cv2 as cv

img = cv.imread('resources/leaf.jpg')

height = 600
width = 800
# ------------> resize image <------------
imgResize = cv.resize(img,(width,height))
cv.imshow('leaf image',img)
cv.imshow('resized image',imgResize)

# ------------> resize video <------------
vdo = cv.VideoCapture('resources/cute cat.mp4')
while True:
    isTrue,frame = vdo.read()
    cv.imshow('video',frame)
    vdoResized = cv.resize(frame,(width,height))
    cv.imshow('resized video',vdoResized)

    if cv.waitKey(1) & 0xFF == ord('e'):
        cv.destroyWindow('video')
        break


if cv.waitKey(10) & 0xFF == ord('q'):
    cv.destroyWindow('leaf image')
cv.waitKey(0)