import mainAPI as api
from PIL import Image
import imagehash
import os
import random

net = api.Net()
# api.saveModel(net)


data_folder = "Data/data_image/"

mod_folder = "Data/mod_image/"

list_files = os.listdir(data_folder)
mod_files = os.listdir(mod_folder)

count = 0
for file in list_files:
    filename = data_folder + file
    img1 = api.readImage(filename)

    num_image = random.randint(1,len(mod_files))
    new_filename = mod_folder + mod_files[num_image]
    img2 = api.readImage(new_filename)

    out1 = net.detach(net.view(net.run(img1)))
    out2 = net.detach(net.view(net.run(img2)))
    image1 = Image.fromarray(out1)
    image2 = Image.fromarray(out2)
    # hash1 = imagehash.average_hash(image1)
    # hash2 = imagehash.average_hash(image2)
    # print(hash1,hash2)
    if file[:file.find(".")] in new_filename:
        print(True)
    print(api.hamming2(out1,out2))
    # break
#     if hash1-hash2 == 0:
#         count += 1
#
# print(count)


#
# img1 = api.readImage("test_image/1.jpg")
# img2 = api.readImage("test_image/5.jpg")
# img3 = api.readImage("test_image/6.jpg")
#
# out1 = net.detach(net.view(net.run(img1)))
# out2 = net.detach(net.view(net.run(img2)))
# out3 = net.detach(net.view(net.run(img3)))
#
#
# image1 = Image.fromarray(out1)
# image2 = Image.fromarray(out2)
# image3 = Image.fromarray(out3)
#
# hash1 = imagehash.phash(image1)
# hash2 = imagehash.phash(image2)
# hash3 = imagehash.phash(image3)
# print("{} | {} | {}".format(hash1-hash2,hash1-hash3,hash2-hash3))