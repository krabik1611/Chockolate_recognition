import os
import cv2 as cv
import matplotlib.pyplot as plt


image_folder = "/home/user/Документы/img/"
files = os.listdir(image_folder)
for file in files:
    filename = image_folder+file
    img = cv.imread(filename,cv.IMREAD_GRAYSCALE)
    blur = cv.GaussianBlur(img,(5,5),0)

    canny = cv.Canny(blur,30,70)
    plt.imshow(cv.cvtColor(canny,cv.COLOR_GRAY2RGB))
    plt.show()
    break
