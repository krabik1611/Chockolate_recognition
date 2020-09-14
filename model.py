import torch
from torch import nn
import torch.nn.functional as F
import cv2 as cv
import matplotlib.pyplot as plt
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 3)
        self.conv2 = nn.Conv2d(6, 12, 3)
        self.conv3 = nn.Conv2d(12, 30, 3)
        self.conv4 = nn.Conv2d(30, 20, 3)
        self.pool = nn.MaxPool2d(2, 2)
        try:
            self.load_state_dict(torch.load("model_torch.th"))
        except FileNotFoundError:
            print("Model not found!\nCreate model.")

    def forward(self, x):
        x = self.pool(torch.sigmoid(self.conv1(x)))
        x = self.pool(torch.sigmoid(self.conv2(x)))
        x = self.pool(torch.sigmoid(self.conv3(x)))
        x = self.pool(torch.sigmoid(self.conv4(x)))
        x = x.view(-1, self.num_flat_features(x))


        return x

    def num_flat_features(self, x):
        size = x.size()[1:]  # all dimensions except the batch dimension
        num_features = 1
        for s in size:
            num_features *= s
        return num_features


def save(model):
    torch.save(model.state_dict(), "model_torch.th")


def imgResize(img):
    img = img.copy()
    img = cv.resize(img, dsize=(400, 300), interpolation=cv.INTER_CUBIC)
    return img


def img2tensor(img):
    img = imgResize(img)
    img_tensor = torch.Tensor(img).T.unsqueeze(dim=0)
    return img_tensor


def tensor2img(tensor):
    tens = tensor.squeeze(0).T.detach().numpy()
    return tens


if __name__ == '__main__':
    net = Net()
    pool = nn.MaxPool2d(2, 2)
    img = cv.cvtColor(cv.imread("Data/data_image/3.jpg"), cv.COLOR_BGR2RGB)
    # img_tensor = torch.Tensor(img).T.unsqueeze(dim=0)
    img = cv.resize(img, dsize=(400, 300), interpolation=cv.INTER_CUBIC)
    out = net(img2tensor(img))
    save(net)
    print(out.size())
    # plt.subplot(1, 2, 1), plt.imshow(img)
    # plt.title("Orig"), plt.xticks([]), plt.yticks([])
    # plt.subplot(1, 2, 2), plt.imshow(out)
    # plt.title("Pooling"), plt.xticks([]), plt.yticks([])
    # plt.show()
    a = 1
    for n in out.size():
        a *= n

    print(img.shape)

    print(a)
