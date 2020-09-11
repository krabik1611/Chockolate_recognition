import requests
from bs4 import BeautifulSoup
from threading import Thread
import os
import csv

count = 1


class MyThread(Thread):
    def __init__(self, name, urls):
        Thread.__init__(self)
        self.urls = urls
        self.name = name
        self.site = 'http://chocolader2.narod.ru/'

    def run(self):
        print("{} start".format(self.name))
        global count
        site = self.site
        for page in self.urls:
            page_request = requests.get(page)
            soup_page = BeautifulSoup(page_request.text, 'lxml')
            all_data = soup_page.findAll("table")

            for table in all_data:
                chock = table.find('a')
                if chock is not None:
                    img = chock.get("href")

                    description = table.find('td').text
                    try:
                        os.mkdir("image/" + str(img)[:str(img).find("/")])
                    except FileExistsError:
                        pass
                    image_path = "image/" + img
                    if image_path[-3:] == "jpg":
                        image_ref = page[:len(site) + 3] + img
                        image_request = requests.get(image_ref)
                        if image_request.status_code == 200:
                            print(count, image_path)
                            count += 1
                            with open(image_path, "wb") as image:
                                for i in image_request:
                                    image.write(i)
                                with open("data.csv", "a") as file:
                                    writer = csv.writer(file)
                                    writer.writerow([image_path, description])
                else:
                    continue

        print("{} complete".format(self.name))


def main():
    global count
    site = 'http://chocolader2.narod.ru/'

    site_request = requests.get(site)
    soup_site = BeautifulSoup(site_request.text, 'lxml')
    data = soup_site.find("th")
    factory = data.findAll("li")
    count = 1
    pages = []
    for line in factory:
        ref = line.find("a").get("href")
        if ref[2] == "/":
            pages.append(site + ref)

    part = int(len(pages) / 20)
    last = 0
    out = []
    while last < len(pages):
        out.append(pages[last: last + part])
        last += part
    for item, url in enumerate(out):
        name = "Thread #{}".format(item + 1)
        thread = MyThread(name, url)
        thread.start()


if __name__ == "__main__":
    main()
