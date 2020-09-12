import torch
from torch import nn
import torch.nn.functional as F
import cv2 as cv
import matplotlib.pyplot as plt

class Net(nn.Module):
    def __init__(self):
        super(PoolNet,self).__init__()
        self.conv1 = nn.Conv2d(3,6,3)
        self.conv2 = nn.Conv2d(6,3,3)
        self.pool = nn.MaxPool2d(2,2)
        try:
            self.load_state_dict(torch.load("model_torch.th"))
        except FileNotFoundError:
            print("Model not found!\nCreate model.")

    def forward(self,x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        return x

def save(model):
    torch.save(model.state_dict(), "model_torch.th")

def img2tensor(img):
    img_tensor = torch.Tensor(img).T.unsqueeze(dim=0)
    return img_tensor

def tensor2img(tensor):
    tens = tensor.squeeze(0).T.detach().numpy()
    return tens


if __name__ == '__main__':
    net = PoolNet()
    pool = nn.MaxPool2d(2,2)
    img = cv.cvtColor(cv.imread("Data/data_image/1.jpg"),cv.COLOR_BGR2RGB)
    img_tensor = torch.Tensor(img).T.unsqueeze(dim=0)
    out = net(img_tensor).squeeze(0).T.detach().numpy()
    save(net)
    plt.subplot(1,2,1),plt.imshow(img)
    plt.title("Orig"), plt.xticks([]),plt.yticks([])
    plt.subplot(1,2,2),plt.imshow(out)
    plt.title("Pooling"), plt.xticks([]),plt.yticks([])
    plt.show()
