import torch
import torch.nn as nn
import torch.nn.functional as F
from matplotlib import pyplot as plt
import numpy as np


class Pool(nn.Module):
    def __init__(self):
        super(Pool,self).__init__()
        self.conv1 = nn.Conv2d(1,200,(3,3))
        self.conv2 = nn.Conv2d(200,100,(3,3))

    def forward(self,x):
        conv1 = F.max_pool2d(F.relu(self.conv1(x)),(2,2))
        conv2 = F.max_pool2d(F.relu(self.conv2(conv1)),2)
        print(conv2.size())
        return conv2.view(-1,self.num_flat_features(conv2))

    def num_flat_features(self,x):
        size = x.size()[1:]
        num_features = 1
        for s in size:
            num_features *= s
        print(num_features)
        return num_features

#
model = Pool()
a = torch.randn(600,600,3)
print(a.size())
# # model = Pool()
# out = model(a)
# print(out.size())
plt.subplot(1,2,1),plt.imshow(a)
plt.title("Orig"), plt.xticks([]),plt.yticks([])
# plt.subplot(1,2,1),plt.imshow(out)
# plt.title("Pooling"), plt.xticks([]),plt.yticks([])
plt.show()
