import cv2 as cv
import matplotlib.pyplot as plt


def show(win_name, mat):
    return cv.imshow(win_name, mat)


img = cv.imread('resources/cat.jpg')
show('opening image', img)

# ----------> 1.bgr 2 gray_scale <----------
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
show('gray image', gray_img)

# ----------> 2.bgr to hsv <----------
# hsv -> hue saturation value (based on,how human think and can see the color)
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
show('hsv img', hsv_img)

# ----------> 3.bgr to L*A*B <----------
lab_img = cv.cvtColor(img, cv.COLOR_BGR2LAB)
show('lab img', lab_img)

# ----------> 4.presenting image by matplot <----------
plt.imshow(img)
plt.show()
# ----------> 5.bgr 2 rgb <----------
rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
show('rgb img', rgb_img)
# plotting again
plt.imshow(rgb_img)
plt.show()
# ----------> 6.hsv to bgr <----------
hsv_bgr_img = cv.cvtColor(img, cv.COLOR_HSV2BGR)
show('hsv to bgr_img', hsv_bgr_img)

# ----------> 7.lab to bgr <----------
lab_bgr_img = cv.cvtColor(img, cv.COLOR_LAB2BGR)
show('lab 2 bgr_img', lab_bgr_img)

# ----------> <----------

cv.waitKey(0)
