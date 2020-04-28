from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

html = urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
bs = BeautifulSoup(html, 'html.parser')

rankSection = bs.find('tbody')
rankHrefs = rankSection.find_all('a')

for i, rankHref in enumerate(rankHrefs):
    href = rankHref.attrs['href']
    text = rankHref.string
    rank = i + 1
    print(str(rank)+"위", text, ":" "https://movie.naver.com" +str(href))

     






