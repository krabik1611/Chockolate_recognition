import torch
from torch import nn
import torch.nn.functional as F
import cv2 as cv
import matplotlib.pyplot as plt

class PoolNet(nn.Module):
    def __init__(self):
        super(PoolNet,self).__init__()
        self.conv1 = nn.Conv2d(3,6,3)
        self.conv2 = nn.Conv2d(6,3,3)
        self.pool = nn.MaxPool2d(2,2)


    def forward(self,x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        return x

net = PoolNet()
pool = nn.MaxPool2d(2,2)
img = cv.cvtColor(cv.imread("Data/data_image/1.jpg"),cv.COLOR_BGR2RGB)
img_tensor = torch.Tensor(img).T.unsqueeze(dim=0)
out = net(img_tensor).squeeze(0).T.detach().numpy()
# print(img.shape)
# print(out.shape)
#
plt.subplot(1,2,1),plt.imshow(img)
plt.title("Orig"), plt.xticks([]),plt.yticks([])
plt.subplot(1,2,2),plt.imshow(out)
plt.title("Pooling"), plt.xticks([]),plt.yticks([])
# img_p = pool(img)
# plt.imshow(img)
plt.show()
