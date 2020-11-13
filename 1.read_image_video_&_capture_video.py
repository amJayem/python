import cv2 as cv

# ------------> reading and showing image <------------
img = cv.imread('resources/leaf.jpg')
cv.imshow('leaf image',img)
# ************> end <************

# ------------> playing video from storage <------------
vdo = cv.VideoCapture('resources/cute cat.mp4')

while True:
    isTrue , frame = vdo.read()
    cv.imshow('cat video',frame)
    if cv.waitKey(10) & 0xFF == ord('q'): # press 'q' to quit video
        break
# ************> end <************

cv.destroyWindow('cat video')
cv.destroyWindow('leaf image')

# ------------> capture live video <------------
vdo_live = cv.VideoCapture(0) # 0 indicates the camera,it may be 1,2.. depends on connected camera
while True:
    isTrue , frame = vdo_live.read()
    cv.imshow('live video',frame)
    if cv.waitKey(10) & 0xFF == ord('q'):
        break

cv.destroyWindow('live video')
# ************> end <************

cv.waitKey(0)