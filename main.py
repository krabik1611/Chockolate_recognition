import mainAPI as api
import matplotlib.pyplot as plt
from PIL import Image
import imagehash
def show(tens):
    for i in range(1, 8):
        plt.subplot(1, 7, i), plt.imshow(tens[i - 1])
        plt.title(i), plt.xticks([]), plt.yticks([])

    plt.show()


net = api.Net()
# api.saveModel(net)

img1 = api.readImage("test_image/1.jpg")
img2 = api.readImage("test_image/5.jpg")
img3 = api.readImage("test_image/6.jpg")

out1 = net.detach(net.view(net.run(img1)))
out2 = net.detach(net.view(net.run(img2)))
out3 = net.detach(net.view(net.run(img3)))


image1 = Image.fromarray(out1)
image2 = Image.fromarray(out2)
image3 = Image.fromarray(out3)

hash1 = imagehash.phash(image1)
hash2 = imagehash.phash(image2)
hash3 = imagehash.phash(image3)
print("{} | {} | {}".format(hash1-hash2,hash1-hash3,hash2-hash3))