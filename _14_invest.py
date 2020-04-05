from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://thevc.kr/')
bs = BeautifulSoup(html, 'html.parser')

rankSection = bs.find('div',{'class':'rank_section'})

rankList = rankSection.findAll('td')

for rank in rankList:
    print(rank.text.strip())
