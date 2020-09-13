import os
import cv2 as cv

data = "Data/data_image/"
files = os.listdir(data)
average = [0,0]
for file in files:
    filename = data + file
    img = cv.imread(filename)
    y, x,_ = img.shape
    # print("({},{})".format(x, y))
    average[0] += x / len(files)
    average[1] += y / len(files)

print(average)
