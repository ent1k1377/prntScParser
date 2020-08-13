import requests
from bs4 import BeautifulSoup
import random


def parse(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.2.195 Yowser/2.5 Safari/537.36'}

        html = requests.get(url, headers=headers).text
        soup = BeautifulSoup(html, 'lxml')
        img_tag = soup.find('img', {'id': 'screenshot-image'})
        photo_url = img_tag['src']

        photo = requests.get(photo_url, headers=headers).content
    except:
        return False
    return photo


abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
       't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def randomLink(num):
    links = []
    n = 0
    while len(links) != num:
        url = 'https://prnt.sc/' + ''.join([random.choice(abc) for i in range(0, 6)])
        photo = parse(url)
        if photo:
            links.append(url)
            with open(f'img/{url[::-1][0:6][::-1]}.png', 'wb') as f:
                f.write(photo)
            n += 1
            print(f'{n}/{num} изображения скачано!')


randomLink(50)
