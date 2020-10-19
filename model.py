import torchvision.datasets as dset
import torch
import torchvision.transforms as transforms
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

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
        if len(x.size()) != 4:
            x = x.unsqueeze(0)
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(torch.sigmoid(self.conv2(x)))
        x = x.view(-1, 2704)
        x = torch.sigmoid(self.fc1(x))
        # x = F.relu(self.fc2(x))
        # x = self.fc3(x)
        return x.view(-1).cpu().detach().numpy()


def getData():
    transform = transforms.Compose([
                    # transforms.ToPILImage(),
                    transforms.Resize((64,64)),
                    transforms.ToTensor(),
                    # transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))

    ])
    trainset = dset.ImageFolder(root="Data/image/",transform=transform)

    trainloader = torch.utils.data.DataLoader(trainset,shuffle=False,batch_size=1)
    return trainloader
