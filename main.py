import torchvision.datasets as dset
import torch
import torchvision.transforms as transforms
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt



class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(2704, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.sigmoid(self.conv2(x)))
        # x = x.view(-1, 2704)
        # x = F.relu(self.fc1(x))
        # x = F.relu(self.fc2(x))
        # x = self.fc3(x)
        return x

transform = transforms.Compose([
                transforms.Resize((64,64)),
                transforms.ToTensor(),
                # transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))

])

device = torch.device("cuda:0" if (torch.cuda.is_available()) else "cpu")

trainset = dset.ImageFolder(root="new_model/Image/",transform=transform)

trainloader = torch.utils.data.DataLoader(trainset,shuffle=True,batch_size=1)

net = Net().to(device)
net.load_state_dict(torch.load("model.th"))

out = []
with torch.no_grad():
    for i,data in enumerate(trainloader):
        image,_ = data
        outputs = net(image.to(device))
        out.append(outputs)

        if i == 2:
            break
for img in out:
    vector = img.view(-1).cpu().detach().numpy()
    plt.plot(vector)
    print(vector.max())
# plt.xticks()
plt.show()
