#위키백과 수집과 출력이 가능한 프로그램
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org' + pageUrl)
    bs = BeautifulSoup(html, 'html.parser')

    try:
        print(bs.h1.get_text())     #태그없이 안의 텍스트만 출력해주는 함수
        print(bs.find(id = 'mw-content-text').findAll('p')[0])
        print(bs.find(id = 'ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('This page is missing something! No worries though!')
    
    for link in bs.findAll('a', href = re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print('-----------\n' + newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks('')