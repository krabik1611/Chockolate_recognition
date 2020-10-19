import torchvision.datasets as dset
import torch
import torchvision.transforms as transforms
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import matplotlib.pyplot as plt
import numpy as np
from model import Net,getData
import cv2 as cv
import os
import pandas as pd
import pickle

device = torch.device("cuda:0" if (torch.cuda.is_available()) else "cpu")

transform = transforms.Compose([
                transforms.ToPILImage(),
                transforms.Resize((64,64)),
                transforms.ToTensor(),
                # transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))

])


net = Net().to(device)
net.load_state_dict(torch.load("model.th"))
#
#

# files = os.listdir(data_folder)
# with torch.no_grad():
#     for i,file in enumerate(files,1):
#         filename = data_folder + file
#         img1 = cv.cvtColor(cv.imread(filename),cv.COLOR_BGR2RGB)
#         tens1 = transform(img1).unsqueeze(0)
#         out1 = net(tens1.to(device))
#         data.append([filename,out1])
#         # writer.writerow([filename,out1])
#         print("{}/{}".format(i,len(files)))
# with open("data.pickle","wb") as f:
#     pickle.dump(data,f)

with open("data.pickle","rb") as f:
    data = pickle.load(f)



img1 = "/home/user/Документы/2.jpg"
img1 = cv.cvtColor(cv.imread(img1),cv.COLOR_BGR2RGB)
tens1 = transform(img1).unsqueeze(0)
out1 = net(tens1.to(device))
result = []
for filename,out in data:
    if np.corrcoef(out1,out)[0][1] >0.94:
        result.append((filename,np.corrcoef(out1,out)[0][1]))
print(len(result))
for filename,coef in result:
    img = cv.cvtColor(cv.imread(filename),cv.COLOR_BGR2RGB)
    plt.subplot(1,2,1),plt.imshow(img)
    plt.title("1"),plt.xticks([]),plt.yticks([])
    plt.subplot(1,2,2),plt.imshow(img1)
    plt.title("orig"),plt.xticks([]),plt.yticks([])
    print(coef)
    plt.show()
