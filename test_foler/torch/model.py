import torch
import torch.nn as nn
import torch.nn.functional as F
import cv2 as cv


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(3, 64, 1),
            nn.ReLU(),
            nn.Conv2d(64, 128, 1)
        )
        self.layer2 = nn.Sequential(
            nn.MaxPool2d(2, 2),
            nn.Conv2d(128, 128, 1),
            nn.ReLU(),
            nn.Conv2d(128, 256, 1),
            nn.ReLU()
        )
        self.layer3 = nn.Sequential(
            nn.MaxPool2d(2, 2),
            nn.Conv2d(256, 256, 1),
            nn.ReLU(),
            nn.Conv2d(256, 256, 1),
            nn.ReLU(),
            nn.Conv2d(256, 512, 1),
            nn.ReLU()
        )
        self.layer4 = nn.Sequential(
            nn.MaxPool2d(2, 2),
            nn.Conv2d(512, 512, 1),
            nn.ReLU(),
            nn.Conv2d(512, 512, 1),
            nn.ReLU(),
            nn.Conv2d(512, 512, 1),
            nn.ReLU()
        )
        self.layer5 = nn.Sequential(
            nn.MaxPool2d(2, 2),
            nn.Conv2d(512, 512, 1),
            nn.ReLU(),
            nn.Conv2d(512, 512, 1),
            nn.ReLU(),
            nn.Conv2d(512, 512, 1),
            nn.ReLU()
        )
        self.layer6 = nn.MaxPool2d(2,2)
        self.layer7 = nn.Sequential(
            nn.Linear(512,4096),
            nn.ReLU(),
            nn.Linear(4096, 1000),
            nn.ReLU(),
            nn.Softmax(dim=1)
        )

    def forward(self,x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)
        x = self.layer5(x)
        x = self.layer6(x).reshape(7, 7, 512)
        x = self.layer7(x)
        return x.view(-1)

    def num_flat_features(self, x):
        size = x.size()[1:]  # all dimensions except the batch dimension
        num_features = 1
        for s in size:
            num_features *= s
        return num_features




def img2tensor(img):
    return torch.from_numpy(img).permute(2, 0, 1).unsqueeze(dim=0).float()


def imgResize(img):
    img = img.copy()
    img = cv.resize(img, dsize=(224, 224), interpolation=cv.INTER_CUBIC)
    return img


def readImage(path):
    return cv.cvtColor(cv.imread(path), cv.COLOR_BGR2RGB)

def tensor2img(tensor):
    no_batch = tensor.long().squeeze(dim=0)

    width_height_channels = no_batch.permute(1, 2, 0)

    final_image = width_height_channels.numpy()
    return final_image
net = Net()

image = imgResize(readImage("../../test_image/1.jpg"))
out = net(img2tensor(image))
print(out.size())
