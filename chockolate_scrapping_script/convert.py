import csv
import os
from bs4 import BeautifulSoup
import requests
from time import  sleep


def getPic(url):
    global count
    image_folder = "image/"

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
    page = requests.get(url,headers=headers)
    soup = BeautifulSoup(page.text,'lxml')
    try:

        div = soup.find("div",{"class":"item_z_pic"}).find("img").get("src")
        url = "https:"+div
        page = requests.get(url,headers=headers)
        with open("{}{}.jpg".format(image_folder,count),"wb") as f:
            for i in page:
                f.write(i)
    except AttributeError:
        pass

def getStat():
    global count
    global total
    print("{}/{}".format(count,total))
csv_dir = "csv/"
files = os.listdir(csv_dir)
total = len(files)*100
count = 0
with open("data.csv","a") as data:
    writer = csv.writer(data)

    for file in files:
        filename = csv_dir+file
        with open(filename,"r") as f:
            reader = list(csv.reader(f))[8:-3]
            for line in reader:
                if count < 100000:
                    count +=1
                    getStat()
                    line.insert(0,count)
                    writer.writerow(line)
                    continue
                count +=1

                url = line[-1]
                getPic(url)
                # line.insert(0,count)
                # writer.writerow(line)

                getStat()
                if count%2 == 0:
                    sleep(10)
