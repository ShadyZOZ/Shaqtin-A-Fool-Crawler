import requests
from bs4 import BeautifulSoup

from db import VideoUrl

HOST = 'https://www.youtube.com'
URL = 'https://www.youtube.com/playlist?list=PLU6BYY1Lu_feVbuZEscpd6xT32zCrVrev'


def crawl():
    r = requests.get(URL)

    soup = BeautifulSoup(r.content, 'html.parser')

    links = soup.tbody.find_all('a', 'pl-video-title-link')

    url_list = [HOST + link['href'].split('&')[0] + '\n' for link in links]

    for url in url_list:
        try:
            v = VideoUrl(url=url)
            v.save()
        except Exception as e:
            print(e)
            break
