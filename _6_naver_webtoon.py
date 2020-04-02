from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://comic.naver.com/webtoon/weekday.nhn')
bs = BeautifulSoup(html, 'html.parser')

webtoonspot = bs.find('div',{'class':'webtoon_spot2'})

titleList = webtoonspot.findAll('strong')

for title in titleList:
    print(title.text)

# webtoonspot = bs.find('div',{'class':'webtoon_spot2'})

# titleList = webtoonspot.findAll('strong')

# for title in titleList:
#     print(title.text)