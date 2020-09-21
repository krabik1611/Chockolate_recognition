import matplotlib.pyplot as plt
import cv2 as cv
import torch
import torch.nn as nn
import os

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


class Image(nn.Module):
    def __init__(self):
        super(Image, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.conv2 = nn.Conv2d(6, 10, 5)
        self.conv3 = nn.Conv2d(10, 7, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.active = nn.ReLU()
        try:
            self.load_state_dict(torch.load("model_torch.th"))
        except FileNotFoundError:
            # print("Model not found!\nCreate file model!\n")
            save(self)

    def forward(self, x):
        x = self.pool(self.active(self.conv1(x)))
        x = self.pool(self.active(self.conv2(x)))
        x = self.pool(self.active(self.conv3(x)))

        return x#.view(-1, self.num_flat_features(x))

    def num_flat_features(self, x):
        size = x.size()[1:]  # all dimensions except the batch dimension
        num_features = 1
        for s in size:
            num_features *= s
        return num_features


def save(model):
    torch.save(model.state_dict(), "model_torch.th")


def img2tensor(img):
    return torch.from_numpy(img).permute(2, 0, 1).unsqueeze(dim=0).float()


def imgResize(img):
    img = img.copy()
    img = cv.resize(img, dsize=(64, 64), interpolation=cv.INTER_CUBIC)
    return img


def tensor2img(tensor):
    no_batch = tensor.long().squeeze(dim=0)

    width_height_channels = no_batch.permute(1, 2, 0)

    final_image = width_height_channels.numpy()
    return final_image

def show(tens):
    for i in range(1, 8):
        plt.subplot(1, 7, i), plt.imshow(tens[i - 1])
        plt.title(i), plt.xticks([]), plt.yticks([])

    plt.show()






if __name__ == "__main__":
    net = Image()
    for i in range(1, 3):
        img = imgResize(cv.cvtColor(cv.imread("Data/data_image/{}.jpg".format(i)), cv.COLOR_BGR2RGB))
        mod_image = imgResize(cv.cvtColor(cv.imread("Data/mod_image/{}_2.jpg".format(i)), cv.COLOR_BGR2RGB))
        # plt.imshow(img)
        # plt.show()
        tens = img2tensor(img)
        out = net(tens)[0].detach().numpy()
        mod = net(img2tensor(mod_image))[0].detach().numpy()
        # plt.plot(out)
        show(mod)
        # print(out.shape)
        # a = np.linalg.det(out)
        # b = np.linalg.det(mod)
        # print("det A:\n{}\ndet b\n{}\nraz\n{}".format(a, b, a-b))
        # print((out-mod).sum())

    # plt.show()
