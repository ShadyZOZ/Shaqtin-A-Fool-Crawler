import requests
from bs4 import BeautifulSoup

host = 'https://www.youtube.com'
url = 'https://www.youtube.com/playlist?list=PLU6BYY1Lu_feVbuZEscpd6xT32zCrVrev'
r = requests.get(url)

soup = BeautifulSoup(r.content)

links = soup.tbody.find_all('a', 'pl-video-title-link')

url_list = [host + link['href'].split('&')[0] for link in links]

with open('urls.txt', 'wb+') as f:
    f.writelines(url_list)
