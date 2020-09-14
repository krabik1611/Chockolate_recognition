import model
import os
import torch
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
import base as bd

# data_dir = "Data/data_image/"
# list_files = os.listdir(data_dir)
# mod_dir = "Data/mod_image/"
# mod_files = os.listdir(mod_dir)
# net = model.Net()
base = bd.DataBase()
# color = ['k','g','r','c','m','y']
# count = 1
# for file in list_files:
#     filename = data_dir + file
#     # print(filename)
#     img = cv.cvtColor(cv.imread(filename), cv.COLOR_BGR2RGB)
#     orig = net(model.img2tensor(img))
#     dict_data = {
#         "id": file[:file.find(".")],
#         "filename": filename,
#         "data": model.tensor2img(orig)
#     }
#     base.writeDB(dict_data)

rows = base.readDB()
print(len(rows))
# for row in rows:
#     print(row[0], row[1], row[2])
