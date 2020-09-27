import csv
import os
from bs4 import BeautifulSoup
import requests
from time import  sleep


def getPic(url):
    global count
    image_folder = "image/"

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}
    page = requests.get(url,headers=headers)
    soup = BeautifulSoup(page.text,'lxml')
    div = soup.find("div",{"class":"item_z_pic"}).find("img").get("src")
    url = "https:"+div
    page = requests.get(url,headers=headers)
    with open("{}{}.jpg".format(image_folder,count),"wb") as f:
        for i in page:
            f.write(i)

def getStat():
    global count
    global total
    print("{}/{}".format(count,total))
csv_dir = "csv/"
files = os.listdir(csv_dir)
total = len(files)
count = 0
with open("data.csv","w") as data:
    writer = csv.writer(data)

    for file in files:
        filename = csv_dir+file
        with open(filename,"r") as f:
            reader = list(csv.reader(f))[8:-3]
            for line in reader:
                count +=1
                url = line[-1]
                getPic(url)
                line.insert(0,count)
                writer.writerow(line)
                getStat()
                sleep(10)
