import model
import base as bd
import cv2 as cv


class MainActive:
    def __init__(self):
        self.bd = bd.DataBase()
        self.net = model.Net()

    def readDB(self):
        allBase = self.bd.readDB()
        return allBase

    def writeDB(self, data):
        self.bd.writeDB(data)

    def runNet(self, img):
        out = self.net(model.img2tensor(img))
        return model.tensor2img(out)

    def getImage(self, path):
        image = cv.cvtColor(cv.imread(path), cv.COLOR_BGR2RGB)
        return image
