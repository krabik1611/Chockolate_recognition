import torch
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np


class Net(nn.Module):
    def __init__(self):
        super(Net,self).__init__()
        self.conv1 = nn.Conv2d(1, 7, 3)
        self.conv2 = nn.Conv2d(7, 16, 3)
        self.fc1 = nn.Linear(16 * 32 * 32, 120)
    def forward(self,x):
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        # x = x.view(-1, self.num_flat_features(x))
        # x = F.relu(self.fc1(x))
        return x
    def num_flat_features(self, x):
        size = x.size()[1:]  # all dimensions except the batch dimension
        num_features = 1
        for s in size:
            num_features *= s
        return num_features

net = Net()






filename  = "../Data/data_image/1.jpg"
img = cv.imread(filename)
# plt.imshow(img)
# plt.show()
image = torch.randn(1,1,32,32)
cv.imshow("img",image[0][0].detach().numpy())
cv.waitKey(0)
cv.destroyAllWindows()
out = net(image)
print(out.size())
cv.imshow("img",out[0][2].detach().numpy())
cv.waitKey(0)
cv.destroyAllWindows()
