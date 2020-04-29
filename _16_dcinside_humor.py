from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup

# 웃긴대학 메인 페이지

headers={
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'
}

req = Request(url="http://web.humoruniv.com/main.html", headers=headers)
response = urlopen(req)

html = response.read()#.decode("ms949")
bs = BeautifulSoup(html, 'html.parser')

rankSection = bs.find('div',{'class':'best_right'})
ranks = rankSection.find('li').find_all('a')

for i, rank in enumerate(ranks):
    href = rank.attrs['href']
    text = rank.string
    rank = i + 1
    print(str(rank)+"위", text, ":" "http://web.humoruniv.com" +str(href))
