from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from time import sleep

URL = "https://www.instagram.com/{}/"


def getMeta(user):
    s = requests.get(URL.format(user))
    bs = BeautifulSoup(s.text, "html.parser")
    # print(bs)
    meta = bs.find("meta", property="og:description")
    name = bs.find("title")
    print(str(name).split("\n")[1].split("•")[0])
    return meta


def getInfo(meta):
    info = str(meta).split("-")[0]
    correct_info = info.split("\"")
    followers = correct_info[1].split(" ")[0]
    following = correct_info[1].split(" ")[2]
    posts = correct_info[1].split(" ")[4]
    dict = {"Followers": followers, "Following": following, "Posts": posts}
    return dict


if __name__ == '__main__':
    # browser = webdriver.Firefox()
    # sleep(5)
    # browser.get(URL)
    dict = getInfo(getMeta("nikolakanevce"))
    for i in dict:
        print(i + ": " + dict.get(i))
