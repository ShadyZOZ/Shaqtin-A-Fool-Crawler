import requests
from bs4 import BeautifulSoup

host = 'https://www.youtube.com'
url = 'https://www.youtube.com/playlist?list=PLU6BYY1Lu_feVbuZEscpd6xT32zCrVrev'
r = requests.get(url)

soup = BeautifulSoup(r.content)

links = soup.tbody.find_all('a', 'pl-video-title-link')

for link in links:
    print(host + link['href'])
