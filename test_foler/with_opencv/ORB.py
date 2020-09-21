import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def keyDot(img):
    img = img.copy()
    orb = cv.ORB_create()
    kp = orb.detect(img,None)
    kp,des =  orb.compute(img,kp)
    img1 = cv.drawKeypoints(img, kp, None, (0, 255, 0), flags=0)
    return img1


img1 = cv.cvtColor(cv.imread("../../test_image/5.jpg"),cv.COLOR_BGR2RGB)
img2 = cv.cvtColor(cv.imread("../../test_image/6.jpg"),cv.COLOR_BGR2RGB)

plt.subplot(1,2,1), plt.imshow(keyDot(img1))
plt.title("1"),plt.xticks([]),plt.yticks([])
plt.subplot(1,2,2), plt.imshow(keyDot(img2))
plt.title("1"),plt.xticks([]),plt.yticks([])
plt.show()