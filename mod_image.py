import os
import numpy as np
import cv2 as cv


def size(img):
    img = img.copy()
    rows, cols, _ = img.shape
    M = cv.getRotationMatrix2D(((cols - 1) / 2.0, (rows - 1) / 2.0), 90, 1)
    dst = cv.warpAffine(img, M, (cols, rows))
    return dst


def affine(img):
    imt = img.copy()
    rows, cols, ch = img.shape
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
    M = cv.getAffineTransform(pts1, pts2)
    dst = cv.warpAffine(img, M, (cols, rows))
    return dst


def rotate(img):
    img = img.copy()
    rows, cols, _ = img.shape
    angle = np.random.randint(1, 180,dtype=np.uint8)
    center = (int(cols / 2), int(rows / 2))
    M = cv.getRotationMatrix2D(center, angle, 1)
    dst = cv.warpAffine(img, M, (cols, rows))
    return dst


def color(img):
    img = img.copy()
    images = []
    for n in range(3):
        image = img.copy()
        image[:, :, 0] += np.random.randint(0, 100,dtype=np.uint8)
        image[:, :, 1] += np.random.randint(0, 100,dtype=np.uint8)
        image[:, :, 2] += np.random.randint(0, 100,dtype=np.uint8)
        images.append(image)
    return images


def savePic(filemane, img):
    cv.imwrite(filemane, img)


def getState():
    global lenFiles
    global count
    total = lenFiles * 6
    proc = count / total * 100
    stat = '[%s%s]' % ("##" * (int(proc) // 10), '--' * (10 - (int(proc) // 10)))
    string = 'Complete %22s %i%% Write:%i/%i' % (stat, proc, count, total)
    print(string)


data_folder = "Data/data_image/"
mod_folder = "Data/mod_image/"

list_files = os.listdir(data_folder)
lenFiles = len(list_files)
count = 1
for file in list_files:
    filename = data_folder + file
    img = cv.cvtColor(cv.imread(filename), cv.COLOR_BGR2RGB)
    new_filename = [mod_folder + file[:file.find('.')] + "_{}.jpg".format(count) for count in range(1, 7)]
    new_image = [size(img), affine(img), rotate(img),color(img)[0],color(img)[1],color(img)[2]]
    # print(type(new_image),type(new_filename))
    for name, image in zip(new_filename, new_image):
        getState()
        savePic(name, image)
        count += 1
