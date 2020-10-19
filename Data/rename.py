import os
image_folder = "Pictures/"
files = os.listdir(image_folder)
for i,file in enumerate(files,1):
    filename = image_folder+file
    new = "{}{}.jpg".format(image_folder,i)
    os.rename(filename,new)
