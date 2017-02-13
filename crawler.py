import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.youtube.com/playlist?list=PLU6BYY1Lu_feVbuZEscpd6xT32zCrVrev')

soup = BeautifulSoup(r.content)

links = soup.tbody.find_all('a')

for link in links:
    print(link['href'])
