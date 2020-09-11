import torch
from torch import nn
import torch.nn.functional as F


class Net(nn.Module):
    def __init__(self):
        super(Net,self).__init__()
        self.conv1 = nn.Conv2d(1,64,kernel_size=(3,3),padding=1)
        self.conv2 = nn.Conv2d(64,64,kernel_size=(3,3),padding=1)
        self.max_pool = nn.MaxPool2d(2, 2)
        self.global_pool = nn.AvgPool2d(7)
        self.fc1 = nn.Linear(64, 64)
        self.fc2 = nn.Linear(64, 10)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = self.max_pool(x)

        x = F.relu(self.conv2(x))
        x = F.relu(self.conv2(x))
        x = self.max_pool(x)

        x = F.relu(self.conv2(x))
        x = F.relu(self.conv2(x))
        x = self.global_pool(x)

        x = x.view(-1, 64)

        x = F.relu(self.fc1(x))
        x = self.fc2(x)

        x = F.log_softmax(x)

        return x



model = Net()
params = model.state_dict()
for key in params.keys():
    print(key)
