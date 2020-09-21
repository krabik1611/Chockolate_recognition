import model
import cv2 as cv


class Net():
    def __init__(self):
        self.net = model.Image()

    def run(self, img):
        img = self.imgResize(img)
        tens = self.img2tensor(img)
        out = self.net(tens)
        return out[0]

    def img2tensor(self, img):
        return model.img2tensor(img)

    def imgResize(self, img):
        return model.imgResize(img)

    def tensor2img(self, tensor):
        return model.tensor2img(tensor)

    def detach(self, tens):
        return tens.detach().numpy()

    def view(self,tens):
        return tens.view(-1)


def readImage(path):
    return cv.cvtColor(cv.imread(path), cv.COLOR_BGR2RGB)


def saveModel(obj):
    model.save(obj)


def hamming2(s1, s2):
    """Calculate the Hamming distance between two bit strings"""
    assert len(s1) == len(s2)
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))