import pandas as pd
import os
import torch
import torch.nn as nn
import cv2 as cv

data = pd.read_csv("data.csv",sep=",")#.loc[:,["id","Name","Orientation"]]
image_folder = "../Data/image/"

def run(path):
    pass



if __name__ == '__main__':

    images = os.listdir(image_folder)
    count = {}
    for row in data["Orientation"]:
        if not row in count.keys():
            count.update({row:0})


    for row in data["id"]:
        filename = "{}.jpg".format(row)
        if filename in images:
            count[data[data["id"]==row]["Orientation"].tolist()[0]] +=1
            # print(data[data["id"]==row]["Orientation"].tolist())
        # break



    print(count)
