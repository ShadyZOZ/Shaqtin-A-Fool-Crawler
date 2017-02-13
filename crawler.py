import requests

r = requests.get('https://www.youtube.com/playlist?list=PLU6BYY1Lu_feVbuZEscpd6xT32zCrVrev')
print(r.content)
