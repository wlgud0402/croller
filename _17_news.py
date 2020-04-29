from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

html = urlopen('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%89%B4%EC%8A%A4&oquery=%EB%89%B4%EC%8A%A4&tqi=UqC7pwprvxsssdN8No4ssssstRN-514238')
bs = BeautifulSoup(html, 'html.parser')

rankSection = bs.find('ol',{'class':'lst_realtime_srch'})
rankHrefs = rankSection.find_all('a')

for i, rankHref in enumerate(rankHrefs):
    href = rankHref.attrs.get('href')
    text = rankHref.find('span',{'class':'tit'}).text
    rank = i + 1
    print(str(rank)+"위", text, ":" "https://search.naver.com/search.naver" +str(href))
    if i == 9:
        break
