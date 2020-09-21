import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import imagehash
import PIL.Image as Image

def imgResize(img):
    img = img.copy()
    img = cv.resize(img, dsize=(8, 8))
    return img

image_path = '../../test_image/5.jpg'

img1 = Image.open(image_path)

image_path = '../../test_image/2.jpg'
img2 = Image.open(image_path)

o1 = imagehash.phash(img1)
o2 = imagehash.phash(img2)
print("{} | {} | {}".format(o1,o2,int(o1-o2)))


