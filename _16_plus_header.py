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

soup = BeautifulSoup(html, 'html.parser')

print(soup)