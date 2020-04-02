from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://rank.ezme.net/')
bs = BeautifulSoup(html, 'html.parser')

rankList = bs.findAll('span',{'class':'demo-card-image__filename'})

for rank in rankList:
    print(rank.text)
