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


device = torch.device("cuda:0" if (torch.cuda.is_available()) else "cpu")

transform = transforms.Compose([
                transforms.ToPILImage(),
                transforms.Resize((64,64)),
                transforms.ToTensor(),
                # transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))

])

trainloader = getData()

net = Net().to(device)
net.load_state_dict(torch.load("model.th"))
#
# out = []
# with torch.no_grad():
#     for i,data in enumerate(trainloader):
#         image,_ = data
#         outputs = net(image.to(device))
#         out.append(outputs)
#
#         if i == 2:
#             break
#
# for img in out:
#     vector = img.view(-1).cpu().detach().numpy()
#
#     plt.hist(vector)
#     print(vector.shape)
# # plt.xticks()
# plt.show()
img = "test_image/1.jpg"
img = cv.cvtColor(cv.imread(img),cv.COLOR_BGR2RGB)
# plt.imshow(img)
# plt.show()

tens = transform(img)

out = net(tens.to(device))
print(out.shape)
