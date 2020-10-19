import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from threading import Thread
import pandas as pd
header = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0"}
image_folder = "image/"
url = "https://colnect.com/chocolate_wrappers/chocolate_wrapper/10901"
df = pd.read_csv("data.csv")
for i,url in zip(df["id"],df["Link"]):
    if i <44:
        continue
    try:
        r = requests.get(url,headers=header)

        soup = BeautifulSoup(r.text,"lxml")
        for img in soup.find_all("img"):
            link = img.get("src")
            if "i.colnect.net/f/" in link:
                url = link[2:]
                url = "https://"+url[:14] + "b" + url[15:]
                img = requests.get(url,headers = header)
                with open("{}{}.jpg".format(image_folder,i),"wb") as f:
                    for n in img:
                        f.write(n)
        print("Complete: {}/{}".format(i,len(df["id"])))
        if i%2 == 0:
            sleep(10)

    except:
        print("error")
