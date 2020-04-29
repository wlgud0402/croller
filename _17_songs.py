from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

html = urlopen('https://music.bugs.co.kr/')
bs = BeautifulSoup(html, 'html.parser')

rankSection = bs.find('tbody')
rankHrefs = rankSection.find_all('th')

# for i, rankHref in enumerate(rankHrefs):
#     href = rankHref.attrs.get('href')
#     text = rankHref.find('span',{'class':'tit'}).text
#     rank = i + 1
#     print(str(rank)+"위", text, ":" "https://search.naver.com/search.naver" +str(href))
#     if i == 9:
#         break

for rankHref in rankHrefs:
    link = rankHref.find('a').attrs.get('href')
    title = rankHref.find('p',{'class':'title'}).text.strip()
    print(title)