import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from threading import Thread


class MyThread(Thread):
    def __init__(self,name,url):
        super(MyThread,self).__init__()
        self.name = name # name thread
        self.payload = {"signin[username]" : 'username', "signin[password]":'password'} # write your login data
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'} # useragent
        self.url = url # link for download



    def run(self):
        with requests.Session() as sess: # create session
            p = sess.post("https://colnect.com/ru/account/login",headers=self.headers,data=self.payload) #login on site
            s = sess.get(self.url,headers=self.headers) # get csv list from site
            print(self.name,end="\r") # write name thread for show count request
            with open("csv/{}.csv".format(self.name),"w")  as f: # write data to file
                f.write(s.text)


def colectRU():

    urls = [["https://colnect.com/en/chocolate_wrappers/csv_list/orientation/2-Square/page/",87],["https://colnect.com/en/chocolate_wrappers/csv_list/orientation/1-Horizontal/page/",1447],["https://colnect.com/en/chocolate_wrappers/csv_list/orientation/3-Vertical/page/",881]]
    all_urls = [] # list for all urls
    for url, num_pages in urls:
        for i in range(num_pages):
            all_urls.append(url+"{}".format(i+1))

    for i,url in enumerate(all_urls):
        thread = MyThread(i,url)
        thread.start()
        sleep(10)

def main():
    colectRU()

if __name__ == '__main__':
    main()
